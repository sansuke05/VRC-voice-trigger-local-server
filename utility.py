# -*- coding: utf-8 -*-

import json
import trigger_settings_loader
import trigger_data


def createJSON(jdic):
    return json.dumps(jdic)


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