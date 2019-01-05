# -*- coding: utf-8 -*-

from time import sleep
from pythonosc import udp_client
from pythonosc.osc_message_builder import OscMessageBuilder

IP = '127.0.0.1'
OSCPORT = 9000

def send(address, osc_arg):
    client = udp_client.UDPClient(IP, OSCPORT)
    message = OscMessageBuilder(address=address)
    message.add_arg(osc_arg)
    m = message.build()
    client.send(m)

    return address + ' ' + str(osc_arg)


if __name__ == "__main__":
    address = '/cube/activate'
    arg = 1
    print(send(address, arg))
    sleep(3)
    arg = 0
    print(send(address, arg))