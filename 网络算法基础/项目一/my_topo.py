#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call

def myNetwork():

    net = Mininet( topo=None,
                   build=False,
                   ipBase='10.0.0.0/8')

    info( '*** Adding controller\n' )
    c0=net.addController(name='c0',
                      controller=RemoteController,
                      ip='127.0.0.1',
                      protocol='tcp',
                      port=6633)

    info( '*** Add switches\n')
    s19 = net.addSwitch('s19', cls=OVSKernelSwitch,protocols=['OpenFlow13'])
    s3 = net.addSwitch('s3', cls=OVSKernelSwitch,protocols=['OpenFlow13'])
    s6 = net.addSwitch('s6', cls=OVSKernelSwitch,protocols=['OpenFlow13'])
    s7 = net.addSwitch('s7', cls=OVSKernelSwitch,protocols=['OpenFlow13'])
    s4 = net.addSwitch('s4', cls=OVSKernelSwitch,protocols=['OpenFlow13'])
    s20 = net.addSwitch('s20', cls=OVSKernelSwitch,protocols=['OpenFlow13'])
    s16 = net.addSwitch('s16', cls=OVSKernelSwitch,protocols=['OpenFlow13'])
    s11 = net.addSwitch('s11', cls=OVSKernelSwitch,protocols=['OpenFlow13'])
    s1 = net.addSwitch('s1', cls=OVSKernelSwitch,protocols=['OpenFlow13'])
    s8 = net.addSwitch('s8', cls=OVSKernelSwitch, protocols=['OpenFlow13'])
    s12 = net.addSwitch('s12', cls=OVSKernelSwitch,protocols=['OpenFlow13'])
    s17 = net.addSwitch('s17', cls=OVSKernelSwitch,protocols=['OpenFlow13'])
    s14 = net.addSwitch('s14', cls=OVSKernelSwitch,protocols=['OpenFlow13'])
    s5 = net.addSwitch('s5', cls=OVSKernelSwitch,protocols=['OpenFlow13'])
    s9 = net.addSwitch('s9', cls=OVSKernelSwitch,protocols=['OpenFlow13'])
    s10 = net.addSwitch('s10', cls=OVSKernelSwitch,protocols=['OpenFlow13'])
    s18 = net.addSwitch('s18', cls=OVSKernelSwitch,protocols=['OpenFlow13'])
    s13 = net.addSwitch('s13', cls=OVSKernelSwitch,protocols=['OpenFlow13'])
    s2 = net.addSwitch('s2', cls=OVSKernelSwitch,protocols=['OpenFlow13'])
    s15 = net.addSwitch('s15', cls=OVSKernelSwitch,protocols=['OpenFlow13'])

    info( '*** Add hosts\n')
    h4 = net.addHost('h4', cls=Host, ip='10.0.0.4', defaultRoute=None,mac='00:00:00:00:00:04')
    h1 = net.addHost('h1', cls=Host, ip='10.0.0.1', defaultRoute=None,mac='00:00:00:00:00:01')
    h17 = net.addHost('h17', cls=Host, ip='10.0.0.17', defaultRoute=None,mac='00:00:00:00:00:17')
    h19 = net.addHost('h19', cls=Host, ip='10.0.0.19', defaultRoute=None,mac='00:00:00:00:00:19')
    h12 = net.addHost('h12', cls=Host, ip='10.0.0.12', defaultRoute=None,mac='00:00:00:00:00:12')
    h14 = net.addHost('h14', cls=Host, ip='10.0.0.14', defaultRoute=None,mac='00:00:00:00:00:14')
    h5 = net.addHost('h5', cls=Host, ip='10.0.0.5', defaultRoute=None,mac='00:00:00:00:00:05')
    h20 = net.addHost('h20', cls=Host, ip='10.0.0.20', defaultRoute=None,mac='00:00:00:00:00:20')
    h6 = net.addHost('h6', cls=Host, ip='10.0.0.6', defaultRoute=None,mac='00:00:00:00:00:06')
    h8 = net.addHost('h8', cls=Host, ip='10.0.0.8', defaultRoute=None,mac='00:00:00:00:00:08')
    h15 = net.addHost('h15', cls=Host, ip='10.0.0.15', defaultRoute=None,mac='00:00:00:00:00:15')
    h3 = net.addHost('h3', cls=Host, ip='10.0.0.3', defaultRoute=None,mac='00:00:00:00:00:03')
    h9 = net.addHost('h9', cls=Host, ip='10.0.0.9', defaultRoute=None,mac='00:00:00:00:00:09')
    h10 = net.addHost('h10', cls=Host, ip='10.0.0.10', defaultRoute=None,mac='00:00:00:00:00:10')
    h16 = net.addHost('h16', cls=Host, ip='10.0.0.16', defaultRoute=None,mac='00:00:00:00:00:16')
    h13 = net.addHost('h13', cls=Host, ip='10.0.0.13', defaultRoute=None,mac='00:00:00:00:00:13')
    h7 = net.addHost('h7', cls=Host, ip='10.0.0.7', defaultRoute=None,mac='00:00:00:00:00:07')
    h11 = net.addHost('h11', cls=Host, ip='10.0.0.11', defaultRoute=None,mac='00:00:00:00:00:11')
    h2 = net.addHost('h2', cls=Host, ip='10.0.0.2', defaultRoute=None,mac='00:00:00:00:00:02')
    h18 = net.addHost('h18', cls=Host, ip='10.0.0.18', defaultRoute=None,mac='00:00:00:00:00:18')

    info( '*** Add links\n')
    net.addLink(s1, s2)
    net.addLink(s1, s4)
    net.addLink(s2, s4)
    net.addLink(s2, s3)
    net.addLink(s3, s10)
    net.addLink(s10, s4)
    net.addLink(s4, s5)
    net.addLink(s5, s9)
    net.addLink(s5, s6)
    net.addLink(s5, s7)
    net.addLink(s6, s8)
    net.addLink(s8, s7)
    net.addLink(s10, s11)
    net.addLink(s11, s12)
    net.addLink(s13, s10)
    net.addLink(s15, s20)
    net.addLink(s14, s15)
    net.addLink(s12, s15)
    net.addLink(s14, s8)
    net.addLink(s12, s17)
    net.addLink(s13, s16)
    net.addLink(s16, s12)
    net.addLink(s16, s18)
    net.addLink(s13, s19)
    net.addLink(h1, s1)
    net.addLink(h2, s2)
    net.addLink(h3, s3)
    net.addLink(h19, s19)
    net.addLink(h13, s13)
    net.addLink(h18, s18)
    net.addLink(h16, s12)
    net.addLink(h17, s17)
    net.addLink(h12, s12)
    net.addLink(h15, s15)
    net.addLink(h14, s14)
    net.addLink(h8, s8)
    net.addLink(h20, s20)
    net.addLink(h7, s7)
    net.addLink(h11, s11)
    net.addLink(h6, s6)
    net.addLink(h5, s5)
    net.addLink(h9, s9)
    net.addLink(h4, s4)
    net.addLink(h10, s10)

    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches\n')
    net.get('s19').start([c0])
    net.get('s3').start([c0])
    net.get('s6').start([c0])
    net.get('s7').start([c0])
    net.get('s4').start([c0])
    net.get('s20').start([c0])
    net.get('s16').start([c0])
    net.get('s11').start([c0])
    net.get('s1').start([c0])
    net.get('s8').start([c0])
    net.get('s12').start([c0])
    net.get('s17').start([c0])
    net.get('s14').start([c0])
    net.get('s5').start([c0])
    net.get('s9').start([c0])
    net.get('s10').start([c0])
    net.get('s18').start([c0])
    net.get('s13').start([c0])
    net.get('s2').start([c0])
    net.get('s15').start([c0])

    info( '*** Post configure switches and hosts\n')

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()

