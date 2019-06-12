from mininet.topo import SingleSwitchTopo
from mininet.net import Mininet
from mininet.cli import CLI

def mycmd( self, line ):
    "mycmd is an example command to extend the Mininet CLI"
    net = self.mn
    print( 'mycmd invoked for', net, 'with line', line, '\n')
CLI.do_mycmd = mycmd

net = Mininet(SingleSwitchTopo(2))
net.start()
CLI(net)
net.stop()
