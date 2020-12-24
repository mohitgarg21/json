import json
import jsonlines
DATA_FILE_PATH = "/home/user/Downloads/exams.json"
with jsonlines.open(DATA_FILE_PATH) as data:
    total = 497
    key_dict = {}
    for line in data:
        for i, v in line.items():
            if v and isinstance(v, list):
                for value_v in v:
                    if isinstance(value_v, dict):
                        for k_value_v, v_value_v in value_v.items():
                            if v_value_v and not isinstance(v_value_v, list) and not isinstance(v_value_v, dict):
                                key_dict[k_value_v] = key_dict.get(k_value_v, 0) + 1

    key_dict_per = {}
    for k, v in key_dict.items():
    	key_dict_per[k] = (v/total)*100
    print(key_dict, key_dict_per)