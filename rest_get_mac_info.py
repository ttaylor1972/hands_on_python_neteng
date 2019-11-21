import requests
import json
import sys
import argparse

from netbox_helpers import print_error_msg


debug = True
parser = argparse.ArgumentParser(description='MAC Address OUI Lookup')
parser.add_argument('mac_address', help='MAC Address to be queried')
args = parser.parse_args()

mac_address = args.mac_address

base_url = "http://macvendors.co/api/"
url = base_url + mac_address + "/json"

if debug:
    print(url)

try:
    req = requests.get(url)
    if req.status_code != 200:
        print("Status Code: " + str(req.status_code) + ". Exiting now.\n")

    print(req.json())

except Exception as err:
    print_error_msg(err)
