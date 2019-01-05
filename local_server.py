# -*- coding: utf-8 -*-

import logging
import json
from websocket_server import WebsocketServer

import trigger_selector
import osc_sender

IP = '127.0.0.1'
WSPORT = 12345

# ログ出力の設定
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter(' %(module)s -  %(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

# Callback functions
def new_client(client, server):
    logger.info('New client {}:{} has joined.'.format(client['address'][0], client['address'][1]))

def client_left(client, server):
    logger.info('Client {}:{} has left.'.format(client['address'][0], client['address'][1]))

def message_received(client, server, message):
    logger.info('Message "{}" has been received from {}:{}'.format(message, client['address'][0], client['address'][1]))

    # 受け取ったJSONをパース(返り値はdict)
    json_data = json.loads(message)

    if json_data['Mode'] == 'speech':
        reply_message = 'Socket OK!'
        server.send_message(client, reply_message)
        logger.info('Message "{}" has been sent to {}:{}'.format(reply_message, client['address'][0], client['address'][1]))
        # debug
        print(json_data['Message'])

        # トリガーメッセージと入力がマッチしていればVRCへOSCメッセージを送信
        (address, value) = trigger_selector.select(json_data['Message'])
        if not value is -1:
            logger.info('Triger selected! Send Message is {} {}.'.format(address, str(value)))
            osc_msg = osc_sender.send(address, value)
            logger.info('OSC Message "{}" has been sent to VRChat client'.format(osc_msg))


if __name__ == "__main__":
    server = WebsocketServer(port=WSPORT, host=IP, loglevel=logging.INFO)
    server.set_fn_new_client(new_client)
    server.set_fn_client_left(client_left)
    server.set_fn_message_received(message_received)
    server.run_forever()