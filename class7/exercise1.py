#!/usr/bin/env python

#### import statements
import pyeapi

#### constants
MY_SWITCH = 'pynet-sw2'

#### functions and classes
def parse_Value(a_device, a_command):
    a_connection = pyeapi.connect_to(a_device)
    show_interfaces = a_connection.enable(a_command)
    all_interfaces = show_interfaces[0]["result"]["interfaces"]
    for an_interface in all_interfaces:
        if "Ethernet" in an_interface:
            in-out-octets = {an_interface :  all_interfaces[an_interface][name]

# main function (this is the main execution code for your program)
def main():
     parse_Value(MY_SWITCH, 'show interfaces')

     # any variables from main() that need passed into other functions would be passed as arguments


if __name__ == "__main__":                    # program execution starts here
    main()                                                   # first action is to call main function
