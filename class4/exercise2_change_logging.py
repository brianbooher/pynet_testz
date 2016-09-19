#!/usr/bin/env python
'''Script uses paramiko to connect to router and change logging buffer size '''
#### import statements
import time
from exercise1_paramiko_get_run_config import open_ssh_connection
from exercise1_paramiko_get_run_config import disable_paging

#### constants
PYNET_RTR2 = {
    'ip_addr' : '184.105.247.71',
    'ssh_port' : 22,
    'username' : 'pyclass',
    'hostkeyfile' : 'labhosts', #local file containing hostkeys
    'passwd' : '88newclass'}

# main function (this is the main execution code for your program)

def main():
    '''Main function, opens connection, disables paging and runs command'''
    remote_conn_pre = open_ssh_connection(**PYNET_RTR2)
    remote_conn = remote_conn_pre.invoke_shell()
    disable_paging(remote_conn)
    remote_conn.send("config t\n")
    time.sleep(1)
    remote_conn.send("logging buffered 16384\n")
    time.sleep(1)
    remote_conn.send("end\n")
    time.sleep(1)
    remote_conn.send("wr me\n")
    time.sleep(1)
    output = remote_conn.recv(5000)
    print output
    # any variables from main() that need passed into other functions would be
    # passed as arguments


if __name__ == "__main__":                    # program execution starts here
    main()                                                   # first action is to call main function
