#/usr/bin/env python

#### import statements
import snmp_helper
import pickle
#### constants
PYNET_RTR2 = ('184.105.247.71', 161)
LAB_USER = ('pysnmp', 'galileo1', 'galileo1')
CCM_HISTORY_RUNNING_LAST_CHANGED = ('1.3.6.1.4.1.9.9.43.1.1.1.0', 'Running Config Last Changed: ')
CCM_HISTORY_RUNNING_LAST_SAVED = ('1.3.6.1.4.1.9.9.43.1.1.2.0', 'Running Config Last Saved: ')
CCM_HISTORY_STARTUP_LAST_CHANGED = ('1.3.6.1.4.1.9.9.43.1.1.3.0', 'Startup Config Last Saved: ')

#### functions and classes
def check_for_change(snmp_user, device_to_check, oid_to_check, history_to_check):
		previous_check = pickle.load( open( history_to_check, "rb" ) )
		print (oid_to_check[1]+str(previous_check))
		snmp_data = snmp_helper.snmp_get_oid_v3(device_to_check, snmp_user, oid_to_check[0])
		output = snmp_helper.snmp_extract(snmp_data)
		print (oid_to_check[1]+output)
		if output != previous_check:
			pickle.dump( output, open( history_to_check, "wb" ) )
		return previous_check != output


def send_mail(recipient, subject, message, sender):
	'''
	Simple function to help simplify sending SMTP email

	Assumes a mailserver is available on localhost
	'''

	import smtplib
	from email.mime.text import MIMEText

	message = MIMEText(message)
	message['Subject'] = subject
	message['From'] = sender
	message['To'] = recipient

	# Create SMTP connection object to localhost
	smtp_conn = smtplib.SMTP('localhost')

	# Send the email
	smtp_conn.sendmail(sender, recipient, message.as_string())

	# Close SMTP connection

	smtp_conn.quit()

	return True

# main function (this is the main execution code for your program)
def main():
	 # I would define any variables that are specific to this script here
	did_it_change=check_for_change(LAB_USER, PYNET_RTR2, CCM_HISTORY_RUNNING_LAST_CHANGED, 'run-conf-check.p')
	if did_it_change:
		send_mail('brian@boohers.org', 'It''s Down!!!', 'It''s Down', 'brian@boohers.org')
	print(did_it_change)
	did_it_change=check_for_change(LAB_USER, PYNET_RTR2, CCM_HISTORY_RUNNING_LAST_SAVED, 'run-conf-saved-check.p')
	if did_it_change:
		send_mail('brian@boohers.org', 'It''s Down!!!', 'It''s Down', 'brian@boohers.org')	
	print(did_it_change)
	did_it_change=check_for_change(LAB_USER, PYNET_RTR2, CCM_HISTORY_STARTUP_LAST_CHANGED, 'start-conf-check.p')
	if did_it_change:
		send_mail('brian@boohers.org', 'It''s Down!!!', 'It''s Down', 'brian@boohers.org')	
	print(did_it_change)

	 # any variables from main() that need passed into other functions would be passed as arguments


if __name__ == "__main__":                    # program execution starts here
	main()                                                   # first action is to call main function
