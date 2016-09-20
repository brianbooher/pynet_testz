#!/usr/bin/env python
'''Script uses Netmiko to connect to router and enter config mode'''

#### import statements
from netmiko import ConnectHandler
from device_list import RTR2
#### functions


# main function (this is the main execution code for your program)
def main():
    '''Main function, opens connection, enters config mode, changes logging
    and verifies'''
    pynet_rtr2 = ConnectHandler(**RTR2)
    pynet_rtr2.config_mode()
    if pynet_rtr2.check_config_mode():
        pynet_rtr2.send_command("logging buffered 16384")
        pynet_rtr2.exit_config_mode()
        output = pynet_rtr2.send_command("show run | include logging buff")
        print output
    else:
        print "We are NOT in Config mode"

if __name__ == "__main__":                    # program execution starts here
    main()                                                   # first action is to call main function
