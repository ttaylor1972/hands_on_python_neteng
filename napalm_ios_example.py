#!/usr/bin/env python3

"""
Sample NAPALM configuration script
for Cisco IOS devices
"""

# import the NAPALM module
# ensure it has been installed "pip3 install napalm"
import napalm

# load the appropriate driver for the device type
# here, we are using the Cisco IOS one
driver = get_network_driver("ios")

# define the device parameters: hostname/IP, username, password
device = driver(hostname='172.16.32.1',
         username='ivoxy',
         password='ivoxy123')

# connect to the device
device.open()

# run commands on the device
device.get_interfaces()
