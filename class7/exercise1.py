#!/usr/bin/env python
'''performs show interface and parses inoctets and outoctets for Ethernet interfaces only'''
#### import statements
from pprint import pprint
import pyeapi

#### constants
MY_SWITCH = 'pynet-sw2'

#### functions and classes

def parse_ethernet_interfaces(a_device):
    '''Establishes connetion, unwraps the results and puts into a dictionary of interface names
        and counters'''
    ethernet_interfaces = dict()
    a_connection = pyeapi.connect_to(a_device)
    show_interfaces = a_connection.enable("show interfaces")
    all_interfaces = show_interfaces[0]["result"]["interfaces"]
    for an_interface in all_interfaces:
        if "Ethernet" in an_interface:
            ethernet_interfaces.update(
                {an_interface : {'interfacename' : all_interfaces[an_interface]["name"]}})
            ethernet_interfaces[an_interface].update(
                {'inoctets' : all_interfaces[an_interface]["interfaceCounters"]["inOctets"]})
            ethernet_interfaces[an_interface].update(
                {'outoctets' : all_interfaces[an_interface]["interfaceCounters"]["outOctets"]})
    return ethernet_interfaces

# main function (this is the main execution code for your program)
def main():
    '''main part of program. calls the primary function and prints the results.'''
    the_interfaces = parse_ethernet_interfaces(MY_SWITCH)
    pprint(the_interfaces)

     # any variables from main() that need passed into other functions would be passed as arguments


if __name__ == "__main__":                    # program execution starts here
    main()                                                   # first action is to call main function
