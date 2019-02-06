# -*- coding: utf-8 -*-

import glob

PATH = 'TriggerSettings/*.json'


# TriggerSettingsのファイル一覧を取得
def listup_setting_files():
    return glob.glob(PATH)


def load():
    files = listup_setting_files()

    # それぞれのファイルを読み込み、文字列→json→辞書に変換し、1つのリストを作成
    for f in files:
        