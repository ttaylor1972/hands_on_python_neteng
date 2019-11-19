#!/usr/bin/env python3

"""
A script to parse the contents of a text file
that contains entries in the form of A:B
This is a basic file-parsing exercise
"""
# ensure you have a file named 'devices.txt'
# which contains a few (say, 3) entries like "172.16.32.14:172.16.32.15"
# as we will be parsing these entries into tuples

# the 'devices.txt' file must be in the same directory as where you
# run the script, or it can't find the file
# alternatively, could put the full path to the file:
#   with open('C:\Scripts\TelnetStuff\devices.txt') as f:

# read in the device file, split the input into separate lines
# put that into a variable
with open('devices.txt', 'r') as f:
    d = f.read().splitlines()

# create a list of IP addresses from the above
# split each line into parts, using ":" as the separator
# put the output into a tuple data definition
ip = list()
for item in d:
    x = item.split(':')
    ip.append(tuple(x))

# print/show the tuples
print(ip)
