#!/user/bin/python
from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.log import setLogLevel, info
from mininet.node import OVSKernelSwitch, RemoteController

def myNetwork():
    net = Mininet(topo = None, build=False)
    info('***Adding Controller\n')
    net.addController(name='c0',controller=RemoteController,ip='192.168.0.222',port=6633)

    info('***Adding Switch\n')
    s1 = net.addSwitch('s1', protocols="OpenFlow13" )

    info('*** Add hosts \n')
    h1 = net.addHost('h1')
    h2 = net.addHost('h2')

    info('*** Add links with Qos Params \n')
    net.addLink(h1, s1, cls=TCLink, bw=3, delay='1ms')
    net.addLink(h2, s1, cls=TCLink, bw=3, delay='1ms')

    info('***Starting Network \n')
    net.start()
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    myNetwork()
