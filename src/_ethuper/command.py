#!/usr/bin/env python3
#--*-- coding: utf-8 --*--



# import 

import argparse, os

from logging import debug, warning, info
import logging



# functions

def auto_launch(option) : 
	""" """
	if option == "on" :
		with open("/home/ethos/ethOS-update-manager/src/var/autolaunch.pk", "w") as f : f.write("1")
	elif option == "off" :
		with open("/home/ethos/ethOS-update-manager/src/var/autolaunch.pk", "w") as f : f.write("1")
	else : 
		error()


def start(option) : 
	""" """

	if option == "fg" :
		# IF updater not WORKING !!!!
		os.system("nohup /home/ethos/ethOS-update-manager/src/updater.py")
	elif option == "bg" :
		# IF updater not WORKING !!!!
		os.system("/home/ethos/ethOS-update-manager/autolaunch-updater")
	else : 
		error()


def return_pids(cmd) : 
	""" """

	txt = "ps aux | grep {}".format(cmd)
	ans = os.popen().readlines()
	strip = [i.split(" ") for i in ans]
	strip = [[ i for i in j if i ] for j in strip]
	pids = [int(i[1]) for i in strip]

	return pids


def stop() : 
	""" """

	pids = return_pids("ethOS-update-manager") 
	for pid in pids  : 
		s = 'kill ' + str(pid)
		os.system("kill")


def restart() : 
	""" """
	
	stop()
	start("bg")


def config(option) : 
	""" """
	if option == "set" :
		print("Not avialable")
	elif option == "reset" :
		print("Not avialable")
	elif option == "show" :
		print("Not avialable")
	else : 
		error()


def reboot_aut(option) : 
	""" """
	
	if option == "on" : 
		with open("./var/reboot_aut.pk", "w") as f : f.write("1")
		restart()
	elif option == "off" : 
		with open("./var/reboot_aut.pk", "w") as f : f.write("0")
		restart()
	else : 
		error()


def merge_files() : 
	""" """
	print("Not avialable") 
	# os.system(/home/ethos/ethOS-update-manager/utils/merge-files.py)


def unistall(option) :
	""" """ 
	if option == "hard" : 
		print("Not avialable")
	elif option == "medium" : 
		print("Not avialable")
	elif option == "soft" :
		print("Not avialable")
	else : 
		error()


def error() : 
	""" """

	print("Command/Option error")
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

