from mininet. topo import Topo 

class MyTopology (Topo):
    def __init__(self):
        Topo.init_ (self)

        # Add switches
        s1 = self. addSwitch('s1')
        s2 = self.addSwitch('s2')

        # Add hosts
        h1 = self. addHost ('h1')
        h2 = self. addHost ('h2')
        h3 = self. addHost ('h3')

        # Add links
        self.addLink(h1,s1)
        self.addLink(h2,s2)
        self.addLink(h3,s2)
        self.addLink(s1,s2)


topos = {'mytopology': (lambda: MyTopology ())}