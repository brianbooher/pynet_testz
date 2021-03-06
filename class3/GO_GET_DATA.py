#/usr/bin/env python
"""Import OID values every 5 minutes for one hour"""
#### import statements
import pickle
import os
import time
import snmp_helper
#### constants
PYNET_RTR1 = ('184.105.247.70', 161)
PYNET_RTR2 = ('184.105.247.71', 161)
LAB_USER = ('pysnmp', 'galileo1', 'galileo1')
IFDESCR_FA4 = ('Interface Description of FE4: ', '1.3.6.1.2.1.2.2.1.2.5')
IFINOCTETS_FA4 = ('In Octets of FE4: ', '1.3.6.1.2.1.2.2.1.10.5')
IFINUCASTPKTS_FA4 = ('In Unicast Packets for FE4: ', '1.3.6.1.2.1.2.2.1.11.5')
IFOUTOCTETS_FA4 = ('Out Octets for FE4: ', '1.3.6.1.2.1.2.2.1.16.5')
IFOUTUCASTPKTS_FA4 = ('Out Unicast Packets for FE4: ', '1.3.6.1.2.1.2.2.1.17.5')
ALL_OIDS = (IFDESCR_FA4, IFINOCTETS_FA4, IFINUCASTPKTS_FA4, IFOUTOCTETS_FA4, IFOUTUCASTPKTS_FA4)
STORAGE = 'f4-traffic-stats.p'
#### functions and classes
def check_it(snmp_user, device_to_check, oid_to_check):
    """Get's OID value and extracts just the data"""
    snmp_data = snmp_helper.snmp_get_oid_v3(device_to_check, snmp_user, oid_to_check[1])
    output = snmp_helper.snmp_extract(snmp_data)
    return output

# main function (this is the main execution code for your program)
def main():
    """Main function, calls other functions"""
    alt_accumulator = []
    # Must collect 13 data points to get 12 readings
    for a_counter in xrange(0, 13):
        a_list = []
        accumulator = []
    #For each run, data is put into a list in the order of "Interface Description of FE4,
    #In Octets of FE4", "In Unicast Packets for FE4", "Out Octets for FE4", and "Out
    #Unicast Packets for FE4
        for another_counter in ALL_OIDS:
            output = check_it(LAB_USER, PYNET_RTR1, another_counter)
            a_list.append(output)
#        print a_list
        if not os.path.exists(STORAGE):
            open(STORAGE, 'w').close()
            accumulator.append(a_list)
            alt_accumulator.append(a_list)
        else:
            accumulator = pickle.load(open(STORAGE, "rb"))
            accumulator.append(a_list)
            alt_accumulator.append(a_list)
        pickle.dump(accumulator, open(STORAGE, "wb"))
        time.sleep(3)
        accumulator = pickle.load(open(STORAGE, "rb"))
    print '\n'
    print accumulator
    print '\n'
    print alt_accumulator

if __name__ == "__main__":                    # program execution starts here
    main()                                    # first action is to call main function
