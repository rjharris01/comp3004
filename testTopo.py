#!/user/bin/python
from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.log import setLogLevel, info
from mininet.node import OVSKernelSwitch, RemoteController

def myNetwork():
    net = Mininet(topo=None,build=False)
    info('***Adding Controlle\n')
    net.addController(name='c0',controller=RemoteController,ip='192.168.0.222',port=6633)

    info('***Adding Switch\n')
    s1 = net.addSwitch('s1')

    info('*** Add hosts \n')
    h1 = net.addHost('h1',csl=Host, ip='10.0.0.1', defaultRoute=None)
    h2 = net.addHost('h2',csl=Host, ip='10.0.0.2', defaultRoute=None)

    info('*** Add links with Qos Params \n')
    net.addLink(h1, s1, cls=TCLink, bw=100, delay='1ms', loss = 0)
    net.addLink(h2, s1, cls=TCLink, bw=100, delay='1ms', loss = 0)

    info('***Starting Network \n')
    net.start()
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    myNetwork()
