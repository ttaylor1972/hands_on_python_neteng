import json

# Helper function to make a prefix json object for netbox
def make_prefix_for_netbox(new_prefix, tags = []):
    null = None
    # Make a dictionary with the values I want
    payload = {
      "prefix": new_prefix,
      "site": null,
      "vrf": 1,
      "tenant": null,
      "vlan": null,
      "status": 1,
      "role": null,
      "is_pool": False,
      "description": "",
      "tags": tags,
      "custom_fields": {}
    }
    # Convert the dictionary into JSON
    json_payload = json.dumps(payload,indent=4, sort_keys=False)

    # return the JSON formatted data
    return json_payload

def make_ip_address_for_netbox(new_ip_address, tags = []):
    null = None
    # Make a dictionary with the values I want

    payload = {
      "address": new_ip_address,
      "vrf": 1,
      "tenant": null,
      "status": 1,
      "role": null,
      "interface": null,
      "nat_inside": null,
      "nat_outside": null,
      "dns_name": "",
      "description": "",
      "tags": tags,
      "custom_fields": {}
    }
    # Convert the dictionary into JSON
    json_payload = json.dumps(payload,indent=4, sort_keys=False)

    # return the JSON formatted data
    return json_payload

def print_error_msg(err = None):
    error_msg = """
    Encountered error launching an http(s) request.
    Please check your connectivity."""
    print(error_msg)
    if err:
        print(err)

def build_api_url(url = "172.16.32.74", port = 32768):
    return "http://{0}:{1}/api/".format(url, port)
