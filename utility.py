# -*- coding: utf-8 -*-

import json
import trigger_settings_loader


def createJSON(jdic):
    return json.dumps(jdic)


def setup():
    trigger_settings_loader.load()
    world_list = trigger_settings_loader.get_world_names()

    dic = {'Status': 'Socket OK!', 'Mode': 'init'}
    dic['Message'] = world_list

    return createJSON(dic)