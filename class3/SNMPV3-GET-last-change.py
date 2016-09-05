#/usr/bin/env python

#### import statements
import snmp_helper
import pickle
import json
import email_helper
#### constants
PYNET_RTR2 = ('184.105.247.71', 161)
LAB_USER = ('pysnmp', 'galileo1', 'galileo1')
CCM_HISTORY_RUNNING_LAST_CHANGED = ('1.3.6.1.4.1.9.9.43.1.1.1.0', 'Running Config Last Changed: ')
CCM_HISTORY_RUNNING_LAST_SAVED = ('1.3.6.1.4.1.9.9.43.1.1.2.0', 'Running Config Last Saved: ')
CCM_HISTORY_STARTUP_LAST_CHANGED = ('1.3.6.1.4.1.9.9.43.1.1.3.0', 'Startup Config Last Saved: ')

#### functions and classes
def check_for_change(snmp_user, device_to_check, oid_to_check, history_to_check):
		with open(history_to_check) as f:
			previous_check = json.load(f)
		print (oid_to_check[1]+str(previous_check))
		snmp_data = snmp_helper.snmp_get_oid_v3(device_to_check, snmp_user, oid_to_check[0])
		output = snmp_helper.snmp_extract(snmp_data)
		print (oid_to_check[1]+output)
		if output != previous_check:
			with open(history_to_check, "w") as f:
				json.dump(output,f)
		return previous_check != output

# main function (this is the main execution code for your program)
def main():

		did_it_change=check_for_change(LAB_USER, PYNET_RTR2, CCM_HISTORY_RUNNING_LAST_CHANGED, 'run-conf-check.json')
		if did_it_change:
			email_helper.send_mail('brian@boohers.org', "It's changed!!!", "It's changed!!!", 'brian@boohers.org')
		print(did_it_change)
		did_it_change=check_for_change(LAB_USER, PYNET_RTR2, CCM_HISTORY_RUNNING_LAST_SAVED, 'run-conf-saved-check.json')
		if did_it_change:
			email_helper.send_mail('brian@boohers.org', "It's changed!!!", "It's changed!!!", 'brian@boohers.org')	
		print(did_it_change)
		did_it_change=check_for_change(LAB_USER, PYNET_RTR2, CCM_HISTORY_STARTUP_LAST_CHANGED, 'start-conf-check.json')
		if did_it_change:
			email_helper.send_mail('brian@boohers.org', "It's changed!!!", "It's changed!!!", 'brian@boohers.org')	
		print(did_it_change)


	 # any variables from main() that need passed into other functions would be passed as arguments


if __name__ == "__main__":                    # program execution starts here
	main()                                                   # first action is to call main function
