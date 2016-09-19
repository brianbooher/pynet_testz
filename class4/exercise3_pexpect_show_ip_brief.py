#!/usr/bin/env python
'''Script uses Pexpect to connect to router and return "show ip int brief" '''
#### import statements
import pexpect

#### constants
PYNET_RTR2 = {
    'ip_addr' : '184.105.247.71',
    'ssh_port' : 22,
    'username' : 'pyclass',
    'hostkeyfile' : 'labhosts', #local file containing hostkeys
    'passwd' : '88newclass',
    'enableprompt' : 'pynet-rtr2#',
    'configureprompt' : r'pynet-rtr2\(config\)#'}
#### functions

def open_ssh_connection(**host_details):
    '''function establishes connection to remote host'''
    remote_conn = pexpect.spawn('ssh -l {} {} -p {} -o UserKnownHostsFile={}'.format(
        host_details['username'],
        host_details['ip_addr'],
        host_details['ssh_port'],
        host_details['hostkeyfile']))
    remote_conn.timeout = 10
    remote_conn.expect('ssword: ')
    remote_conn.sendline(host_details['passwd'])
    remote_conn.expect(host_details['enableprompt'])
    return remote_conn

def disable_paging(remote_conn, **host_details):
    '''Disable paging on a Cisco router'''
    remote_conn.sendline("terminal length 0")
    remote_conn.expect(host_details['enableprompt'])


# main function (this is the main execution code for your program)
def main():
    '''Main function, opens connection, disables paging and runs command'''
    remote_conn = open_ssh_connection(**PYNET_RTR2)
    disable_paging(remote_conn, **PYNET_RTR2)
    remote_conn.sendline("show ip int brief")
    remote_conn.expect(PYNET_RTR2['enableprompt'])
    print remote_conn.before
     # any variables from main() that need passed into other functions would be passed as arguments


if __name__ == "__main__":                    # program execution starts here
    main()                                                   # first action is to call main function
