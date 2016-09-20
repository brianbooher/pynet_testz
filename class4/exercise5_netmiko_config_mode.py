#!/usr/bin/env python
'''Script uses Netmiko to connect to router and enter config mode
Please note. This script looks just like yours, but that was after I tried
to take one of my previous scripts and keep the extended dictionary entries I had.
it would seem that Netmiko does extensive error checking on the dictionaries to make sure the values are appropriate. '''

#### import statements
from netmiko import ConnectHandler
import device_list

# main function (this is the main execution code for your program)
def main():
    '''Main function, opens connection, enters config mode and verifies'''
    pynet_rtr1 = ConnectHandler(**device_list.RTR1)
    pynet_rtr1.config_mode()
    if pynet_rtr1.check_config_mode():
        print "We are in Config mode"
    else:
        print "We are NOT in Config mode"

if __name__ == "__main__":                    # program execution starts here
    main()                                                   # first action is to call main function
