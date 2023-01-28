#!/usr/bin/python
import sys
from mininet.node import Controller
from mininet.log import setLogLevel, info
from mn_wifi.cli import CLI_wifi
from mn_wifi.net import Mininet_wifi

def topology(plot):
    "Create a network."
    net = Mininet_wifi(controller=Controller)

    info("*** Creating nodes\n")
    #TODO: Task1
    sta1 = net.addStation('sta1', mac='00:00:00:00:00:02', ip='10.0.0.2/8', position='30,40,0', band='5', range= 20, encrypt='wpa2', failMode='standalone', passwd= '19061006', min_v=1, max_v=5)
    sta2 = net.addStation('sta2', mac='00:00:00:00:00:03', ip='10.0.0.3/8', position='30,40,0', band='5', range= 20, encrypt='wpa2', failMode='standalone', passwd= '19061006', min_v=5, max_v=10)
    sta3 = net.addStation('sta3', mac='00:00:00:00:00:04', ip='10.0.0.4/8', position='30,40,0', band='5', range= 20, encrypt='wpa2', failMode='standalone', passwd= '19061006', min_v=2, max_v=7)
    sta4 = net.addStation('sta4', mac='00:00:00:00:00:05', ip='10.0.0.5/8', position='30,40,0', band='5', range= 20, encrypt='wpa2', failMode='standalone', passwd= '19061006', min_v=2, max_v=7)
    
    ap1 = net.addAccessPoint('ap1', mac ='00:00:00:00:10:02', ssid='ap1', mode='g', channel='1', position='50,50,0', band='5', range= 25, encrypt='wpa2', failMode='standalone', passwd= '19061006')
    ap2 = net.addAccessPoint('ap2', mac ='00:00:00:00:10:03', ssid='ap2', mode='g', channel='6', position='100,50,0', band='5', range= 25, encrypt='wpa2', failMode='standalone', passwd= '19061006')
    ap3 = net.addAccessPoint('ap3', mac ='00:00:00:00:10:04', ssid='ap3', mode='g', channel='2', position='150,50,0', band='5', range= 25, encrypt='wpa2', failMode='standalone', passwd= '19061006')
    ap4 = net.addAccessPoint('ap4', mac ='00:00:00:00:10:05', ssid='ap4', mode='g', channel='3', position='150,90,0', band='5', range= 25, encrypt='wpa2', failMode='standalone', passwd= '19061006')


    c1 = net.addController('c1')

    net.setPropagationModel(model="logDistance", exp=5)

    info("*** Configuring wifi nodes\n")
    net.configureWifiNodes()

    info("*** Creating links\n")
    #TODO: Task2
    net.addLink(ap1, ap2)
    net.addLink(ap2, ap3)
    net.addLink(ap3, ap4)
 
    #TODO: Task3
    net.plotGraph(min_x=0, min_y=0, max_x=200, max_y=200)
    net.startMobility(time=0)
    net.mobility(sta1, 'start', time=10, position='30,40,0')
    net.mobility(sta1, 'stop', time=20, position='100,40,0')
    net.mobility(sta2, 'start', time=15, position='30,40,0')
    net.mobility(sta2, 'stop', time=21, position='150,60,0')
    net.mobility(sta3, 'start', time=16, position='30,40,0')
    net.mobility(sta3, 'stop', time=22, position='150,100,0')
    net.mobility(sta4, 'start', time=3, position='30,40,0')
    net.mobility(sta4, 'stop', time=10, position='50,100,0')
    net.stopMobility(time=30)
    
    info("*** Starting network\n")
    net.build()
    c1.start()

    #TODO: Task4
    ap1.start([c1])
    ap2.start([c1])
    ap3.start([c1])
    ap4.start([c1])
    

    info("*** Running CLI\n")
    CLI_wifi(net)

    info("*** Stopping network\n")
    net.stop()
    

if __name__ == '__main__':
    setLogLevel('info')
    plot = False if '-p' in sys.argv else True
    topology(plot)
