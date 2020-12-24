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
                for subexam_dict in v:
                    for subexam_k, subexam_v in subexam_dict.items():
                        if subexam_k == 'instances':
                            for instance_dict in subexam_v:
                                for instance_k, instance_v in instance_dict.items():
                                    if instance_k == 'syllabus':
                                        for syllabus_dict in instance_v:
                                            for syllabus_k, syllabus_v in syllabus_dict.items():
                                                if syllabus_v and syllabus_k not in line_keys:
                                                    line_keys.append(syllabus_k)
                                                    key_dict[syllabus_k] = key_dict.get(syllabus_k, 0) + 1
            if i == 'instances':
                for instance_dict in v:
                    for instance_k, instance_v in instance_dict.items():
                        if instance_k == 'syllabus':
                            for syllabus_dict in instance_v:
                                for syllabus_k, syllabus_v in syllabus_dict.items():
                                    if syllabus_v and syllabus_k not in line_keys:
                                        line_keys.append(syllabus_k)
                                        key_dict[syllabus_k] = key_dict.get(syllabus_k, 0) + 1
    key_dict_per = {}
    for k, v in key_dict.items():
       key_dict_per[k] = (v/total)*100
    print(key_dict, key_dict_per)