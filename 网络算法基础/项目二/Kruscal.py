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
from ryu.lib.packet import arp
from ryu.lib.packet import ipv6
from ryu.lib import mac

import networkx as nx

import matplotlib.pyplot as plt

import copy
import random
import numpy as np


def draw(Matrix, linkList1):
    """画图,生成图片"""
    G = nx.Graph()
    weight = {}
    graph = []
    for i in range(len(Matrix)):
        for j in range(i):
            if Matrix[i][j] > 0 and Matrix[i][j] < 1000000:
                graph.append((i + 1, j + 1))
                graph.append((j + 1, i + 1))
                weight[(i + 1, j + 1)] = int(Matrix[i][j])
                weight[(j + 1, i + 1)] = int(Matrix[i][j])

    path = []
    for link1 in linkList1:
        path.append((link1[0] + 1, link1[1] + 1))
        path.append((link1[1] + 1, link1[0] + 1))

    for gra in graph:
        G.add_edge(gra[0], gra[1], color='black')

    for pat in path:
        G.add_edge(pat[0], pat[1], color='red')
    pos = nx.spring_layout(G)
    edges = G.edges()
    colors = [G[u][v]['color'] for u, v in edges]
    nx.draw_networkx_nodes(G, pos, node_size=300)
    nx.draw_networkx_edges(G, pos, width=2, edge_color=colors, node_shape='p')
    nx.draw_networkx_labels(G, pos, font_size=13)

    nx.draw_networkx_edge_labels(G, pos, weight, font_size=10)

    plt.savefig('now_photo.png')


class Topo(object):
    def __init__(self, logger):
        self.switches = None
        self.host_mac_to = {}
        self.logger = logger
        self.edges = {}
        self.weights = 0;
        self.edge_weight = None;
        self.flag = 0

    def edges_weight(self):
        """给各边赋权重"""
        edge_weight = np.array(np.ones((20, 20)) * 1000000)

        for (s, t) in self.edges.keys():
            edge_weight[s - 1][t - 1] = random.randint(1, 10)
            # 保证两个节点到彼此的权重相同
            edge_weight[t - 1][s - 1] = edge_weight[s - 1][t - 1]

        return edge_weight

    def kruskal(self, edge_weight):
        """实现 Kruscal 算法，返回最小生成树各边"""
        """思路:先将所有连通的边加入linked_edge列表中，再使用Kruscal算法找到最小生成树，并存储各边至mst_edge中"""
        node_num = len(edge_weight)
        edge_num = 0

        # 得到边的个数
        for i in range(node_num):
            for j in range(i):
                if edge_weight[i][j] > 0 and edge_weight[i][j] < 10000000:
                    edge_num += 1

        mst_edge = []

        # 如果边的数量小于点的数量-1，即不是全连通，直接返回
        if edge_num < node_num - 1:
            return mst_edge

        linked_edge = []
        # 将连通的边加入linked_edge
        for i in range(node_num):
            # 从i开始，遍历剩下的点
            for j in range(i + 1, node_num):
                # 如果两个节点之间存在边
                if edge_weight[i][j] < 10000000:
                    # 将该边加入集合，形式为[节点i,节点j,权重]
                    linked_edge.append([i, j, edge_weight[i][j]])
                    # i, j均从0开始，为0--12；所给图连通的边均加入linked_edge

        # 将边按第二个元素即权重排序，边权重从小到大
        linked_edge.sort(key=lambda x: x[2])

        # 创建节点列表
        forest = [[i] for i in range(node_num)]
        # 每次取权重最小的边

        for edge in linked_edge:
            for i in range(len(forest)):
                if edge[0] in forest[i]:  # 边的左结点在该树内
                    m = i
                if edge[1] in forest[i]:  # 边的右结点在该树内
                    n = i

            # m==n时，即两结点均在该树内
            # m!=n时，合并树
            if m != n:
                mst_edge.append(edge)
                forest[m] = forest[m] + forest[n]
                forest[n] = []

        return mst_edge  # kruskal算法计算出的最小生成树所含边

    def find_neighbors(self, src, list):
        """找到各结点的邻接结点，存储在二维列表 neighbors"""
        neighbors = [[] for i in range(len(list) + 1)]  # 最小生成树边为n-1条，要加1
        for i in range(len(list) + 1):
            for edge in list:
                if i == edge[0]:
                    neighbors[i].append(edge[1])
                elif i == edge[1]:
                    neighbors[i].append(edge[0])
        return neighbors
        # 某个结点的邻接结点 e.g.neighbors[0]=[1,2,3]表示结点0邻接结点1，2，3

    # src 当前操作的结点;pre_src 上一个结点
    def find_links(self, src, pre_src, links):
        result = []
        if len(links[src]) < 1:
            return result

        for node in links[src]:
            if node != pre_src:
                result.append((pre_src, src, node))
                newresult = self.find_links(node, src, links)
                result.extend(newresult)

        return result

    def cal_flowTables(self, src_dw, first_port):
        """收到包之后调用该函数，计算流表的转发，流表匹配源ip，向生成树上其他端口转发"""
        if self.weights == 0:
            self.edge_weight = self.edges_weight()
            self.weights = 1
        edgeList = self.kruskal(self.edge_weight)
        nodes_neighbor = self.find_neighbors(src_dw - 1, edgeList)  # 每个结点邻接的结点列表
        links = self.find_links(src_dw - 1, None, nodes_neighbor)  # （前个结点，当前结点，后个结点）
        print('起始结点为：', src_dw)  # 打印起始的结点
        if self.flag == 0:
            draw(self.edge_weight, edgeList)
            self.flag = 1
        edgeList1 = edgeList.copy()
        for i in range(len(edgeList1)):
            edgeList1[i][0] += 1
            edgeList1[i][1] += 1
        print('最小生成树各边包括：', edgeList1)  # 打印最小生成树各边

        temp1 = {}  # key为两个邻接的结点，value为两个邻接结点中后一个结点邻接的结点列表
        for link in links:
            if (link[0], link[1]) not in temp1.keys():
                temp1[(link[0], link[1])] = [link[2]]
            else:
                temp1[(link[0], link[1])].append(link[2])

        temp2 = []
        index = [key[1] for key in temp1.keys()]
        # temp1中每个key中的第二个结点组成的列表，即为邻接结点大于等于2个的结点
        for i in range(20):
            if i not in index:
                for key in temp1.keys():
                    if i in temp1[key]:
                        temp2.append((key[1], i, None))
                        # 中间结点无后继
            else:
                for key in temp1.keys():
                    if i == key[1]:
                        temp2.append((key[0], key[1], temp1[key]))
                        # 中间结点有后继，有/无前继

        ryu_FlowTables = []
        # 根据Ryu的格式配置流表路径
        for item in temp2:
            if item[0] is not None:
                if item[2] is None:
                    inport = self.edges[(item[1] + 1, item[0] + 1)]
                    outportList = [1]
                    ryu_FlowTables.append((item[1] + 1, inport, outportList))
                else:
                    inport = self.edges[(item[1] + 1, item[0] + 1)]
                    outportList = [1]
                    for node in item[2]:
                        op = self.edges[(item[1] + 1, node + 1)]
                        outportList.append(op)
                    ryu_FlowTables.append((item[1] + 1, inport, outportList))
            else:
                inport = first_port
                outportList = [1]
                for node in item[2]:
                    op = self.edges[(item[1] + 1, node + 1)]
                    outportList.append(op)
                ryu_FlowTables.append((item[1] + 1, inport, outportList))

        return ryu_FlowTables, nodes_neighbor
# Ryu控制器
class KruscalController(app_manager.RyuApp):
    # 指明OpenFlow版本
    OFP_VERSIONS=[ofproto_v1_3.OFP_VERSION]

    def __init__(self,*args,**kwargs):
        super(KruscalController,self).__init__(*args,**kwargs)
        
        self.mac_to_port={} # 全局的mac表,{{datapath:mac->port},...,{datapath:mac->port}}
        self.datapaths=[]
        self.flood_history={}   # 泛洪历史表
        self.arp_history={} # arp历史表
        self.flag = False
        self.mac_list = { 1: '00:00:00:00:00:01',
                          2: '00:00:00:00:00:02',
                          3: '00:00:00:00:00:03',
                          4: '00:00:00:00:00:04',
                          5: '00:00:00:00:00:05',
                          6: '00:00:00:00:00:06',
                          7: '00:00:00:00:00:07',
                          8: '00:00:00:00:00:08',
                          9: '00:00:00:00:00:09',
                          10: '00:00:00:00:00:10',
                          11: '00:00:00:00:00:11',
                          12: '00:00:00:00:00:12',
                          13: '00:00:00:00:00:13',
                          14: '00:00:00:00:00:14',
                          15: '00:00:00:00:00:15',
                          16: '00:00:00:00:00:16',
                          17: '00:00:00:00:00:17',
                          18: '00:00:00:00:00:18',
                          19: '00:00:00:00:00:19',
                          20: '00:00:00:00:00:ff'}

        self.arp_table = {'192.168.0.1':'00:00:00:00:00:01',
                          '192.168.0.2':'00:00:00:00:00:02',
                          '192.168.0.3':'00:00:00:00:00:03',
                          '192.168.0.4':'00:00:00:00:00:04',
                          '192.168.0.5':'00:00:00:00:00:05',
                          '192.168.0.6':'00:00:00:00:00:06',
                          '192.168.0.7':'00:00:00:00:00:07',
                          '192.168.0.8':'00:00:00:00:00:08',
                          '192.168.0.9':'00:00:00:00:00:09',
                          '192.168.0.10':'00:00:00:00:00:10',
                          '192.168.0.11':'00:00:00:00:00:11',
                          '192.168.0.12':'00:00:00:00:00:12',
                          '192.168.0.13':'00:00:00:00:00:13',
                          '192.168.0.14':'00:00:00:00:00:14',
                          '192.168.0.15':'00:00:00:00:00:15',
                          '192.168.0.16':'00:00:00:00:00:16',
                          '192.168.0.17':'00:00:00:00:00:17',
                          '192.168.0.18':'00:00:00:00:00:18',
                          '192.168.0.19':'00:00:00:00:00:19',
                          '192.168.0.255':'00:00:00:00:00:ff' 
                          }
         
        self.topo = Topo(self.logger)
    
    # 由dpid找到相应的datapath
    def find_dp(self,dpid):
        for dp in self.datapaths:
            if dp.id==dpid:
                return dp
        return None
    
    # 向控制器传输交换机特征
    @set_ev_cls(ofp_event.EventOFPSwitchFeatures, CONFIG_DISPATCHER)
    def switch_features_handler(self, ev):
        datapath = ev.msg.datapath
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser

        match = parser.OFPMatch()
        actions = [parser.OFPActionOutput(ofproto.OFPP_CONTROLLER,
                                          ofproto.OFPCML_NO_BUFFER)]
        self.add_flow(datapath, 0, match, actions)

    # 添加流表
    def add_flow(self, datapath, priority, match, actions, buffer_id=None):
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

    # 配置路径
    def configure_path(self,path,event,src_mac,dst_mac):
        msg=event.msg
        datapath=msg.datapath
        ofproto=datapath.ofproto
        parser=datapath.ofproto_parser

        for switch,inport,outportList in path:
            match=parser.OFPMatch(in_port=inport,eth_src=src_mac,eth_dst=dst_mac)
            actions = []

            for outport in outportList:
                actions.append(parser.OFPActionOutput(outport))
            
            # 由dpid找到对应的datapath
            datapath=self.find_dp(int(switch))
            assert datapath is not None

            inst=[parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS,actions)]

            mod=datapath.ofproto_parser.OFPFlowMod(
                datapath=datapath,
                match=match,
                idle_timeout=0,
                hard_timeout=0,
                priority=1,
                instructions=inst
            )
            # 下发流表
            datapath.send_msg(mod)

    #监听Packet_in事件
    @set_ev_cls(ofp_event.EventOFPPacketIn,MAIN_DISPATCHER)
    def packet_in_handler(self,event):
        msg=event.msg
        datapath=msg.datapath
        ofproto=datapath.ofproto
        parser=datapath.ofproto_parser

        in_port=msg.match['in_port']

        #获取数据
        pkt=packet.Packet(msg.data)

        #假设为以太帧，获取帧头
        eth=pkt.get_protocols(ethernet.ethernet)[0]
        
        #直接下发生成树流表
        if self.flag == False:
            for i in range(20):
                i = i+1
                path1,nodes_neighbor = self.topo.cal_flowTables(
                    i,
                    1)
                print('switches_path', path1)
                for nodes_n in range(20):
                    nodes_n += 1
                    #给路径中交换机下发流表
                    self.configure_path(path1,event,self.mac_list[i],self.mac_list[nodes_n])
                    path2, nodes_neighbor = self.topo.cal_flowTables(
                        nodes_n,
                        1)
                    #下发回路
                    self.configure_path(path2,event,self.mac_list[nodes_n],self.mac_list[i])
                    # [(nodes_n,1,[self.topo.edges[(nodes_n,i)]]),(i,self.topo.edges[(i,nodes_n)],[1])]
            print('----------------done----------------')
            
            self.flag = True
                 
        #丢弃LLDP帧
        if eth.ethertype==ether_types.ETH_TYPE_LLDP:
            return
  
        dst_mac=eth.dst
        src_mac=eth.src
        
        arp_pkt = pkt.get_protocol(arp.arp)
        if arp_pkt:
            self.arp_table[arp_pkt.src_ip] = src_mac

        dpid=datapath.id
        self.mac_to_port.setdefault(dpid,{})
        self.mac_to_port[dpid][src_mac]=in_port
        self.flood_history.setdefault(dpid,[])
        
        if '33:33' in dst_mac[:5]:
            if (src_mac,dst_mac) not in self.flood_history[dpid]:
                self.flood_history[dpid].append((src_mac,dst_mac))
            else:
                return
                      
        if src_mac not in self.topo.host_mac_to.keys():
            self.topo.host_mac_to[src_mac]=(dpid,in_port)
        
        if dst_mac in self.topo.host_mac_to.keys():
            final_port=self.topo.host_mac_to[dst_mac][1]
            src_switch=self.topo.host_mac_to[src_mac][0]
            dst_switch=self.topo.host_mac_to[dst_mac][0]
            mst_path, _=self.topo.cal_flowTables(
                1,
                1)
            assert len(mst_path)>0
                        
            self.configure_path(mst_path,event,src_mac,dst_mac)
            self.logger.info("Configure done")

            out_port=[]
            for s,_,op in mst_path:
                if s==dpid:
                    out_port=op
        
        else: 
            if self.arp_handler(msg):  
                return 

            out_port=[]
            out_port.append(ofproto.OFPP_FLOOD)

    
    # 交换机进入时触发
    @set_ev_cls(event.EventSwitchEnter)
    def switch_enter_handler(self,event):
        self.logger.info("一个交换机进入，重新发现拓扑")
        self.switch_status_handler(event)
        self.logger.info('拓扑发现完毕')

    # 交换机离开时触发
    @set_ev_cls(event.EventSwitchLeave)
    def switch_leave_handler(self,event):
        self.logger.info("一个交换机退出，重新发现拓扑")
        self.switch_status_handler(event)
        self.logger.info('拓扑发现完毕')

    # 配置交换机状态与打印连通信息
    def switch_status_handler(self,event):
        all_switches=copy.copy(get_switch(self,None))

        # 获取交换机的ID值
        self.topo.switches=[s.dp.id for s in all_switches]

        self.logger.info("switches {}".format(self.topo.switches))
        
        self.datapaths=[s.dp for s in all_switches]

        all_links=copy.copy(get_link(self,None))

        all_link_stats=[(l.src.dpid,l.dst.dpid,l.src.port_no,l.dst.port_no) for l in all_links]
        self.logger.info("Number of links {}".format(len(all_link_stats)))

        all_link_repr=''

        for s1,s2,p1,p2 in all_link_stats:
            
            self.topo.edges[(s1,s2)]=p1
            self.topo.edges[(s2,s1)]=p2

            all_link_repr+='s{}p{}--s{}p{}\n'.format(s1,p1,s2,p2)
        self.logger.info("All links:\n "+all_link_repr)
    
    def arp_handler(self, msg):
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
        
        if arp_pkt:
            hwtype = arp_pkt.hwtype
            proto = arp_pkt.proto
            hlen = arp_pkt.hlen
            plen = arp_pkt.plen
            
            opcode = arp_pkt.opcode

            arp_src_ip = arp_pkt.src_ip
            arp_dst_ip = arp_pkt.dst_ip

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

