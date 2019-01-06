# -*- coding: utf-8 -*-
import re

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

# トリガーキーと入力文字をパターンマッチさせる
def select(input_text):
    global triggers
    address = ''

    for trigger in triggers:
        for k in trigger.keys():
            if k is 'address':
                address = trigger.get(k)
                continue
            
            pattern = r'^'
            key_parts = k.split(' ')

            # 正規表現の作成
            for p in key_parts:
                pattern += r'(?=.*{0})'.format(p)
            pattern += r'.*$'
            print(pattern)

            # パターンマッチ
            m = re.search(pattern, input_text)

            if m:
                return (address, trigger.get(k))
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
        '詠唱終了だ！よくやった'
    ]

    for txt in texts:
        print(select(txt))