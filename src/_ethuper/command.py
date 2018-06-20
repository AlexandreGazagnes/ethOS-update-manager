#!/usr/bin/env python3
#--*-- coding: utf-8 --*--


"""
ethuper : command functions
"""


# import 

import argparse, os, sys
from src._var import * 


# functions

def auto_launch(option) : 
	""" """
	
	if option.lower() == "on" :
		var_manager("AUTO_LAUNCH", "wb", 1)

	elif option.lower() == "off" :
		var_manager("AUTO_LAUNCH", "wb", 0)

	elif otion == "show" :
		ans = var_manager("AUTO_LAUNCH", "rb")

		if ans  : 
			print("auto launch : On")
		else : 
			print("auto launch : Off")
	else : 
		error()


def auto_reboot(option) : 
	""" """
	
	if option.lower() == "on" :
		var_manager("AUTO_REBOOT", "wb", 1)

	elif option.lower() == "off" :
		var_manager("AUTO_REBOOT", "wb", 0)

	elif otion == "show" :
		ans = var_manager("AUTO_REBOOT", "rb")

		if ans  : 
			print("auto launch : On")
		else : 
			print("auto launch : Off")
	else : 
		error()


def start(option) : 
	""" """

	if not is_working() : 

		if option.lower() == "fg" :
			os.system("python3 /home/ethos/ethOS-update-manager/src/main.py")

		elif option.lower() == "bg" :
			os.system("python3 /home/ethos/ethOS-update-manager/launch.py")
	else : 
		print("program already running, please type 'Yes' to force an other start")
		ans = input()

		if ans == "Yes" : 
			start()


def stop() : 
	""" """

	res = os.popen("ps aux | grep ethOS-update-manager").readlines()
	l = [i for i in res if "main.py" in i ]

	if len(l) : 
		print("Sorry program not started")
	else : 
		for i in l : 
			print(i)

	pids = [ i.split(" ")[1] for i in l]

	[os.system("kill " + str(i)) for i in pids]


def restart() : 
	""" """
	
	stop()
	start("bg")


def config(option) : 
	""" """

	if option.lower() == "set" :
		set_system_var()
		set_id_var()
		set_telegram_var()
		restart()

	elif option.lower() == "show" :
		var_read()
	
	else : 
		error()


def merge_files() : 
	""" """

	print("Not avialable") 
	# os.system(/home/ethos/ethOS-update-manager/utils/merge-files.py)


def is_working() : 
	""" """

	res = os.popen("ps aux | grep ethOS-update-manager").readlines()
	l = [i for i in res if "main.py" in i ]

	if len(l) : 
		print("Sorry program not started")
		return False
	else : 
		for i in l : 
			print(i)
		return True


def unistall(option) :
	""" """ 

	if option.lower() == "hard" : 
		print("Not avialable")
	
	elif option.lower() == "medium" : 
		print("Not avialable")
	
	elif option.lower() == "soft" :
		print("Not avialable")
	
	else : 
		error()


def error() : 
	""" """

	print("Command/Option error")
	print("Do you want to acces to the Manual (full doc of instructions?")

	while True : 
		ans = input("y/n\n")
		if ans.lower() == "y" : 
			man()
			return True 
		
		elif ans.lower() == "n"  : 
			return True 

		else : 
			print("y or n")


def man(): 
	""" """

	txt = var_manager("doc.txt", "rb", folder=DOC_FOLDER)
	print(txt)


def help(): 
	""" """

	man()

