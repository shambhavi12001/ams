import paramiko
from scp import SCPClient
import time
# declare credentials
host = 'ams-pi.local'
username = 'pi'
password = 'ece498ams'
# connect to server
con = paramiko.SSHClient()
con.load_system_host_keys()
con.connect(host, username=username, password=password)
with SCPClient(con.get_transport()) as scp:
    scp.put('GSM_PWRKEY.py', '~/')
# execute the script
stdin, stdout, stderr = con.exec_command('python3 GSM_PWRKEY.py')
if stderr.read() == b'':
    print('Started SIM Module successfully')
else:
    print('An error occurred')

stdin, stdout, stderr = con.exec_command('echo $(date) >> status.txt; vcgencmd measure_temp >> status.txt; free >> status.txt; uptime >> status.txt')
if stderr.read() == b'':
    print('Recorded')
    scp.get('status.txt')
else:
    print('An error occurred')

con.close()
time.sleep(5)
