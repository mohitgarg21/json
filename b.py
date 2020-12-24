import json
import jsonlines
DATA_FILE_PATH = "/home/user/Downloads/exams.json"
with jsonlines.open(DATA_FILE_PATH) as data:
    total = 497
    key_dict = {}
    for line in data:
        line_keys = []
        for i, v in line.items():
            if i == 'subexams':
                for sub_exam_dict in v:
                    for sub_exam_k, sub_exam_v in sub_exam_dict.items():
                        if sub_exam_k == 'instances':
                            for instance_dict in sub_exam_v:
                                for instance_k, instance_v in instance_dict.items():
                                    if instance_v and instance_k not in line_keys:
                                        line_keys.append(instance_k)
                                        key_dict[instance_k] = key_dict.get(instance_k, 0) + 1

    key_dict_per = {}
    for k, v in key_dict.items():
    	key_dict_per[k] = (v/total)*100
    print(key_dict, key_dict_per)