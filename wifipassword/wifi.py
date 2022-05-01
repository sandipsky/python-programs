#importing required module
import subprocess
import os

print(os.name)
if os.name == 'nt':
    def getWifiNames():
        #variable to store output of command 'netsh wlan show profiles'
        meta_data = subprocess.check_output(['netsh','wlan','show','profiles'])

        #previous output to string format
        data = meta_data.decode("utf-8")
        #separating output by new line
        data = data.split("\n")

        #list to store wifi names
        names = []

        for line in data:
            #select the line with string all user profile
            if "All User Profile     :" in line:
                name = line.split(":")[1] #only stores second part
                names.append(name[1:-1]) #appends wifi name to list by removing spaces
        return names
    m = len(max(getWifiNames(),key=len))
    for name in getWifiNames():
        meta_data = subprocess.check_output(['netsh','wlan','show','profile', name, 'key=clear'])
        data = meta_data.decode("utf-8")
        data = data.split("\n")
        for line in data:
            if "Key Content" in line:
                password = line.split(":")[1]
        print(name.ljust(m), ":", password)
else:
    pass



    