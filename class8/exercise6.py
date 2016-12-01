#!/usr/bin/env python

#### import statements
import django
import threading
from netmiko import ConnectHandler
from datetime import datetime
from net_system.models import NetworkDevice, Credentials

#### constants
MY_VAL = 'whatever'
OTHER_CONST = 'something else'

#### functions and classes
def show_ver(a_device):
    remote_conn = ConnectHandler(device_type=a_device.device_type, 
                                 ip=a_device.ip_address,
                                 username=a_device.credentials.username, 
                                 password=a_device.credentials.password,
                                 port=a_device.port, secret='')
    a_result = remote_conn.send_command_expect("show version")
    print
    print a_device
    print '#' * 40
    print a_result
    print
    print '#' * 40
    print

# main function (this is the main execution code for your program)
def main():
     # I would define any variables that are specific to this script here
    django.setup()
    devices = NetworkDevice.objects.all()
    start_time = datetime.now()
    for a_device in devices:
        my_thread = threading.Thread(target=show_ver, args=(a_device,))
        my_thread.start()

    main_thread = threading.currentThread()
    for some_thread in threading.enumerate():
        if some_thread != main_thread:
            print some_thread
            some_thread.join()

    elapsed_time = datetime.now() - start_time
    print "Elsapsed time: " + str(elapsed_time)

     # any variables from main() that need passed into other functions would be passed as arguments


if __name__ == "__main__":                    # program execution starts here
    main()                                                   # first action is to call main function

