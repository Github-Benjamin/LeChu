import paramiko

host = '118.113.202.xx'
port = '22'
username = 'root'
pawwword = 'root'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='118.113.202.xx', port=22, username='root', password='root')

stdin, stdout, stderr = ssh.exec_command('df -hl')

print(stdout.read().decode())
