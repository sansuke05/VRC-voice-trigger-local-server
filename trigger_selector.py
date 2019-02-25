# -*- coding: utf-8 -*-
import re
import trigger_data
from utility import *

triggers = [
    { 
        'address': '/cube/activate',
        'キューブ アクティブ':1,
        'キューブ オフ':0 
    },
    { 
        'address': '/magicparticle/activate',
        '詠唱 開始':1,
        '詠唱 終了':0
    },
    {
        'address': '/light/activate',
        '電気 つけて':1,
        '電気 消して':0
    }
]


def convert_key_val_to_integer(key_value):
    if key_value == 'OnTrigerKey':
        return 1
    elif key_value == 'OffTriggerKey':
        return 0
    else:
        return -1


# トリガーキーと入力文字をパターンマッチさせる
def select(input_text):
    #global triggers
    address = ''

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
            #print(pattern)

            # パターンマッチ
            m = re.search(pattern, input_text)

            if m:
                value = convert_key_val_to_integer(key_val)
                return (address, value)
    #[loop END]
    return ('', -1)


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
        #print(trigger_data.data_in_current_world)