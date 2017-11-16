import paramiko
import select

ip = raw_input("IP address of server: ")
print "Connecting to: "+ip+"..."

username = raw_input("Username: ")
password = raw_input("Password: ")
cmd_to_run = raw_input("Command to run: ")

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(ip, username=username, password=password)

stdin, stdout, stderr  = client.exec_command(cmd_to_run)

while not stdout.channel.exit_status_ready():
    # Only print data if there is data to read in the channel
    if stdout.channel.recv_ready():
        rl, wl, xl = select.select([stdout.channel], [], [], 0.0)
        if len(rl) > 0:
            # Print data from stdout
            print stdout.channel.recv(1024),

client.close()