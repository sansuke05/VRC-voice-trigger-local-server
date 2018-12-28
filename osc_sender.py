# -*- coding: utf-8 -*-

from pythonosc import udp_client
from pythonosc.osc_message_builder import OscMessageBuilder

IP = '127.0.0.1'
OSCPORT = 9000
ADDRESS = '/cube/active'

def send(osc_arg):
    client = udp_client.UDPClient(IP, OSCPORT)
    message = OscMessageBuilder(address=ADDRESS)
    message.add_arg(osc_arg)
    m = message.build()
    client.send(m)

    return ADDRESS + ' ' + str(osc_arg)


if __name__ == "__main__":
    arg = 1
    print(send(arg))
    arg = 0
    print(send(arg))