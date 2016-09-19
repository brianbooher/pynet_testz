#!/usr/bin/env python
'''Script uses Netmiko to connect to router and enter config mode
Please note. This script looks just like yours, but that was after I tried
to take one of my previous scripts and keep the extended dictionary entries I had.
it would seem that Netmiko does extensive error checking on the dictionaries to make sure the values are appropriate. '''

#### import statements
from netmiko import ConnectHandler

#### constants
RTR1 = {
    'device_type': 'cisco_ios',
    'ip' : '184.105.247.70',
    'port' : 22,
    'username' : 'pyclass',
    'password' : '88newclass'}

RTR2 = {
    'device_type': 'cisco_ios',
    'ip' : '184.105.247.71',
    'port' : 22,
    'username' : 'pyclass',
    'password' : '88newclass'}

JNPR_SRX1 = {
    'device_type': 'juniper',
    'ip' : '184.105.247.76',
    'port' : 22,
    'netconf_port' : 830,
    'username' : 'pyclass',
    'password' : '88newclass'}

#### functions


# main function (this is the main execution code for your program)
def main():
    '''Main function, opens connection, enters config mode and verifies'''
    pynet_rtr1 = ConnectHandler(**RTR1)
    pynet_rtr1.config_mode()
    if pynet_rtr1.check_config_mode():
        print "We are in Config mode"
    else:
        print "We are NOT in Config mode"

if __name__ == "__main__":                    # program execution starts here
    main()                                                   # first action is to call main function
