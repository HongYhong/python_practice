import subprocess

print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\nbilibili.com\nexit\n')
print(output.decode('utf-8','ignore'))
print('Exit code:', p.returncode)