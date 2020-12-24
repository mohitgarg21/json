import json
import jsonlines
DATA_FILE_PATH = "/home/user/Downloads/exams.json"
with jsonlines.open(DATA_FILE_PATH) as data:
    total = 497
    key_dict = {}
    for line in data:
        line_keys = []
        for i, v in line.items():
            if i == 'instances':
                for instances_dict in v:
                    for instances_k, instances_v in instances_dict.items():
                        if instances_v and instances_k not in line_keys:
                            line_keys.append(instances_k)
                            key_dict[instances_k] = key_dict.get(instances_k, 0) + 1

    key_dict_per = {}
    for k, v in key_dict.items():
    	key_dict_per[k] = (v/total)*100
    print(key_dict, key_dict_per)