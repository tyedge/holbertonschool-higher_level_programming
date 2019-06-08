#!/usr/bin/python3
import json
import sys
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


newlist = []
filename = "add_item.json"
i = 1
save_to_json_file(newlist, filename)
with open(filename, 'a', encoding='utf-8') as file:
    while i < len(sys.argv):
        newlist.append(sys.argv[i])
        file.write(json.dumps(newlist))
        i += 1

save_to_json_file(newlist, filename)
load_from_json_file(filename)
