!#/usr/bin/env python

'''
Write a script that connects to the lab pynet-rtr1, logins, and executes the
'show ip int brief' command.
'''

#### import statements

import telnetlib
import time
import socket
import sys
import getpass

#### constants
TELNET_PORT = 23
TELNET_TIMEOUT = 6

#### functions and classes

class TelnetGet(object):
	def __init__(self, ip, username, password, clicommand):
		self.ip = ip
		self.username = username
		self.password = password
		self.clicommand = clicommand
	def telnet_connect():
		'''
		Establish telnet connection
		'''
		try:
			return telnetlib.Telnet(self.ip, TELNET_PORT, TELNET_TIMEOUT)
		except socket.timeout:
			sys.exit("Connection timed-out")
	def login(remote_conn, username, password):
		'''
		Login to network device
		'''
		output = remote_conn.read_until("sername:", TELNET_TIMEOUT)
		remote_conn.write(username + '\n')
		output += remote_conn.read_until("ssword:", TELNET_TIMEOUT)
		remote_conn.write(password + '\n')
		return output


# main function (this is the main execution code for your program)
def main():
'''
Write a script that connects to the lab pynet-rtr1, logins, and executes the
'show ip int brief' command.
'''
ip_addr = raw_input("IP address: ")
ip_addr = ip_addr.strip()
username = 'pyclass'
password = getpass.getpass()

remote_conn = telnet_connect(ip_addr)
output = login(remote_conn, username, password)

time.sleep(1)
remote_conn.read_very_eager()
disable_paging(remote_conn)

output = send_command(remote_conn, 'show ip int brief')

print "\n\n"
print output
print "\n\n"

remote_conn.close()


if __name__ == "__main__":                    # program execution starts here
	main()                                                   # first action is to call main function
