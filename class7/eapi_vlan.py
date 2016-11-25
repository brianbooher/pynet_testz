#!/usr/bin/env python

#### import statements
from pprint import pprint
import pyeapi
import argparse

#### constants
MY_SWITCH = 'pynet-sw2'

#### functions and classes
def add_vlan(a_switch, vlanid, name):
    a_connection = pyeapi.connect_to(MY_SWITCH)
    whole_result = a_connection.enable("show vlan")
    vlans = whole_result[0]["result"]["vlans"]
    cmds = ['vlan '+vlanid, 'name '+name]
    if vlanid in vlans:
        print "vlan exists"
    else:
        a_connection.config(cmds) 
        print "vlan doesn't exist"
        whole_result = a_connection.enable("show vlan")
        vlans = whole_result[0]["result"]["vlans"]
        pprint(vlans)

def remove_vlan(a_switch, vlanid):
    a_connection = pyeapi.connect_to(MY_SWITCH)
    whole_result = a_connection.enable("show vlan")
    vlans = whole_result[0]["result"]["vlans"]
    cmds = ['no vlan '+vlanid]
    if vlanid in vlans:
        print "vlan exists"
        a_connection.config(cmds)
        whole_result = a_connection.enable("show vlan")
        vlans = whole_result[0]["result"]["vlans"]
        pprint(vlans)
    else:
        print "vlan doesn't exist"


# main function (this is the main execution code for your program)
def main():
     # I would define any variables that are specific to this script here
    parser = argparse.ArgumentParser(description='Testing my use of ArgParser')
    parser.add_argument('--name', nargs=2, action="store", dest='vlanid_name')
    parser.add_argument('--remove', action="store", dest='vlanid')
    results = parser.parse_args()
    if results.vlanid_name:
        print "adding vlan"
        add_vlan(MY_SWITCH, results.vlanid_name[1], results.vlanid_name[0],)
    if results.vlanid:
        print "removing vlan"
        remove_vlan(MY_SWITCH, results.vlanid)

     # any variables from main() that need passed into other functions would be passed as arguments


if __name__ == "__main__":                    # program execution starts here
    main()                                                   # first action is to call main function

