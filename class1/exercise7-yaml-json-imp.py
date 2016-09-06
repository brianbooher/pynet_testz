#!/usr/bin/env python
import yaml
import json
from pprint import pprint as pp

with open("some_yaml_import.yml") as f:
    new_list = yaml.load(f)

#print yaml.dump(new_list)

#print yaml.dump(new_list, default_flow_style=True)

#print yaml.dump(new_list, default_flow_style=False)

pp(new_list)

with open("some_json_import.json") as f:
    new_list2 = json.load(f)

print json.dumps(new_list2)
pp (new_list2)

i = 0
print "YAML Variable"
while i < len(new_list):
    print type(new_list[i])
    print new_list[i]
    i += 1


i = 0
print "JSON Variable"
while i < len(new_list2):
    print type(new_list2[i])
    print new_list2[i]
    i += 1

