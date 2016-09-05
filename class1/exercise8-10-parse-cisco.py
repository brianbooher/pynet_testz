#!/usr/bin/env python
import json
import yaml
from ciscoconfparse import CiscoConfParse
#import config file into variable
cisco_cfg = CiscoConfParse("cisco_ipsec.txt")

intf = cisco_cfg.find_objects(r"^interface")
intf
print ('\n')
print("Interfaces only")
for i in intf:
    print i.text

print ('\n')
print("fourth Interface children details")
fa4 = intf[4]
fa4
fa4.children
for child in fa4.children:
    print child.text

crypto_group2 = cisco_cfg.find_objects_w_child(parentspec=r"crypto map", childspec=r"group2")
crypto_group2
print ('\n')
print("Crypto Maps with group2")
for j in crypto_group2:
    print j.text
print ('\n')
crypto_no_aes = cisco_cfg.find_objects_wo_child(r'crypto map', r'AES')
print("Crypto Maps without AES")
for k in crypto_no_aes:
    print k.text

