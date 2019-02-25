# -*- coding: utf-8 -*-

data_in_all_world = []

data_in_current_world = dict()

test_world_data = '''{
    "WorldName" : "VoiceTriggerTesting",
    "OSCButtonTrigers": [
        {
            "address": "/cube/activate",
            "OnTrigerKey": "キューブ アクティブ",
            "OffTriggerKey": "キューブ オフ"
        },
        {
            "address": "/magicparticle/activate",
            "OnTrigerKey": "詠唱 開始",
            "OffTriggerKey": "詠唱 終了"
        },
        {
            "address": "/light/activate",
            "OnTrigerKey": "電気 つけて",
            "OffTriggerKey": "電気 消して"
        }
    ]
}
'''