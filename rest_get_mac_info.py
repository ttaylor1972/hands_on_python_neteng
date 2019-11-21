import requests
import json
from netbox_helpers import print_error_msg

debug = True

mac_address = "08:74:02:00:00:00"
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
