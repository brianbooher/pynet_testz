#!/usr/bin/env python
import yaml

my_list = range(8)
my_list.append('whatever')
my_list.append('hello')
my_list.append({})
my_list[-1]['ip_addr'] = '10.10.10.239'
my_list[-1]['attribs'] = range(7)

my_2list = range(8)
my_2list.append('whenever')
my_2list.append('goodbye')
my_2list.append({})
my_2list[-1]['ip_addr'] = '192.168.30.103'
my_2list[-1]['attribs'] = range(7)


print my_list
print len(my_list)

print yaml.dump(my_list)

print yaml.dump(my_list, default_flow_style=True)

print yaml.dump(my_list, default_flow_style=False)

with open("some_yaml_file.yml", "w") as f:
    f.write("---\n")
    f.write(yaml.dump(my_list, default_flow_style=False))
    f.write(yaml.dump(my_2list, default_flow_style=False))
