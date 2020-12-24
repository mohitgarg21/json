import json
import jsonlines
DATA_FILE_PATH = "/home/user/Downloads/exams.json"
with jsonlines.open(DATA_FILE_PATH) as data:
    print(type(data))
    total = 0
    for line in data:
        total += 1
    print(total)