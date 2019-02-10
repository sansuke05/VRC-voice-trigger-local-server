# -*- coding: utf-8 -*-

import glob
import json
import pprint

PATH = 'TriggerSettings/*.json'

json_dicts = []


# TriggerSettingsのファイル一覧を取得
def listup_setting_files():
    return glob.glob(PATH)


# それぞれのファイルを読み込み、文字列→json→辞書に変換し、1つのリストを作成
def load():
    global json_dicts
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


# jsonリストからワールド名をパースし、ワールドリストを作成して返す
def get_world_names():
    global json_dicts
    world_list = []

    for jdic in json_dicts: 
        world = jdic.get('WorldName')
        world_list.append(world)
    
    return world_list

# ファイルロード、ワールドリストの作成
def setup():
    load()
    return get_world_names()


# Unit Test
if __name__ == "__main__":
    files = listup_setting_files()
    for f in files:
        print(f)
    
    load()
    pprint.pprint(json_dicts)

    print(get_world_names())