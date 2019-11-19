#!/usr/bin/env python3

"""
A script to loop over multiple Cisco IOS devices,
then run commands against each via TELNET
"""

# import necessary libraries
import telnetlib
import time

# devices.txt contains an IP address on each line
# ensure this file is in the same directory from which
# this script is run, or add the full path to this fle
with open('mydevices.txt','r') as f:
    ips = f.read().splitlines()

# define username, password
user = 'lab99'
password = 'lab123'

# iterate through the list of devices & execute the same commands
for ip in ips:
    tn = telnetlib.Telnet(ip)
    tn.read_until(b'Username: ')
    tn.write(user.encode('ascii') + b'\n')

    if password:
        tn.read_until(b'Password: ')
        tn.write(password.encode('ascii') + b'\n')
    # set the terminal length to avoid "--More--" prompt
    tn.write(b'terminal length 0' + b'\n')
    tn.write(b'show run' + b'\n\n')
    # wait (sleep) 3 seconds before continuing
    time.sleep(3)
    tn.write(b'show ip int brief' + b'\n\n')  # ???
    # close the connection & print output
    tn.write(b'exit\n')
    line = tn.read_all().decode('ascii')
    print(line)
