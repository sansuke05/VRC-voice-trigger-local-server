# -*- coding: utf-8 -*-

import logging
from time import sleep
import json
import webbrowser
from websocket_server import WebsocketServer

import trigger_selector
import osc_sender
from utility import *

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
    pass
    #logger.info('New client {}:{} has joined.'.format(client['address'][0], client['address'][1]))

def client_left(client, server):
    pass
    #logger.info('Client {}:{} has left.'.format(client['address'][0], client['address'][1]))

def message_received(client, server, message):
    #logger.info('Message "{}" has been received from {}:{}'.format(message, client['address'][0], client['address'][1]))

    # 受け取ったJSONをパース(返り値はdict)
    json_data = json.loads(message)

    if json_data['Mode'] == 'speech':
        reply_json_msg = '{"Status": "Socket OK!", "Mode": "speech"}'
        server.send_message(client, reply_json_msg)
        #logger.info('Message "{}" has been sent to {}:{}'.format(reply_json_msg, client['address'][0], client['address'][1]))
        # debug
        #print(json_data['Message'])

        # トリガーメッセージと入力がマッチしていればVRCへOSCメッセージを送信
        (address, value, auto_off) = trigger_selector.select(json_data['Message'])
        if value != -1:
            #logger.info('Triger selected! Send Message is {} {}.'.format(address, str(value)))
            osc_msg = osc_sender.send(address, value)
            logger.info('OSC Message "{}" has been sent to VRChat client'.format(osc_msg))

            # オートオフ設定なら1秒後にoffメッセージを送信
            if auto_off:
                sleep(1)
                osc_msg = osc_sender.send(address, 0)
                logger.info('[Auto Off]OSC Message "{}" has been sent to VRChat client'.format(osc_msg))

    elif json_data['Mode'] == 'init':
        reply_json_msg = setup()
        server.send_message(client, reply_json_msg)
        #logger.info('Message "{}" has been sent to {}:{}'.format(reply_json_msg, client['address'][0], client['address'][1]))

    elif json_data['Mode'] == 'chworld':
        change_current_world(json_data['Message'])
        reply_json_msg = '{"Status": "Socket OK!", "Mode": "chworld"}'
        server.send_message(client, reply_json_msg)
        #logger.info('Message "{}" has been sent to {}:{}'.format(reply_json_msg, client['address'][0], client['address'][1]))


if __name__ == "__main__":
    check_dir()

    # ブラウザの起動
    url = 'https://sansuke05.github.io/VRC-voice-trigger-web/'
    webbrowser.open(url)

    # サーバーの起動
    server = WebsocketServer(port=WSPORT, host=IP, loglevel=logging.INFO)
    server.set_fn_new_client(new_client)
    server.set_fn_client_left(client_left)
    server.set_fn_message_received(message_received)
    server.run_forever()