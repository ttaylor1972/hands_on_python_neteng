import paramiko

ssh_client = paramiko.SSHClient()

ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect('172.16.32.199', port=22, username='lab99', password='lab123', look_for_keys=False, allow_agent=False)

stdin, stdout, stderr = ssh_client.exec_command('sh version')

output = stdout.read().decode()
print(output)

ssh_client.close()

with open('R1_show_version.txt', 'w') as f:
    f.write(output)
