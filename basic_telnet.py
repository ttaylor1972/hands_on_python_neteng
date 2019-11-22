#!/usr/bin/env python3
"""
A basic TELNET program to connect to a Cisco IOS device,
then output its configuration
"""

# import necessary libraries
import telnetlib
import getpass
import sys

# set the Cisco device address
deviceAddr = "172.16.32.33"
# the user will be prompted to enter their username & password
switchUser = input("Enter your telnet username: ")
switchPass = getpass.getpass()

# gather username, password from user
# connect to the device & send username, password
# convert commands to ASCII format
t = telnetlib.Telnet(deviceAddr)
t.read_until(b"Username:")
t.write(switchUser.encode("ascii") + b"\n")
if switchPass:
    t.read_until(b"Password:")
t.write(switchPass.encode("ascii") + b"\n")

# set Cisco device terminal length to "0"
# so that the session doesn't hang waiting for user
# to press spacebar
t.write(b"terminal length 0\n")
# send IOS "show version" command, then exit
t.write(b"sh ver\n")
t.write(b"exit\n")
# output device responses in ASCII format
print(t.read_all().decode("ascii"))
