#!/usr/bin/env python

import telnetlib

TELNET_PORT = 23
TELNET_TIMEOUT = 6

def main():
	ip_addr = '184.105.247.70'
	username = 'pyclass'
	password = '88newclass'
	
	remote_conn = telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
	output = remote_conn.read_until("username:", TELNET_TIMEOUT)
	remote_conn.close()
	print(output)
	
if __name__ == "__main__":
	main()