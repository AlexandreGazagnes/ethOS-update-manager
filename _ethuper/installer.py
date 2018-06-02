#!/usr/bin/env python3
#--*-- coding: utf-8 --*--


import os, time, pickle

# update install.pk
with open("/home/ethos/ethOS-update-manager/_ethuper/var/install.pk", "w") as f:
	f.write("True")
	
# prepare sys
os.system("cd")
os.system("chmod +x /home/ethos/ethOS-update-manager/launch")
os.system("chmod +x /home/ethos/ethOS-update-manager/_ethuper/main.py")


# create alias (shortcup for CLI) : 
os.system("""echo "alias --your_shortcut--='/home/ethos/ethOS-update-manager/launch'" >>  /home/ethos/.bashrc""")

# for automatic program launch (background) at each ethos stratup : 
os.system("echo '/home/ethos/ethOS-update-manager/launch' >> /home/ethos/.bashrc")


print("for full install, system will reboot in : ")
for i in range(2, 0, -1) : 
	print(str(i+1))
	time.sleep(1)

#auto reboot 
os.system("r")
