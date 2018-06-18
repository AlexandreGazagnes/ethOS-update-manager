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


def prepare_system(): 
	"""prepare system"""

	os.system("clear")
	os.system("cd /home/ethos/")
	os.system("mkdir ethOS-update-manager/src/var/")

	FILES = 	[	"SLEEPER", "LAP_STAMP", "MIN_HASH", "JET_LAG", "LATENCY", 
					"TELEGRAM_MODE", "TOKEN", "CHAT_ID", "RIG"]
	
	for filename in : FILES
		os.system("touch ethOS-update-manager/src/var/{}".format(filename))

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


