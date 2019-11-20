from napalm import get_network_driver

driver = get_network_driver('ios')

optional_args = {'secret': 'ivoxy123'} #cisco is the enable password
ios = driver('192.168.122.212', 'ivoxy', 'ivoxy123', optional_args=optional_args)
ios.open()

#show all methods available
print(dir(ios))

ios.close()
