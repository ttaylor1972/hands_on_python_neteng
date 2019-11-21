import requests
import json
from netbox_helpers import make_ip_address_for_netbox, print_error_msg

debug = True
port = 32768
base_url = "http://172.16.32.74:{}/api/".format(port)
prefix_path = "ipam/ip-addresses/"
url = base_url + prefix_path
netbox_api_token = "0123456789abcdef0123456789abcdef01234567"
_headers = {
    "Authorization": "Token {}".format(netbox_api_token),
    "Accept": "application/json",
    "Content-type": "application/json",
}
# list of tuples that have an IP and a list of tags
ip_list = [
    ("10.50.24.11/24", ["lab50", "snmp_server", "prod"]),
    ("10.50.24.12/24", ["lab50", "snmp_server", "prod"]),
    ("10.50.24.14/24", ["lab50", "snmp_server", "dev"]),
    ("10.50.24.22/24", ["lab50", "syslog_server", "prod"]),
    ("10.50.24.27/24", ["lab50", "syslog_server", "prod"]),
    ("10.50.24.29/24", ["lab50", "syslog_server", "dev"]),
    ("10.50.24.33/24", ["lab50", "radius_server", "prod"]),
    ("10.50.24.34/24", ["lab50", "radius_server", "prod"]),
    ("10.50.24.36/24", ["lab50", "radius_server", "dev"]),
]
if debug:
    print(_headers)
    print("API URL: {}".format(url))


for ip_tuple in ip_list:
    payload = make_ip_address_for_netbox(ip_tuple[0], tags=ip_tuple[1])

    if debug:
        print(payload)
    try:
        req = requests.post(url, headers=_headers, data=payload)
        if debug:
            print(req.status_code)
            print(req.json())

        if req.status_code != 201:
            print("Status Code: " + str(req.status_code) + ". skipping.\n")
    except Exception as err:
        print_error_msg(err)


# Find all the ip address with a particular tag
# to validate they were created
if debug:
    query_param = "dev"
    ip_addresses_by_tag_url = url + "?tag={}".format(query_param)
    try:
        req2 = requests.get(ip_addresses_by_tag_url, headers=_headers)
        if debug:
            print(req2.status_code)
            print(req2.json())
    except Exception as err:
        print_error_msg(err)
