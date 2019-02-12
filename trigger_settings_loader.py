# -*- coding: utf-8 -*-

import glob
import json
import pprint
import trigger_data

PATH = 'TriggerSettings/*.json'


# TriggerSettingsのファイル一覧を取得
def listup_setting_files():
    return glob.glob(PATH)


# それぞれのファイルを読み込み、文字列→json→辞書に変換し、1つのリストを作成
def load():
    files = listup_setting_files()

    for file in files:
        json_str = ''
        buffar = None
        with open(file, 'r') as f:
            buffar = f.readlines()
        
        for line in buffar:
            json_str += line
        
        json_dic = json.loads(json_str)
        trigger_data.data_in_all_world.append(json_dic)
    #[END of loop]

    # 現在のワールド設定にリストの先頭のワールドを設定
    trigger_data.data_in_current_world = trigger_data.data_in_all_world[0]


# jsonリストからワールド名をパースし、ワールドリストを作成して返す
def get_world_names():
    world_list = []

    for jdic in trigger_data.data_in_all_world: 
        world = jdic.get('WorldName')
        world_list.append(world)
    
    return world_list


# Unit Test
if __name__ == "__main__":
    files = listup_setting_files()
    for f in files:
        print(f)
    
    load()
    pprint.pprint(trigger_data.data_in_all_world)
    pprint.pprint(trigger_data.data_in_current_world)

    print(get_world_names())