from collections import defaultdict
from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.topology import event
from ryu.controller.handler import MAIN_DISPATCHER,CONFIG_DISPATCHER
from ryu.controller.handler import set_ev_cls
from ryu.ofproto import ofproto_v1_3
from ryu.lib.packet import packet
from ryu.lib.packet import ethernet
from ryu.lib.packet import ether_types
from ryu.topology.api import get_switch,get_all_link,get_link
import os 
import copy
import random
from ryu.lib.packet import arp
from ryu.lib import mac
import networkx as nx
import matplotlib.pyplot as plt

def draw_graph(graph,path,weight):
    nodes = set([n1 for n1, n2 in graph] + [n2 for n1, n2 in graph])
    G=nx.Graph()
    for node in nodes:
        G.add_node(node)
 
    G.add_edges_from(graph,color='purple')
    G.add_edges_from(path,color='orange')

    pos=nx.spring_layout(G)
    edges = G.edges()
    colors = [G[u][v]['color'] for u,v in edges]

    nx.draw_networkx_nodes(G,pos,node_size=400)
    nx.draw_networkx_edges(G,pos,width=2,edge_color=colors)
    nx.draw_networkx_labels(G,pos,font_size=10)
      
    nx.draw_networkx_edge_labels(G,pos,weight,font_size=7)

    if not os.path.exists("./show_photo/"):
        os.mkdir("./show_photo/")
    if path != []:
        plt.savefig('./show_photo/' + str(path[0][0]) + "---" + str(path[-1][0]) + ".png")
    else:
        plt.savefig('./show_photo/Topo.png')
        plt.savefig('Topo.png')
    plt.savefig('now_photo.png')
    plt.close()

class Topo(object):
    def __init__(self,logger):

        self.switches=None
        self.graph = None

        self.host_mac_to={}
        self.logger=logger
        self.flag=[]
        self.weight = None
        self.edges={}

    # 使用循环桶实现Dijkstra算法求最短路
    def compute_path(self,src_sw,dst_sw,first_port,last_port):
        bucket = []
        for i in range(6):
            bucket.append([])
        node_s = (0, src_sw)            # 源节点二元组（距离标记，节点）
        d = {} #距离
        for u in self.switches:
            d[u] = 9999999
        d[src_sw] = 0
        pre = {}                    # 父节点

        bucket[0].append(node_s)
        flag = 0
        point={} #记录在桶中的相应位置
        point[src_sw]=0
        while bucket != [[]]*6 :   # 所有的桶未空
            min_list = bucket[flag] #抽取一个桶中的元素
            while not len(min_list) == 0:
                min_node = min_list.pop()  #这个桶出一个节点
                del point[min_node[1]]  #删去这个节点在桶中的指向
                if (min_node[1] == dst_sw):
                    break

                for u in self.switches:
                    if(min_node[1]==u):
                        continue
                    if (min_node[1],u) in self.edges:
                        if (d[min_node[1]] + (self.edges[(min_node[1],u)])[1] < d[u]):   #更短就更新桶中的节点位置
                            pre[u] = min_node[1]
                            if u in point:
                                bucket[point[u]].remove((d[u], u))
                            d[u] = d[min_node[1]] + self.edges[(min_node[1],u)][1]  #更新距离
                            bucket[d[u] % 6].append((d[u], u))  #重新加入桶
                            point[u] = d[u] % 6 #循环利用桶所以取模
            flag += 1
            if flag > 5:
                flag %= 6 #大于桶的长度取模循环
        
        current_path=[]
        s = dst_sw
        while s != src_sw:
            current_path.append(s)
            s = pre[s]
        current_path.append(src_sw)

        current_path.reverse()

        graph=[]
        weight={}
        for a in self.switches:
            for b in self.switches:
                if a==b:
                    continue;
                if (a,b) in self.edges:
                    graph.append((a,b))
                    weight[(a,b)] = self.edges[(a,b)][1]
        graph_path=[]
        for i in range(len(current_path)-1):
            graph_path.append((current_path[i],current_path[i+1]))
            graph_path.append((current_path[i+1],current_path[i]))

        self.weight = weight
        self.graph = graph

        print("the shortest path is: ")
        print(current_path)

        if src_sw==dst_sw:
                path=[src_sw]
        else:
                path=current_path
            
        record=[]
        inport=first_port

        for s1,s2 in zip(path[:-1],path[1:]):
            outport,_=self.edges[(s1,s2)]
                
            record.append((s1,inport,outport))
            inport,_=self.edges[(s2,s1)]
            
        record.append((dst_sw,inport,last_port))

        return record,graph_path

# Ryu控制器
class DijkstraController(app_manager.RyuApp):
    # 指明OpenFlow版本
    OFP_VERSIONS=[ofproto_v1_3.OFP_VERSION]

    def __init__(self,*args,**kwargs):
        super(DijkstraController,self).__init__(*args,**kwargs)
        self.mac_to_port={} # 全局的mac表,{{datapath:mac->port},...,{datapath:mac->port}}
        self.datapaths=[]
        self.initshow = 0
        self.flag = []
        self.arp_table={}

        self.topo=Topo(self.logger)
        self.flood_history={}   # 泛洪历史表

        self.arp_history={} # arp历史表
    
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
    def configure_path(self,shortest_path,event,src_mac,dst_mac):
        msg=event.msg
        datapath=msg.datapath
        flag=0
        ofproto=datapath.ofproto

        parser=datapath.ofproto_parser
        for switch,inport,outport in shortest_path:
            match=parser.OFPMatch(in_port=inport,eth_src=src_mac,eth_dst=dst_mac)

            actions=[parser.OFPActionOutput(outport)]

            # 发现该交换机的dpid，并将dpid赋值给datapath
            for dp in self.datapaths:
                if dp.id==int(switch):
                    datapath=dp
                    flag=1
                    break
            if flag==0:
                datapath=None
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

    # 监听Packet_in事件
    @set_ev_cls(ofp_event.EventOFPPacketIn,MAIN_DISPATCHER)
    def packet_in_handler(self,event):
        msg=event.msg
        datapath=msg.datapath
        ofproto=datapath.ofproto
        parser=datapath.ofproto_parser
        in_port=msg.match['in_port']

        # 获取数据
        pkt=packet.Packet(msg.data)

        # 假设为以太帧，获取帧头
        eth=pkt.get_protocols(ethernet.ethernet)[0]

        # 丢弃LLDP帧
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

            shortest_path,path=self.topo.compute_path(
                src_switch,
                dst_switch,
                in_port,
                final_port)

            if set([path[0][0], path[-1][0]]) not in self.flag:
                draw_graph(self.topo.graph, path, self.topo.weight)
                self.flag.append(set([path[0][0], path[-1][0]]))
            
            self.logger.info("The shortest path from {} to {} contains {} switches".format(src_mac,dst_mac,len(shortest_path)))
            
            assert len(shortest_path)>0
            
            path_str=''
            for s,ip,op in shortest_path:
                path_str=path_str+"--{}-{}-{}--".format(ip,s,op)

            self.configure_path(shortest_path,event,src_mac,dst_mac)

            self.logger.info("----------------done----------------")

            out_port=None
            for s,_,op in shortest_path:
                 if s==dpid:
                    out_port=op

        else: 
            if self.arp_handler(msg):  
                return 
            out_port=ofproto.OFPP_FLOOD
        actions=[parser.OFPActionOutput(out_port)]

        data=None
        if msg.buffer_id==ofproto.OFP_NO_BUFFER:
            data=msg.data
        
        out=parser.OFPPacketOut(
            datapath=datapath,
            buffer_id=msg.buffer_id,
            in_port=in_port,
            actions=actions,
            data=data
        )
        datapath.send_msg(out)

    # 交换机进入时触发        
    @set_ev_cls(event.EventSwitchEnter)
    def switch_enter_handler(self,event):
        self.logger.info("一个交换机进入，重新发现拓扑")
        self.switch_status_handler(event)
        self.logger.info('拓扑发现完毕')

        weight = {}
        self.initshow += 1
        if self.initshow == len(self.topo.switches):
            graph = []
            for a in self.topo.switches:
                for b in self.topo.switches:
                    if (a,b) in self.topo.edges:
                        weight[(a, b)] = self.topo.edges[(a, b)][1]
                        graph.append((a, b))
            graph_path = []
            draw_graph(graph, graph_path, weight)

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

            weight=random.randint(1,5)
            self.topo.edges[(s1,s2)]=(p1,weight)
            self.topo.edges[(s2,s1)]=(p2,weight)

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
