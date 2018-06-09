 # -*- coding: utf-8 -*-
from mininet.topo import Topo, LinearTopo
from mininet.topolib import TreeTopo
from mininet.net import Mininet
from mininet.node import CPULimitedHost,OVSSwitch, Controller, RemoteController
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
#from TCCSDNTopologias import ringTopology
from time import sleep
from random import choice 




def iniciaRede(net):
    net.start()
    print "Dumping host connections"
    dumpNodeConnections(net.hosts)
    listaLinks = net.links
    print "Listando Links"
    for j in listaLinks:
    	print j
    print "Testando conexão da Rede"
    net.pingAll()
    
def iperfTeste (net, hostCLi, hostServ ): 
    print "Testando Largura de Banda entre " + str(hostCLi) + " e " + str(hostServ)
    net.iperf((hostCLi, hostServ))

if __name__ == '__main__':
    topo = LinearTopo(k=5, n=2) # k numero de switch e n numero de hosts por switch
    #topo = TreeTopo(depth=5)
    #topo = ringTopology(10) 
    net = Mininet(topo=topo,controller = RemoteController( 'c0', ip='192.168.25.15', port=6633 ))
    setLogLevel('info')
    iniciaRede(net)
    listaHosts = net.hosts

    while 1: 
        sleep(2);
        host1 = choice(listaHosts);
        while 1:
            host2 = choice(listaHosts);
            if host1 != host2:
                break
        iperfTeste(net, host1, host2)     

    #iperfTeste(net,'h1' , 'h2')  



