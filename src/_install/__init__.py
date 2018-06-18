#!/usr/bin/env python3
#--*-- coding: utf-8 --*--


"""
install functions
"""


# import 

import os, time
from src._var import *


# functions

def write_bashrc(txt=" ") : 

	cmd = """echo "{}" >> /home/ethos/.bashrc """.format(txt)
	os.system(cmd)


def counter(k=4) : 

	time.sleep(1)
	print("")
	for i in range(k, 0, -1) : 
		print(str(i-1), end=" --> ")
		time.sleep(1)


def prepare_system(folder = "/home/ethos/ethOS-update-manager/src/var/"): 
	"""prepare system"""

	os.system("clear")
	os.system("cd /home/ethos/")

	try : 
		os.system("mkdir {}".format(folder))
	except : 
		print("BE SURE FILES ALREADY EXISTS")

	try : 
		FILES = 	[	"SLEEPER", "LAP_STAMP", "MIN_HASH", "JET_LAG", "LATENCY", 
					"TELEGRAM_MODE", "TOKEN", "CHAT_ID", "RIG", "AUTO_REBOOT"]
	
		for filename in FILES :
			os.system("touch {}{}".format(folder, filename))
	except : 
		print("BE SURE FILES ALREADY EXISTS")

	os.system("chmod +x /home/ethos/ethOS-update-manager/launch.py")
	os.system("chmod +x /home/ethos/ethOS-update-manager/src/main.py")


def write_title():
	"""title in .bashrc"""

	write_bashrc() #  empty line
	write_bashrc()
	write_bashrc("###################################")
	write_bashrc("#      ethOS-update-manager        ")
	write_bashrc("###################################")
	write_bashrc()
	write_bashrc()


def main_title():
	"""print title and intro for install manualy"""

	os.system("clear")
	print() #  empty line
	print()
	print("###################################")
	print("#      ethOS-update-manager        ")
	print("###################################")
	print()
	print()
	print("      	Install mode")
	print("###################################")
	print()
	print()
	print(	"Welcome in ethOS-update-manager v0.5\n"
			"we are going to help you in this awsome experience\n"
			"but first thing first : \n")
	print()
	print("please type <Enter> to continue...")
	print()


def system_var_title() : 
	"""" """
	os.system("clear")
	print()
	print()
	print("       Set system variables ")
	print("###################################")
	print()
	print()
			
	print(	"We are settings first all system variables\n"
			"You will have to set SLEEPER, LAP_STAMP, MIN_HASH, AUTO_REBOOT\n"
			"JET_LAG and LATENCY\n"
			"everything will be explained, let you drive\n")
	print()
	print()

def telegram_var_title() : 
	""" """

	os.system("clear")
	print()
	print()
	print("       Set telegram variables ")
	print("###################################")
	print()
	print()
			
	print(	"We are settings first all telegram variables\n"
			"You will have to set TELEGRAM_MODE, TOKEN, CHAT_ID and RIG\n"
			"everything will be explained, let you drive\n")
	print()
	print()


def write_alias() : 
	"""create alias (shortcup for CLI) 'LAUNCH' to launch program manualy"""

	write_bashrc("# create alias (shortcup for CLI) LAUNCH to launch program manualy :")
	write_bashrc("alias LAUNCH='python3 /home/ethos/ethOS-update-manager/launch.py'")

	write_bashrc()
	write_bashrc()


def write_autolaunch() : 
	"""for automatic program launch (background) at each ethos stratup"""

	write_bashrc("# for automatic program launch (background) at each ethos stratup:")
	write_bashrc("python3 /home/ethos/ethOS-update-manager/launch.py")

	write_bashrc()
	write_bashrc()


def reboot() : 
	"""auto reboot"""

	os.system("clear")
	print()
	print()
	# info reboot
	print(	"\n\n"
			"######################################################\n"
			"######################################################\n\n\n"
			"-->  your program is now installed & functional   <--\n\n\n"
			"-->  for full install, system will reboot in 3s   <--\n\n\n"
			"######################################################\n"
			"######################################################\n"
			"\n\n")

	counter(4)

	# do reboot
	ans = os.system("r")
	if ans : 
		ans = os.system("reboot")
		if ans : 
			ans = os.system("sudo reboot")
			if ans : 
				print(	"\n\n"
						"##################################################\n"
						"##################################################\n\n\n"
						"-->  auto reboot fail : please reboot manualy  <--\n\n\n"
						"##################################################\n"
						"##################################################\n"
						"\n\n")


