# -*- coding: utf-8 -*-

import os
import json
import trigger_settings_loader
import trigger_data

# for mac or linux
# PATH = './TriggerSettings'
# F_PATH = PATH + '/VoiceTriggerTesting.json'
# for windows
PATH = '.¥¥TriggerSettings'
F_PATH = PATH + '¥¥VoiceTriggerTesting.json'


def createJSON(jdic):
    return json.dumps(jdic)


def check_dir():
    if not os.path.exists(PATH):
        os.mkdir(PATH)

        with open(F_PATH, mode='w') as f:
            f.write(trigger_data.test_world_data)


def setup():
    trigger_settings_loader.load()
    world_list = trigger_settings_loader.get_world_names()

    dic = {'Status': 'Socket OK!', 'Mode': 'init'}
    dic['Message'] = world_list

    return createJSON(dic)


def change_current_world(selected_world):
    for world in trigger_data.data_in_all_world:
        world_name = world['WorldName']

        if world_name == selected_world:
            trigger_data.data_in_current_world = world
            break
    #[END of loop]
    print(trigger_data.data_in_current_world['WorldName'])


# Unit test
if __name__ == "__main__":
    check_dir()