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

query_param = "lab50"
prefixes_by_tag_url = url + "?tag={}".format(query_param)

try:
    req = requests.get(prefixes_by_tag_url, headers=_headers)
    if debug:
        print(req.status_code)
        print(req.json())

except Exception as err:
    print_error_msg(err)
