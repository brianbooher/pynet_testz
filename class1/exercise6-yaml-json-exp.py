#!/usr/bin/env python
import yaml
import json

my_list = range(8)
my_list.append('bezonkers')
my_list.append('whattsamattau')
my_list.append({})
my_list[-1]['ip_addr'] = '10.10.15.73'
my_list[-1]['attribs'] = range(7)

print my_list
print len(my_list)

print yaml.dump(my_list)

print yaml.dump(my_list, default_flow_style=True)

print yaml.dump(my_list, default_flow_style=False)

with open("some_yaml_file.yml", "w") as f:
    f.write("---\n")
    f.write(yaml.dump(my_list, default_flow_style=False))

print json.dumps(my_list)

with open("some_json_file.json", "w") as f:
    json.dump(my_list,f)

