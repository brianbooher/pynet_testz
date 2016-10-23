import telnetlib

TELNET_PORT = 23
TELNET_TIMEOUT = 6

ip_addr = '184.105.247.70'
username = 'pyclass'
password = '88newclass'
remote_conn = telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
output=remote_conn.read_until("sername:", TELNET_TIMEOUT)
print(output)
remote_conn.write(username+'\n')
output=remote_conn.read_until("assword:", TELNET_TIMEOUT)
print(output)
remote_conn.write(password+'\n')
output=remote_conn.read_until("#", TELNET_TIMEOUT)
print(output)
remote_conn.write("show ip int brief"+'\n')
output=remote_conn.read_very_eager()
print(output)
remote_conn.close()

