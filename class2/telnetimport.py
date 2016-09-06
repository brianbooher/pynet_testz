#!/usr/bin/env python

import telnetlib
import time

TELNET_PORT = 23
TELNET_TIMEOUT = 6

def main():
	ip_addr = '184.105.247.70'
	username = 'pyclass'
	password = '88newclass'
	
	remote_conn = telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
	remote_conn.read_until("sername:", TELNET_TIMEOUT)
	remote_conn.write(username+'\n')
        remote_conn.read_until("assword:", TELNET_TIMEOUT)
        remote_conn.write(password+'\n')
        remote_conn.read_until("#", TELNET_TIMEOUT)
        remote_conn.write("show ip int brief"+'\n')
#### using read_until and flagging on value in command prompt. As part of my standard configuratin, I could speciy a unique tag for the prompt that would always work.
        output=remote_conn.read_until("#", TELNET_TIMEOUT)
	print(output)
        remote_conn.close()
	
if __name__ == "__main__":
	main()
