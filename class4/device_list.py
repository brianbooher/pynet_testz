RTR1 = {
    'device_type': 'cisco_ios',
    'ip' : '184.105.247.70',
    'port' : 22,
    'username' : 'pyclass',
    'alt_key_file' : 'labhosts',
    'ssh_strict' : True,
    'alt_host_keys' : True,
    'password' : '88newclass'}

RTR2 = {
    'device_type': 'cisco_ios',
    'ip' : '184.105.247.71',
    'port' : 22,
    'username' : 'pyclass',
    'alt_key_file' : 'labhosts',
    'ssh_strict' : True,
    'alt_host_keys' : True,
    'password' : '88newclass'}

JNPR_SRX1 = {
    'device_type': 'juniper',
    'ip' : '184.105.247.76',
    'port' : 22,
    'username' : 'pyclass',
    'alt_key_file' : 'labhosts',
    'ssh_strict' : True,
    'alt_host_keys' : True,
    'password' : '88newclass'}

A_DEVICE_LIST = [RTR1, RTR2, JNPR_SRX1]

ROUTER_LIST = [RTR1, RTR2]

