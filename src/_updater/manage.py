#!/usr/bin/env python3
# -*- coding: utf-8 -*-



# import 

import os, subprocess, pickle, time

from logging import debug, warning, info

# do not use pandas on ethos 1.3.1

from confs.params import * 
from confs.filepaths import * 



# to remind : 

# HEADER = 		[ # global
# 				'timestamp', 'uptime','miner_secs','miner_version','version',				
# 				'hostname','ip', 'cpu_temp','gpus', 'working_gpus',
# 				'hash','proxy_problem',
# 			# for each GPU : 
# 				'miner_hashes','rejected_shares',
# 				'fanrpm','fanpercent','temp', 'temp_avg', 'temp_max',		
# 				'bioses','core','mem','voltage', 'watts', 'powertune']


# functions

def miner_not_started(data) : 
	"""if miner not started"""

	with open("./var/allow_minestart.pk", "r") as f : allow = int(f.read())

	# miner not mining
	if data["miner_hashes"] < 1 :

		# record  and first restart reallow
		if not allow : 

			logging.warning("Miner not started, allow and minestart")

			os.system("allow")
			os.system("minestart")

			with open("./var/allow_minestart.pk", "w") as f : f.write("1")

		# if already restarted and reallowe: reboot
		else : 

			logging.warning("Miner not working, but already re-allowed and re-started")

			with open("./var/allow_minestart.pk", "w") as f :
				 allow = f.write("0")
			os.system("r")


def miner_too_hot(data) : 
	"""if miner to hot""" 

	# if GPU temp to hot disallow and minestop
	if (data["temp_max"] > 75) or (data["temp_avg"] > 70) : 

		logging.warning("Critical problem, system disallow and minestop")

		os.system("disallow")
		os.system("minestop")
		
		logging.warning("Miner will wait before reboot")
		
		# wait to have lower temp
		time.sleep(60*30) 
		
		logging.warning("rebooting")
		
		os.system("r")


def miner_not_perf(data) : 
	"""if miner not perf """ 

	# if all GPU do not mine : reboot 
	if data['gpus'] > data['working_gpus'] : 

		logging.warning("Major problem, one or more GPU not working, reboot")
		
		os.system("r")

		### INTRODUCE HARD AND SOFT REBOOT 
		### FOR EXAMPLE IF 5 CONSECUTIVE REBBOT
		### SEND A MESSAGE FOR MANUAL INTERVENTION


def manage(data) :
	""" for each mining config apply good action"""

	logging.info("manage mode enable : checking if problems")

	miner_not_started(data)
	miner_to_hot(data)
	miner_not_perf(data)


