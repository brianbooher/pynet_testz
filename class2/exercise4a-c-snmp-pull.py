#!/usr/bin/env python

#### import statements
import pysnmp
import snmp_helper

#### constants
COMMUNITY_STRING = 'galileo'
SNMP_PORT = 161
pynet_rtr1 = {'IP': '184.105.247.70', 'name': 'pynet_rtr1'}
pynet_rtr2 = {'IP': '184.105.247.71', 'name': 'pynet_rtr2'}
sysnam_OID = {'OID': '1.3.6.1.2.1.1.5.0', 'name': 'System Name'}
sysdesc_OID = {'OID': '1.3.6.1.2.1.1.1.0', 'name': 'System Description'}

#### functions and classes

# main function (this is the main execution code for your program)

def snmp_get(snmp_data, device):
	access_details = (device['IP'], COMMUNITY_STRING, SNMP_PORT)
	snmp_results = snmp_helper.snmp_get_oid(access_details, snmp_data['OID'])
	output = snmp_helper.snmp_extract(snmp_results)
	print("For "+device['name']+" the "+snmp_data['name']+" is "+'\n')
	print(output)
	print('\n')


def main():
	snmp_get(sysnam_OID, pynet_rtr1)
	snmp_get(sysdesc_OID, pynet_rtr1)
	snmp_get(sysnam_OID, pynet_rtr2)
	snmp_get(sysdesc_OID, pynet_rtr2)

	
		 # any variables from main() that need passed into other functions would be passed as arguments


if __name__ == "__main__":                    # program execution starts here
	main()                                                   # first action is to call main function
