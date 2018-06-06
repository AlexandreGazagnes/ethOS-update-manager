#!/usr/bin/env python3
#--*-- coding: utf-8 --*--



# import 

import argparse, os

from logging import debug, warning, info
import logging



# functions

def auto_launch(option) : 
	""" """
	
	if option.lower() == "on" :
		with open("/home/ethos/ethOS-update-manager/src/var/autolaunch.pk", "w") as f : f.write("1")
		restart()
	elif option.lower() == "off" :
		with open("/home/ethos/ethOS-update-manager/src/var/autolaunch.pk", "w") as f : f.write("0")
		# restart()
	elif otion == "show" :
		with open("/home/ethos/ethOS-update-manager/src/var/autolaunch.pk", "r") as f : ans = f.read()
		if ans == "1" : 
			print("auto launch : On")
		elif ans == "0" : 
			print("auto launch : Off")
		else : 
			raise ValueError("auto_launch error")
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
		# restart()
	elif option.lower() == "reset" : 
		print("Not avialable")
		# restart()
	elif option.lower() == "show" :
		print("Not avialable")
	else : 
		error()



def reboot_aut(option) : 
	""" """
	
	if option.lower() == "on" : 
		with open("/home/ethos/ethOS-update-manager/src/var/reboot_aut.pk", "w") as f : f.write("1")
		restart()
	elif option.lower() == "off" : 
		with open("/home/ethos/ethOS-update-manager/src/var/reboot_aut.pk", "w") as f : f.write("0")
		restart()
	elif otion == "show" :
		with open("/home/ethos/ethOS-update-manager/src/var/reboot_aut.pk", "r") as f : ans = f.read()
		if ans == "1" : 
			print("reboot aut : On")
		elif ans == "0" : 
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
	if ans.lower() == y : 
		man()


def man(): 
	""" """

	with open("/home/ethos/ethOS-update-manager/docs/manual.txt", "r") as f : 
		txt = f.read()
	print(txt)


def help(): 
	""" """

	man()

