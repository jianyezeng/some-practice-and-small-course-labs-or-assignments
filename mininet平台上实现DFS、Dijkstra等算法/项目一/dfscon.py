from collections import defaultdict
from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.topology import event
from ryu.controller.handler import MAIN_DISPATCHER, CONFIG_DISPATCHER
from ryu.controller.handler import set_ev_cls
from ryu.ofproto import ofproto_v1_3
from ryu.lib.packet import packet
from ryu.lib.packet import ethernet
from ryu.lib.packet import ether_types
from ryu.topology.api import get_switch, get_all_link, get_link
import copy
import random
from ryu.lib.packet import arp
from ryu.lib.packet import ipv6
from ryu.lib import mac

import os
import networkx as nx
import matplotlib.pyplot as plt

def draw_graph(graph, path, index, head=0, rear=0):
    """画图"""
    plt.figure()
    #从图中提取节点
    nodes = set([n1 for n1, n2 in graph] + [n2 for n1, n2 in graph])
    #定义图表
    gra = nx.Graph()

    for node in nodes:
        gra.add_node(node)

    gra.add_edges_from(graph, color='b')
    gra.add_edges_from(path, color='r')

    edges = gra.edges()
    colors = [gra[u][v]['color'] for u, v in edges]

    nx.draw(gra, with_labels=True, edge_color=colors)

    #判断是否有名为photos的文件夹用于存储图片，若没有则创建一个
    if not os.path.exists("./photos/"):
        os.mkdir("./photos/")
    plt.savefig('./photos/' + 'index' + str(index) + ":" + str(head) + "-" + str(rear) + ".png")
    plt.savefig('now_photo.png')


class topo(object):
    """topo类"""
    def __init__(self, logger):
        """对参数进行初始化"""
        self.adjacent = defaultdict(lambda s1s2: None)#adjacent 存储两交换机间的接口信息以及边的权重；
        self.switches = None
        self.host_mac_to = {}
        self.logger = logger

    def reset(self):
        """将topo类的属性重置"""
        self.adjacent = defaultdict(lambda s1s2: None)
        self.switches = None
        self.host_mac_to = None

    def get_adjacent(self, s1, s2):
        """调用adjacent"""
        return self.adjacent.get((s1, s2))

    def set_adjacent(self, s1, s2, port):
        """将 两 交 换 机 间 的 接 口 和 边权存入adjacent中"""
        self.adjacent[(s1, s2)] = port

    def findpath(self, beg, end, sign, onepath, allpaths):
        """通过DFS算法探索所有路径,在探索过程中，onepath存储一条路径，并在到达终点时将其作为一个元素存入allpath列表中"""
        if beg == end:#处理开始点与结束点相同的情况
            allpaths.append(onepath.copy())
        else:
            for u in self.switches:
                if (self.get_adjacent(beg, u) is not None) and (sign[u] != 1):
                    sign[u] = 1
                    onepath.append(u)
                    self.findpath(u, end, sign, onepath, allpaths)
                    onepath.remove(u)
                    sign[u] = 0

    def longest_path(self, beg, end, first_port, last_port):
        """得到最长路"""
        self.logger.info(
            "topo calculate the longest path from ---{}-{}-------{}-{}".format(first_port, beg, end, last_port))
        self.logger.debug("there is {} swithes".format(len(self.switches)))

        sign = {}
        for s in self.switches:
            sign[s] = 0
        sign[beg] = 1

        onepath = []
        onepath.append(beg)

        #使用之前的findpath方法找到两个节点之间所有路径并将其存在allpaths中
        allpaths = []
        self.findpath(beg, end, sign, onepath, allpaths)

        #打印出所有路径
        print("paths num is: {}".format(len(allpaths)))
        print("all paths:")
        sp = allpaths[0]
        lp = allpaths[0]
        for i in allpaths:
            if (len(i) > len(lp)):
                lp = i
            if (len(i) < len(sp)):
                sp = i
            print(i)

        #打印出最短路和最长路
        print("the shortest path is: ")
        print(sp)
        print("the longest path is: ")
        print(lp)

        if beg == end:
            path = [beg]
        else:
            path = lp

        #将两个交换机之间的输入和输出端口以Ryu能识别的方式记录在record
        record = []
        inport = first_port

        # s1 s2; s2:s3, sn-1  sn
        for s1, s2 in zip(path[:-1], path[1:]):
            outport = self.get_adjacent(s1, s2)

            record.append((s1, inport, outport))
            inport = self.get_adjacent(s2, s1)

        record.append((end, inport, last_port))
        return record, lp


# TODO Port status monitor

class DFSController(app_manager.RyuApp):
    """控制器配置"""
    OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION]#表明使用的openflow版本为1.3

    def __init__(self, *args, **kwargs):
        """将控制器初始化处理"""
        super(DFSController, self).__init__(*args, **kwargs)
        self.mac_to_port = {}
        ## datapaths为OpenFlow下的各个交换机
        self.datapaths = []

        self.topo = topo(self.logger)

        #于判断某交换机是否泛洪过特定的发送源 mac 到目标 mac
        self.flood_history = {}

        self.arp_table = {}
        self.rarp_table = {}
        self.arp_history = {}

        self.initshow = 0
        self.index = 1
        self.lp_path = []

    def _find_dp(self, dpid):
        for dp in self.datapaths:
            if dp.id == dpid:
                return dp
        return None

    #fp_event.EventOFPSwitchFeatures 事件到来且处于 CONFIG_DISPATCHER 阶段时触发方法 switch_features_handler
    @set_ev_cls(ofp_event.EventOFPSwitchFeatures, CONFIG_DISPATCHER)
    def switch_features_handler(self, ev):
        """交换机向控制器传输自身的features信息，并将优先级设为最低，并添加到流表"""
        datapath = ev.msg.datapath
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser

        #match为流表的匹配域，在此初始化
        match = parser.OFPMatch()
        #actions为流表动作
        actions = [parser.OFPActionOutput(ofproto.OFPP_CONTROLLER,
                                          ofproto.OFPCML_NO_BUFFER)]
        self.add_flow(datapath, 0, match, actions)

    def add_flow(self, datapath, priority, match, actions, buffer_id=None):
        """控制器对交换机添加流表"""
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser

        inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS,
                                             actions)]
        if buffer_id:
            mod = parser.OFPFlowMod(datapath=datapath, buffer_id=buffer_id,
                                    priority=priority, match=match,
                                    instructions=inst)
        else:
            mod = parser.OFPFlowMod(datapath=datapath, priority=priority,
                                    match=match, instructions=inst)
        datapath.send_msg(mod)

    def configure_path(self, longest_path, event, src_mac, dst_mac):
        #在两节点之间配置最长路
        msg = event.msg
        datapath = msg.datapath

        ofproto = datapath.ofproto

        parser = datapath.ofproto_parser

        for switch, inport, outport in longest_path:
            match = parser.OFPMatch(in_port=inport, eth_src=src_mac, eth_dst=dst_mac)
            actions = [parser.OFPActionOutput(outport)]
            datapath = self._find_dp(int(switch))
            assert datapath is not None

            inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS, actions)]

            mod = datapath.ofproto_parser.OFPFlowMod(
                datapath=datapath,
                match=match,
                idle_timeout=0,
                hard_timeout=0,
                priority=1,
                instructions=inst
            )
            datapath.send_msg(mod)

    #当交换机发送数据包给控制器时且在特性消息接受到后到断开连接前的阶段触发
    @set_ev_cls(ofp_event.EventOFPPacketIn, MAIN_DISPATCHER)
    def packet_in_handler(self, event):

        msg = event.msg

        #取出数据包内的信息
        datapath = msg.datapath
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser

        in_port = msg.match['in_port']

        pkt = packet.Packet(msg.data)

        eth = pkt.get_protocols(ethernet.ethernet)[0]

        #对LLDP类型数据包不处理
        if eth.ethertype == ether_types.ETH_TYPE_LLDP:
            return

        #得到起点和终点的mac地址
        dst_mac = eth.dst
        src_mac = eth.src

        # 检查这是否是一个arp包
        arp_pkt = pkt.get_protocol(arp.arp)
        if arp_pkt:
            self.arp_table[arp_pkt.src_ip] = src_mac


        dpid = datapath.id

        self.mac_to_port.setdefault(dpid, {})

        self.mac_to_port[dpid][src_mac] = in_port

        self.flood_history.setdefault(dpid, [])
        #ipv6协定的广播数据包的目的 MAC 地址以 33：33 开头，如果之前控制器没有 flood 该数据包就进行记
        if '33:33' in dst_mac[:5]:
            if (src_mac, dst_mac) not in self.flood_history[dpid]:
                self.flood_history[dpid].append((src_mac, dst_mac))
            else:
                return

        if src_mac not in self.topo.host_mac_to.keys():
            self.topo.host_mac_to[src_mac] = (dpid, in_port)

        if dst_mac in self.topo.host_mac_to.keys():

            final_port = self.topo.host_mac_to[dst_mac][1]
            src_switch = self.topo.host_mac_to[src_mac][0]
            dst_switch = self.topo.host_mac_to[dst_mac][0]

            # 用 longest_path 函数计算最长路径
            longest_path, lp = self.topo.longest_path(
                src_switch,
                dst_switch,
                in_port,
                final_port)

            if lp not in self.lp_path:
                graph = []
                for a in self.topo.switches:
                    for b in self.topo.switches:
                        if self.topo.get_adjacent(a, b) is not None:
                            graph.append((a, b))
                graph_path = []
                for i in range(len(lp) - 1):
                    graph_path.append((lp[i], lp[i + 1]))
                    graph_path.append((lp[i + 1], lp[i]))
                draw_graph(graph, graph_path, self.index, lp[0], lp[-1])
                self.index += 1
                self.lp_path.append(lp)

            self.logger.info(
                "The longest path from {} to {} contains {} switches".format(src_mac, dst_mac, len(longest_path)))

            assert len(longest_path) > 0

            #打印出两个节点之间的最长路
            path_str = ''

            for s, ip, op in longest_path:
                path_str = path_str + "--{}-{}-{}--".format(ip, s, op)

            self.logger.info("The longset path from {} to {} is {}".format(src_mac, dst_mac, path_str))

            self.logger.info("Have calculated the longest path from {} to {}".format(src_mac, dst_mac))

            self.logger.info("Now configuring switches of interest")

            self.configure_path(longest_path, event, src_mac, dst_mac)

            self.logger.info("Configure done")

            out_port = None
            for s, _, op in longest_path:
                if s == dpid:
                    out_port = op

        else:
            if self.arp_handler(msg):
                return
            out_port = ofproto.OFPP_FLOOD

        actions = [parser.OFPActionOutput(out_port)]

        data = None

        if msg.buffer_id == ofproto.OFP_NO_BUFFER:
            data = msg.data

        out = parser.OFPPacketOut(
            datapath=datapath,
            buffer_id=msg.buffer_id,
            in_port=in_port,
            actions=actions,
            data=data
        )
        datapath.send_msg(out)


    #拓扑发现
    @set_ev_cls(event.EventSwitchEnter)
    def switch_enter_handler(self, event):
        """交换机进入"""
        self.logger.info("A switch entered.Topology rediscovery...")
        self.switch_status_handler(event)
        self.logger.info('Topology rediscovery done')

    @set_ev_cls(event.EventSwitchLeave)
    def switch_leave_handler(self, event):
        """交换机离开"""
        self.logger.info("A switch leaved.Topology rediscovery...")
        self.switch_status_handler(event)
        self.logger.info('Topology rediscovery done')

    def switch_status_handler(self, event):
        """使用副本避免对 network 产生影响"""

        all_switches = copy.copy(get_switch(self, None))

        # 获取交换机的ID值
        self.topo.switches = [s.dp.id for s in all_switches]

        self.logger.info("switches {}".format(self.topo.switches))

        self.datapaths = [s.dp for s in all_switches]

        all_links = copy.copy(get_link(self, None))

        all_link_stats = [(l.src.dpid, l.dst.dpid, l.src.port_no, l.dst.port_no) for l in all_links]
        self.logger.info("Number of links {}".format(len(all_link_stats)))

        all_link_repr = ''

        for s1, s2, p1, p2 in all_link_stats:
            self.topo.set_adjacent(s1, s2, p1)
            self.topo.set_adjacent(s2, s1, p2)

            all_link_repr += 's{}p{}--s{}p{}\n'.format(s1, p1, s2, p2)
        self.logger.info("All links:\n " + all_link_repr)


        #将拓扑结构可视化展示。
        self.initshow += 1
        if self.initshow == 13:
            graph = []
            for a in self.topo.switches:
                for b in self.topo.switches:
                    if self.topo.get_adjacent(a, b) is not None:
                        graph.append((a, b))
            graph_path = []
            draw_graph(graph, graph_path, self.index)
            self.index += 1

    def arp_handler(self, msg):
        """处理arp请求"""
        datapath = msg.datapath
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser
        in_port = msg.match['in_port']

        pkt = packet.Packet(msg.data)

        eth = pkt.get_protocols(ethernet.ethernet)[0]
        arp_pkt = pkt.get_protocol(arp.arp)

        if eth:
            eth_dst = eth.dst
            eth_src = eth.src

        if eth_dst == mac.BROADCAST_STR and arp_pkt:
            arp_dst_ip = arp_pkt.dst_ip

            if (datapath.id, eth_src, arp_dst_ip) in self.arp_history:

                if self.arp_history[(datapath.id, eth_src, arp_dst_ip)] != in_port:
                    return True
            else:
                self.arp_history[(datapath.id, eth_src, arp_dst_ip)] = in_port


        #在得到 arp 头参数后构建 arp 数据包
        if arp_pkt:

            hwtype = arp_pkt.hwtype
            proto = arp_pkt.proto
            hlen = arp_pkt.hlen
            plen = arp_pkt.plen

            opcode = arp_pkt.opcode

            arp_src_ip = arp_pkt.src_ip
            arp_dst_ip = arp_pkt.dst_ip

        #从 arp 请求和 arp 回复得到 arp table。
            if opcode == arp.ARP_REQUEST:
                if arp_dst_ip in self.arp_table:
                    actions = [parser.OFPActionOutput(in_port)]
                    arp_reply = packet.Packet()

                    arp_reply.add_protocol(ethernet.ethernet(
                        ethertype=eth.ethertype,
                        dst=eth_src,
                        src=self.arp_table[arp_dst_ip]))

                    arp_reply.add_protocol(arp.arp(
                        opcode=arp.ARP_REPLY,
                        src_mac=self.arp_table[arp_dst_ip],
                        src_ip=arp_dst_ip,
                        dst_mac=eth_src,
                        dst_ip=arp_src_ip))

                    arp_reply.serialize()
                    out = parser.OFPPacketOut(
                        datapath=datapath,
                        buffer_id=ofproto.OFP_NO_BUFFER,
                        in_port=ofproto.OFPP_CONTROLLER,
                        actions=actions, data=arp_reply.data)
                    datapath.send_msg(out)

                    return True
        return False