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
                    for k_value_v, v_value_v in sub_exam_dict.items():
                        if k_value_v == 'instances':
                            for instance_dict in v_value_v:
                                for k_value_v1, v_value_v1 in instance_dict.items():
                                    if k_value_v1 == 'syllabus':
                                        for event_dict in v_value_v1:
                                            for k_value_v2, v_value_v2 in event_dict.items():
                                                if v_value_v2 and k_value_v2 not in line_keys:
                                                    line_keys.append(k_value_v2)
                                                    key_dict[k_value_v2] = key_dict.get(k_value_v2, 0) + 1

    key_dict_per = {}
    for k, v in key_dict.items():
    	key_dict_per[k] = (v/total)*100
    print(key_dict, key_dict_per)