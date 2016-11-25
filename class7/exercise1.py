#!/usr/bin/env python

#### import statements
import pyeapi
from pprint import pprint

#### constants
MY_SWITCH = 'pynet-sw2'

#### functions and classes

def parse_ethernet_interfaces(a_device):
    ethernet_interfaces = dict()
    a_connection = pyeapi.connect_to(a_device)
    show_interfaces = a_connection.enable("show interfaces")
    all_interfaces = show_interfaces[0]["result"]["interfaces"]
    for an_interface in all_interfaces:
        if "Ethernet" in an_interface:
            ethernet_interfaces.update({an_interface : {'interfacename' : all_interfaces[an_interface]["name"]}})
            ethernet_interfaces[an_interface].update({'inoctets' : all_interfaces[an_interface]["interfaceCounters"]["inOctets"]})
            ethernet_interfaces[an_interface].update({'outoctets' : all_interfaces[an_interface]["interfaceCounters"]["outOctets"]})
    return ethernet_interfaces

# main function (this is the main execution code for your program)
def main():
    the_interfaces = parse_ethernet_interfaces(MY_SWITCH)
    pprint(the_interfaces)

     # any variables from main() that need passed into other functions would be passed as arguments


if __name__ == "__main__":                    # program execution starts here
    main()                                                   # first action is to call main function
