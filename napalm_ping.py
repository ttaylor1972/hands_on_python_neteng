from napalm import get_network_driver
import json

driver = get_network_driver('ios')
optional_args = {'secret': 'ivoxy123'} #cisco is the enable password
ios = driver('192.168.122.212', 'ivoxy', 'ivoxy123')
ios.open()
#start your code


output = ios.ping(destination='9.9.9.9', count=20, source='192.168.122.212')
ping = json.dumps(output, sort_keys=True, indent=4)
print(ping)

#end your code
ios.close()
