# -*- coding: utf-8 -*-

import glob
import json
import pprint

PATH = 'TriggerSettings/*.json'


# TriggerSettingsのファイル一覧を取得
def listup_setting_files():
    return glob.glob(PATH)


# それぞれのファイルを読み込み、文字列→json→辞書に変換し、1つのリストを作成
def load():
    json_dicts = []
    files = listup_setting_files()

    for file in files:
        json_str = ''
        buffar = None
        with open(file, 'r') as f:
            buffar = f.readlines()
        
        for line in buffar:
            json_str += line
        
        json_dic = json.loads(json_str)
        json_dicts.append(json_dic)
    #[END of loop]

    return json_dicts


# jsonリストからワールド名をパースし、ワールドリストを作成して返す
def get_world_names(jsons):
    pass


# Unit Test
if __name__ == "__main__":
    files = listup_setting_files()
    for f in files:
        print(f)
    
    l = load()
    pprint.pprint(l)