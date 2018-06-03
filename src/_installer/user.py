#!/usr/bin/env python3
#--*-- coding: utf-8 --*--



# import 

import os, time
from logging import debug, info warning
import logging



# fonctions

def autosettings() : 
	""" """

	print("enable autosettings ? y/n")
	while True : 
		ans = input()

		if ans.lower() == "y" : 
			with open("./var/autolaunch.pk", "w") as f : f.write("1")
			with open("./var/reboot_aut.pk", "w") as f : f.write("1")
			with open("./var/sleeper.pk", "w") as f : f.write("300")
			return True

		elif ans.lower() == "n" :  
			return False

		else : 
			print("y or n")


def autolaunch() : 
	""" """
	
	print("enable autolaunch ? (DEFAULT and RECOMMANDED")
	while True : 
		ans = input()

		if ans.lower() == "y" : 
			with open("./var/autolaunch.pk", "w") as f : f.write("1")
			return True

		elif ans.lower() == "n" :  
			with open("./var/autolaunch.pk", "w") as f : f.write("0")
			return True

		else : 
			print("y or n")


def reboot_aut() : 
	""" """

	print("enable rebooting autorisation? (DEFAULT and RECOMMANDED)")
	while True : 
		ans = input()

		if ans.lower() == "y" : 
			with open("./var/reboot_aut.pk", "w") as f : f.write("1")
			return True

		elif ans.lower() == "n" :  
			with open("./var/reboot_aut.pk", "w") as f : f.write("0")
			return True

		else : 
			print("y or n")


def reboot_aut() : 
	""" """

	print("log time delta? in minutes (DEFAULT : 5)" )
	while True : 
		ans = input()

		try : 
			ans = int(ans)

		except : 
			print("Digit number please")
			continue

		if 60 >= ans >= 1 : 
			t = str(ans * 60)
			with open("./var/sleeper.pk", "w") as f : f.write(t)
			return True
		else : 
			print("Min 1, Max 60")


def user_settings() : 
	""" """ 
	
	done = autosettings()

	if not done : 
		autolaunch()
		reboot_aut()
		time_delta()




