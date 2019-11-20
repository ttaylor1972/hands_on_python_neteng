from napalm import get_network_driver
import json

driver = get_network_driver('ios')
optional_args = {'secret': 'ivoxy123'} #cisco is the enable password
ios = driver('192.168.122.212', 'ivoxy', 'ivoxy123', optional_args=optional_args)
ios.open()
#start your code

output = ios.get_arp_table()
# for item in output:
#     print(item)


dump = json.dumps(output, sort_keys=True, indent=4)
#print(dump)

with open('arp.txt', 'w') as f:
    f.write(dump)

#end your code
ios.close()