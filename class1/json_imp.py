#!/usr/bin/env python
import json 
from pprint import pprint as pp
with open("some_json_import.json") as f:
    new_list = json.load(f)

print json.dumps(new_list)
pp (new_list)

i = 0

while i < len(new_list):
    print type(new_list[i])
    print new_list[i]
    i += 1

