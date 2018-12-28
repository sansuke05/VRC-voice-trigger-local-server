# -*- coding: utf-8 -*-
import re

triggers = { 'キューブ アクティブ':1, 'キューブ オフ':0 }

# トリガーキーと入力文字をパターンマッチさせる
def select(input_text):
    global triggers

    for k in triggers.keys():
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
            return triggers.get(k)
    #[loop END]
    return -1


# 単体テスト用
if __name__ == "__main__":
    texts = [
        'キューブ アクティブ',
        'キューブ オフ',
        'あのキューブをアクティブにして！',
        'キューブをオフにしてよ',
        'キューブだ！',
        'あれオフやんけ',
        'こやこや〜'
    ]

    for txt in texts:
        print(select(txt))