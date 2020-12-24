import json
import jsonlines
DATA_FILE_PATH = "/home/user/Downloads/exams.json"
with jsonlines.open(DATA_FILE_PATH) as data:
    total = 497
    key_dict = {}
    line_keys = []
    for line in data:
    	for i, v in line.items():
    		if v:
    		    key_dict[i] = key_dict.get(i, 0) + 1

    key_dict_per = {}
    for k, v in key_dict.items():
    	key_dict_per[k] = (v/total)*100
    print(key_dict, key_dict_per)