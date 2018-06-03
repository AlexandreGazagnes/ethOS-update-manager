#!/usr/bin/env python3
#--*-- coding: utf-8 --*--



# import 

import os, time
from logging import debug, info, warning
import logging



# fonctions

def prepare_sys() : 
	""" """

	os.system("cd")
	os.system("chmod +x /home/ethos/ethOS-update-manager/autolaunch-updater")
	os.system("chmod +x /home/ethos/ethOS-update-manager/ethuper")

	os.system("chmod +x /home/ethos/ethOS-update-manager/src/updater.py")
	os.system("chmod +x /home/ethos/ethOS-update-manager/src/ethuper.py")


def add_aliases() : 
	""" """
	os.system("""echo "alias ethuper='/home/ethos/ethOS-update-manager/ethuper'" >>  /home/ethos/.bashrc""")


def add_autolaunch() : 
	""" """
	os.system("echo '/home/ethos/ethOS-update-manager/autolaunch-updater' >> /home/ethos/.bashrc")


def reboot_install() : 
	""" """ 
	print("for full install, system will reboot in : ")
	for i in range(3, 0, -1) : 
		print(str(i))
		time.sleep(1)

	#auto reboot 
	v = os.system("r")
	
	# # if r do not work
	# if v :  
	# 	os.system("reboot")
	