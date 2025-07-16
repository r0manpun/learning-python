# connect to Linux server using SSH and execute commands

import paramiko

def ssh_execute_command(host, username, password, command):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=host, username=username, password=password)
    stdin, stdout, stderr = client.exec_command(command)
    output = stdout.read().decode()
    error = stderr.read().decode()
    client.close()
    return output, error
