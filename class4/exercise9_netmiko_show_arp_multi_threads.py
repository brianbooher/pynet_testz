#!/usr/bin/env python
'''Script uses Netmiko to connect to router and enter config mode
Please note. This script looks just like yours, but that was after I tried
to take one of my previous scripts and keep the extended dictionary entries I had.
it would seem that Netmiko does extensive error checking on the dictionaries
to make sure the values are appropriate. '''

#### import statements
# Catch Paramiko warnings about libgmp and RandomPool
import warnings
with warnings.catch_warnings(record=True) as w:
    import paramiko

import multiprocessing
from datetime import datetime

import netmiko
from netmiko.ssh_exception import NetMikoTimeoutException, NetMikoAuthenticationException

from device_list import A_DEVICE_LIST

def print_output(results):
    '''return results of each process and which were successful or not'''
    print "\nSuccessful devices:"
    for a_dict in results:
        for identifier, a_result in a_dict.iteritems():
            (success, out_string) = a_result
            if success:
                print '\n\n'
                print '#' * 80
                print 'Device = {0}\n'.format(identifier)
                print out_string
                print '#' * 80

    print "\n\nFailed devices:\n"
    for a_dict in results:
        for identifier, a_result in a_dict.iteritems():
            (success, out_string) = a_result
            if not success:
                print 'Device failed = {0}'.format(identifier)

    print "\nEnd time: " + str(datetime.now())
    print


def worker_show_arp(a_device, mp_queue):
    '''
    Return a dictionary where the key is the device identifier
    Value is (success|fail(boolean), return_string)
    '''

    try:
        a_device['port']
    except KeyError:
        a_device['port'] = 22

    identifier = '{ip}:{port}'.format(**a_device)
    return_data = {}

    show_arp_command = 'show arp'
    sshclass = netmiko.ssh_dispatcher(a_device['device_type'])

    try:
        net_connect = sshclass(**a_device)
        show_arp = net_connect.send_command(show_arp_command)
    except (NetMikoTimeoutException, NetMikoAuthenticationException) as an_error:
        return_data[identifier] = (False, an_error)

        # Add data to the queue (for parent process)
        mp_queue.put(return_data)
        return None

    return_data[identifier] = (True, show_arp)
    mp_queue.put(return_data)


def main():
    '''Main code segments. Starts multiple processes to execute commands in
    parallel'''
    mp_queue = multiprocessing.Queue()
    processes = []

    print "\nStart time: " + str(datetime.now())

    for a_device in A_DEVICE_LIST:

        a_process = multiprocessing.Process(target=worker_show_arp, args=(a_device, mp_queue))
        processes.append(a_process)
        # start the work process
        a_process.start()

    # wait until the child processes have completed
    for a_process in processes:
        a_process.join()

    # retrieve all the data from the queue
    results = []
    for a_process in processes:
        results.append(mp_queue.get())

    print_output(results)

if __name__ == "__main__":                    # program execution starts here
    main()                                                   # first action is to call main function
