#!/usr/bin/env python
import yaml

with open("some_yaml_import.yml") as f:
    new_list = yaml.load(f)

print yaml.dump(new_list)

print yaml.dump(new_list, default_flow_style=True)

print yaml.dump(new_list, default_flow_style=False)

i = 0

while i < len(new_list):
    print type(new_list[i])
    print new_list[i]
    i += 1

