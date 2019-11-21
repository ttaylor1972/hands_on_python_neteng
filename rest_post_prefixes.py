import requests
import json
from netbox_helpers import make_prefix_for_netbox, print_error_msg

debug = True
port = 32768
base_url = "http://172.16.32.74:{}/api/".format(port)
prefix_path = "ipam/prefixes/"
url = base_url + prefix_path
netbox_api_token = "0123456789abcdef0123456789abcdef01234567"
_headers = {
    "Authorization": "Token {}".format(netbox_api_token),
    "Accept": "application/json",
    "Content-type": "application/json",
}

if debug:
    print(_headers)
    print("API URL: {}".format(url))

# TODO: Change the second_octet variable to your lab number
second_octet = 50
lab_tag = "lab{}".format(second_octet)
my_tags = ["useful_meta_data", lab_tag]

for third_octet in range(0, 51):
    prefix = "10." + str(second_octet) + "." + str(third_octet) + ".0/24"
    payload = make_prefix_for_netbox(prefix, tags=my_tags)
    if debug:
        print(payload)
    try:
        req = requests.post(url, headers=_headers, data=payload)
        if debug:
            print(req.status_code)
            print(req.json())

        if req.status_code != 201:
            print("Status Code: " + str(req.status_code) + ". Exiting now.\n")

    except Exception as err:
        print_error_msg(err)

if debug:
    # Retrieve prefixes with the same tags that we've created
    try:
        prefixes_by_tag_url = url + "?tag={}".format(lab_tag)
        req2 = requests.get(prefixes_by_tag_url, headers=_headers)
        print(req2.status_code)
        print(req2.json())

    except Exception as err:
        print_error_msg(err)
