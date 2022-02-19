# -*- coding: utf-8 -*-
import re
import trigger_data
from utility import *

triggers = [
    {
        'address': '/cube/activate',
        'キューブ アクティブ': 1,
        'キューブ オフ': 0
    },
    {
        'address': '/magicparticle/activate',
        '詠唱 開始': 1,
        '詠唱 終了': 0
    },
    {
        'address': '/light/activate',
        '電気 つけて': 1,
        '電気 消して': 0
    }
]


def convert_key_val_to_integer(key_value):
    if key_value == 'OnTrigerKey':
        return 1
    elif key_value == 'OffTriggerKey':
        return 0
    else:
        return -1


def is_auto_off(trigger):
    if trigger['OffTriggerKey'] == 'AutoOff':
        return True
    return False


# トリガーキーと入力文字をパターンマッチさせる
def select(input_text):
    #global triggers
    data = trigger_data.data_in_current_world
    type_str = 'type'
    if type_str in data and data[type_str] == 'Avatar':
        return select_avatar(input_text)
    else:
        return select_world(input_text)


def select_world(input_text):
    address = ''
    auto_off = False

    for trigger_tmp in trigger_data.data_in_current_world['OSCButtonTrigers']:
        trigger = dict(trigger_tmp)
        address = trigger.pop('address')

        for (key_val, triger_key) in trigger.items():
            pattern = r'^'
            key_parts = triger_key.split(' ')

            # 正規表現の作成
            for p in key_parts:
                pattern += r'(?=.*{0})'.format(p)
            pattern += r'.*$'
            # print(pattern)

            # パターンマッチ
            m = re.search(pattern, input_text)

            if m:
                value = convert_key_val_to_integer(key_val)
                # OnTriggerKeyならAutoOffか確認
                if value == 1 and is_auto_off(trigger):
                    auto_off = True
                    return (address, value, auto_off)
                return (address, value, auto_off)
    # [loop END]
    return ('', -1, auto_off)


def select_avatar(input_text):
    address = ''

    for trigger_tmp in trigger_data.data_in_current_world['OSCButtonTrigers']:
        trigger = dict(trigger_tmp)
        address = trigger.pop('address')
        if trigger.pop('type') != 'int':
            continue
        trigger_keys = trigger.pop('changeTriggerKeys')

        for index, trigger_key in enumerate(trigger_keys):
            pattern = r'^'
            key_parts = trigger_key.split(' ')

            # 正規表現の作成
            for p in key_parts:
                pattern += r'(?=.*{0})'.format(p)
            pattern += r'.*$'
            # print(pattern)

            # パターンマッチ
            m = re.search(pattern, input_text)

            if m:
                return (address, index, False)
    # [loop END]
    return ('', -1, False)


# 単体テスト用
if __name__ == "__main__":
    texts = [
        'キューブ アクティブ',
        'キューブ オフ',
        'あのキューブをアクティブにして！',
        'キューブをオフにしてよ',
        'キューブだ！',
        'あれオフやんけ',
        'こやこや〜',
        '詠唱開始！',
        '詠唱終了だ！よくやった',
        '電気つけてよ',
        '電気を消してってば！',
    ]

    setup()

    for txt in texts:
        print(select(txt))
        # print(trigger_data.data_in_current_world)
