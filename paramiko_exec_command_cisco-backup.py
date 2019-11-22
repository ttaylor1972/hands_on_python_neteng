import myparamiko


ssh_client = myparamiko.connect('172.16.32.199', 22, 'lab99', 'lab123')
remote_connection = myparamiko.get_shell(ssh_client)
myparamiko.send_command(remote_connection, 'terminal length 0')
output = myparamiko.send_command(remote_connection,'show run')

output_str = output.decode()
print(output_str)

list = output_str.split('\n')
list = list[4:-1]
config = '\n'.join(list)
#print(config)

with open('Router1-running-sample_ios_sh_run_output.txt', 'w') as f:
    f.write(config)

myparamiko.close(ssh_client)
