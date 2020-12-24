import json
import jsonlines
DATA_FILE_PATH = "/home/user/Downloads/exams.json"
with jsonlines.open(DATA_FILE_PATH) as data:
    total = 497
    key_dict = {}
    for line in data:
        line_keys = []
        for i, v in line.items():
            if i == 'cutoffUrlsOfficial':
                for value_v in v:
                    for cutOffUrl_k, cutOffUrl_v in value_v.items():
                        if cutOffUrl_v and cutOffUrl_k not in line_keys:
                            line_keys.append(cutOffUrl_k)
                            key_dict[cutOffUrl_k] = key_dict.get(cutOffUrl_k, 0) + 1

    key_dict_per = {}
    for k, v in key_dict.items():
    	key_dict_per[k] = (v/total)*100
    print(key_dict, key_dict_per)