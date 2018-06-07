#!/usr/bin/env python3
#--*-- coding: utf-8 --*--



# import 

import os, time
from logging import debug, info, warning
import logging

from _var_manager import *


# fonctions

def autosettings() : 
	""" """

	print("enable autosettings ? y/n (DEFAULT and RECOMMANDED : y)")
	while True : 
		ans = input()

		if ans.lower() == "y" : 
			var_manager("autolaunch_aut.pk", "w", 1)
			var_manager("reboot_aut.pk", "w", 1)
			var_manager("sleeper.pk", "w", 300)
			return True

		elif ans.lower() == "n" :  
			return False

		else : 
			print("y or n")


def choose_autolaunch() : 
	""" """
	
	print("enable autolaunch ? y/n (DEFAULT and RECOMMANDED : y)")
	while True : 
		ans = input()

		if ans.lower() == "y" : 
			var_manager("autolaunch_aut.pk", "w", 1)
			return True

		elif ans.lower() == "n" :  
			var_manager("autolaunch_aut.pk", "w", 0)
			return True

		else : 
			print("y or n")


def choose_reboot_aut() : 
	""" """

	print("enable rebooting autorisation? y/n (DEFAULT and RECOMMANDED : y)")
	while True : 
		ans = input()

		if ans.lower() == "y" : 
			var_manager("reboot_aut.pk", "w", 1)
			return True

		elif ans.lower() == "n" :  
			var_manager("reboot_aut.pk", "w", 0)
			return True

		else : 
			print("y or n")


def choose_time_delta() : 
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
			var_manager("sleeper.pk", "w", t)
			return True
		else : 
			print("Min : 1, Max : 60")


def user_settings() : 
	""" """ 

	done = autosettings()

	if not done : 
		choose_autolaunch()
		choose_reboot_aut()
		choose_time_delta()




