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
try:
    txt = load_from_json_file("add_item.json")
except FileNotFoundError:
    txt = []
txt = txt + new
save_to_json_file(txt, "add_item.json")
