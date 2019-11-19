#!/usr/bin/env python3

"""
A script to connect to a Cisco IOS device
and pass some commands, via TELNET
"""

# import the required modules; these come with Python3
import getpass
import telnetlib


# set your device IP; ensure TELNET is enabled
host = '192.168.122.10'
user = 'lab99'
password = 'lab123'
# if you don't want a hardcoaded password use:
#    passsword = getpass.getpass()

# connect to the device via TELNET, refer to the session as "tn"
tn = telnetlib.Telnet(host)

# read until the byte string "Username: "" appears
tn.read_until(b'Username: ')
# send the user name in ASCII format
# always send a ""\n" - the new line/ENTER key
tn.write(user.encode('ascii') + b'\n')

# read/wait until the byte string "Password: " appears
# send the password in ASCII format
tn.read_until(b'Password: ')
tn.write(password.encode('ascii')+b'\n')

tn.write(b'enable\n')
tn.write(b'cisco\n')

# each command should be sent as bytes
# set the terminal length to "0", so no "--More--" prompt
tn.write('terminal length 0\n'.encode())
# show the device software version
tn.write(b'show version' + b'\n')
# send the configure command
tn.write(b'configure terminal\n')
# exit config mode
tn.write(b'end\n')
# end the TELNET session
tn.write(b'exit\n')

# convert the output from bytes to ASCII
# to make it human-readable
line=tn.read_all().decode('ascii')
print(line)
