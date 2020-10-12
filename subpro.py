import subprocess
# ret = subprocess.call(["ping","127.0.0.1","-c","3"])
# ret = subprocess.call(['ls','-l'])

# ret=subprocess.call(['python3','threads1.py'])
import platform

osType = platform.system()

print("OS:",osType)

if osType == 'Darwin':
    pass
elif osType == 'Windows':
    subprocess.call(['open','D:/hello.txt'])


print("Return code:",ret)