# -*- coding: utf-8 -*-

import json
 
def encodeJson(keys, values):
    dict_data = {}
    for i in range (len(keys)):
        dict_data[keys[i]] = values[i]

    return json.dumps(dict_data)

