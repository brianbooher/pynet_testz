#!/usr/bin/env python
'''Script uses Netmiko to connect to router and enter config mode'''

#### import statements
from netmiko import ConnectHandler
from device_list import ROUTER_LIST

#### functions


# main function (this is the main execution code for your program)
def main():
    '''Main function, opens connection, enters config mode, changes logging
    and verifies'''

for a_device in ROUTER_LIST:
    a_connection = ConnectHandler(**a_device)
    a_connection.config_mode()
    if a_connection.check_config_mode():
        a_connection.send_config_from_file(config_file='some_commands.txt')
        a_connection.exit_config_mode()
        output = a_connection.send_command("show run | include logging")
        print output
    else:
        print "We are NOT in Config mode"

if __name__ == "__main__":                    # program execution starts here
    main()                                                   # first action is to call main function
