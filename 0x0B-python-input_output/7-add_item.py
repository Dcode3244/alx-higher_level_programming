#!/usr/bin/python3
""" defines a script that adds all arguments to a
    python list and save them to a file """


import json
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

new = []
for i in range(1, len(sys.argv)):
    new.append(sys.argv[i])

save_to_json_file(new, "add_item.json")
txt = load_from_json_file("add_item.json")
with open("add_item.json", "a", encoding="utf-8") as f:
    f.write("\n")
