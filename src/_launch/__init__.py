#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
launch functions
"""


# import 

import os, time, random


# functions

def randomize_start() : 
	"""add a random sleeper to avoid multi boot"""

	s = round(random.random() * 10 * 1, 1) 
	time.sleep(s)


def working_process() : 
	"""handle working processes"""

	process = os.popen("ps -aux | grep ethOS-update-manager").readlines()
	is_working = ["src/main.py" in p for p in process]

	return is_working


def launch_if_needed(is_working) : 
	""" """
	
	# if 1 process break
	if True in is_working :
		print("ethOS-update-manager already running")
		return 0
	
	# else launch one
	print("ethOS-update-manager launched")
	os.system("nohup python3 /home/ethos/ethOS-update-manager/src/main.py >> /home/ethos/ethOS-update-manager/logs/log 2>&1 &")
	return 0


def reset_fake_show_stats():
	""" """

	os.system("cp /home/ethos/ethOS-update-manager/.show_stats.save /home/ethos/ethOS-update-manager/.show_stats.txt")