#!/usr/bin/env python
'''Script uses paramiko to connect to router and return "show run" '''
#### import statements
import time
import paramiko

#### constants
PYNET_RTR2 = {
    'ip_addr' : '184.105.247.71',
    'ssh_port' : 22,
    'username' : 'pyclass',
    'hostkeyfile' : 'labhosts', #local file containing hostkeys
    'passwd' : '88newclass'}
#### functions

def open_ssh_connection(**host_details):
    '''function establishes connection to remote host'''
    remote_conn_pre = paramiko.SSHClient()
    remote_conn_pre.load_host_keys(host_details['hostkeyfile'])
    remote_conn_pre.connect(hostname=host_details['ip_addr'],
                            port=host_details['ssh_port'],
                            username=host_details['username'],
                            password=host_details['passwd'],
                            look_for_keys=False,
                            allow_agent=False)
    return remote_conn_pre

def disable_paging(remote_conn):
    '''Disable paging on a Cisco router'''
    remote_conn.send("terminal length 0\n")
    time.sleep(1)
    # Clear the buffer on the screen
    output = remote_conn.recv(1000)
    return output


# main function (this is the main execution code for your program)
def main():
    '''Main function, opens connection, disables paging and runs command'''
    remote_conn_pre = open_ssh_connection(**PYNET_RTR2)
    remote_conn = remote_conn_pre.invoke_shell()
    disable_paging(remote_conn)
    remote_conn.send("show run\n")
    time.sleep(3)
    output = remote_conn.recv(5000)
    print output
     # any variables from main() that need passed into other functions would be passed as arguments


if __name__ == "__main__":                    # program execution starts here
    main()                                                   # first action is to call main function
