#!/usr/bin/env python
'''Script uses Pexpect to connect to router and return "show ip int brief" '''
#### import statements
from exercise3_pexpect_show_ip_brief import open_ssh_connection
from exercise3_pexpect_show_ip_brief import disable_paging
#### constants
PYNET_RTR2 = {
    'ip_addr' : '184.105.247.71',
    'ssh_port' : 22,
    'username' : 'pyclass',
    'hostkeyfile' : 'labhosts', #local file containing hostkeys
    'passwd' : '88newclass',
    'enableprompt' : 'pynet-rtr2#',
    'configureprompt' : r'pynet-rtr2\(config\)#'}

def change_config(a_command, a_connection, **host_details):
    '''enter config, execute command and exit to enable prompt'''
    a_connection.sendline("config t")
    a_connection.expect(host_details['configureprompt'])
    a_connection.sendline(a_command)
    a_connection.expect(host_details['configureprompt'])
    a_connection.sendline("end")
    return a_connection.before

# main function (this is the main execution code for your program)
def main():
    '''Main function, opens connection, disables paging and runs command'''
    remote_conn = open_ssh_connection(**PYNET_RTR2)
    disable_paging(remote_conn, **PYNET_RTR2)
    a_result = change_config('logging buffered 16384', remote_conn, **PYNET_RTR2)
    print a_result
    a_result = change_config('logging buffered 8192', remote_conn, **PYNET_RTR2)
    print a_result

     # any variables from main() that need passed into other functions would be passed as arguments


if __name__ == "__main__":                    # program execution starts here
    main()                                                   # first action is to call main function
