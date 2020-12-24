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
                            for instances_dict in sub_exam_v:
                                for instances_k, instances_v in instances_dict.items():
                                    if instances_k == 'syllabus':
                                        for syllabus_dict in instances_v:
                                            for syllabus_k, syllabus_v in syllabus_dict.items():
                                                if syllabus_k == 'subSubjects':
                                                    for subSubjects_dict in syllabus_v:
                                                        for subSubject_k, subSubject_v in subSubjects_dict.items():
                                                            if subSubject_k == 'subSubjects':
                                                                for subSubjects1_dict in subSubject_v:
                                                                    for subSubject_k1, subSubject_v1 in subSubjects1_dict.items():
                                                                        if subSubject_v1 and subSubject_k1 not in line_keys:
                                                                            line_keys.append(subSubject_k1)
                                                                            key_dict[subSubject_k1] = key_dict.get(subSubject_k1, 0) + 1

    if i == 'instances':
        for instances_dict in v:
            for instances_k, instances_v in instances_dict.items():
                if instances_k == 'syllabus':
                    for syllabus_dict in instances_v:
                        for syllabus_k, syllabus_v in syllabus_dict.items():
                            if syllabus_k == 'subSubjects':
                                for subSubjects_dict in syllabus_v:
                                    for subSubjects_k, subSubjects_v in subSubjects_dict.items():
                                        if subSubjects_k == 'subSubjects':
                                            for subSubjects1_dict in subSubjects_v:
                                                for subSubjects_k1, subSubjects_v1 in subSubjects1_dict.items():
                                                    if subSubjects_v1 and subSubjects_k1 not in line_keys:
                                                        line_keys.append(subSubject_k1)
                                                        key_dict[subSubject_k1] = key_dict.get(subSubject_k1, 0)

    key_dict_per = {}
    for k, v in key_dict.items():
    	key_dict_per[k] = (v/total)*100
    print(key_dict, key_dict_per)