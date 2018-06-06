#!/usr/bin/env python3
#--*-- coding: utf-8 --*--



# import 

import argparse, os

from logging import debug, warning, info
import logging

from _var_manager import *
from confs.filepaths import *



# functions

def auto_launch(option) : 
	""" """
	
	if option.lower() == "on" :
		var_manager("autolaunch_aut.pk", "w", 1)
		restart()

	elif option.lower() == "off" :
		var_manager("autolaunch_aut.pk", "w", 0)
		restart()

	elif otion == "show" :
		ans = var_manager("autolaunch_aut.pk", "r")

		if ans  : 
			print("auto launch : On")
		else : 
			print("auto launch : Off")
	else : 
		error()


def start(option, force=False) : 
	""" """

	if not is_working() : 

		if option.lower() == "fg" :
			os.system("/home/ethos/ethOS-update-manager/src/updater.py")

		elif option.lower() == "bg" :
			os.system("/home/ethos/ethOS-update-manager/autolaunch-updater")
	else : 
		print("program already running, please type 'Yes' to force an other start")
		ans = input()

		if ans == "Yes" : 
			start()


def stop() : 
	""" """

	res = os.popen("ps aux | grep ethOS-update-manager").readlines()
	l = -1
	for i, lign in enumerate(res) : 
		if "/home/ethos/ethOS-update-manager" in lign : 
			l= i 

	if l == -1 : 
		print("Sorry program not started")
	else : 
		li = res[l].split(" ")
		li = [i for i in li if li]
		pid = li[1]

		s = 'kill ' + str(pid)
		os.system(s)


def restart() : 
	""" """
	
	stop()
	start("bg")


def config(option) : 
	""" """

	if option.lower() == "set" :
		print("Not avialable")
		restart()

	elif option.lower() == "reset" : 
		print("Not avialable")
		restart()
	elif option.lower() == "show" :
		print("Not avialable")
	
	else : 
		error()


def reboot_aut(option) : 
	""" """
	
	if option.lower() == "on" : 
		var_manager("reboot_aut.pk", "w", 1)
		restart()

	elif option.lower() == "off" : 
		var_manager("reboot_aut.pk", "w", 0)
		restart()
	
	elif otion == "show" :
		ans = var_manager("reboot_aut.pk", "r")
	
		if ans  : 
			print("reboot aut : On")
		else  : 
			print("reboot aut  : Off")
		else : 
			raise ValueError("auto_launch error")
	else : 
		error()


def merge_files() : 
	""" """

	print("Not avialable") 
	# os.system(/home/ethos/ethOS-update-manager/utils/merge-files.py)



def is_working() : 
	""" """
	res = os.popen("ps aux | grep ethOS-update-manager").readlines()
	for lign in res : 
		if "/home/ethos/ethOS-update-manager" in lign : 
			print("program is working")
			return True

	print("program is not working")
	return False



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

	print("Command/Option. error")
	print("Do you want to acces to the Manual (full doc of instructions?")
	ans = input("y/n\n")
	if ans.lower() == "y" : 
		man()


def man(): 
	""" """

	txt = var_manager("doc.txt", "r", folder=DOC_FOLDER)
	print(txt)


def help(): 
	""" """

	man()

