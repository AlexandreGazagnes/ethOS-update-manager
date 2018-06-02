#!/usr/bin/env python3
# -*- coding: utf-8 -*-


########################################################
########################################################
#		ethOsUpdateManager_v0.2.1
########################################################
########################################################



# import 

import os, subprocess, pickle, time

from logging import debug, warning, info
import logging
logging.basicConfig(level=logging.INFO)

# please do not use pandas on ethos 1.3.1

from lib.filepaths import * 
from lib.params import * 
from lib.files import * 
from lib.data import * 
from lib.text import * 


# Custom file paths

# feel free to uncomment and to change file paths, 
# if not default file paths will be used
# more info in lib/filepaths

		# DATA_FOLDER = "/home.ethos/
		# DATA_FILE = "update.csv" # feel free to give your personal config

		# COUNTER_FILE = ".counter" # you should not change this file
		# TEMP_FILE = "update.temp" # you should not change this file



# Custom Parametres

# feel free to uncomment and to change file paths, 
# if not default file paths will be used
# more info in lib/consts


logging.basicConfig(level=logging.INFO)

		# CMD = "show stats" # or update


SLEEPER = 5  # 5 minutes


		# KEYS_SELECTED= [# global :
		# 				'uptime','miner_secs', 					# time
		# 				'miner_version','version',				# ethos
		# 				'hostname','ip',   						# id 
		# 				'cpu_temp','gpus','hash','proxy_problem'#status and perf 

		# 				# for each GPU : 
		# 				'miner_hashes','rejected_shares',		# perf
		# 				'fanrpm','fanpercent','temp',			# temp
		# 				'bioses',								# id 
		# 				'core','mem','voltage',					# local config
		# 				'watts',								# conso 
		# 				'powertune']							# DEPRICIATED


		# HEADER = 		[ # global
		# 				'timestamp', 'uptime','miner_secs','miner_version','version',				# ethos
		# 				'hostname','ip', 'cpu_temp','gpus', 'working_gpus',
		# 				'hash','proxy_problem',
		# 				# for each GPU : 
		# 				'miner_hashes','rejected_shares',
		# 				'fanrpm','fanpercent','temp', 'temp_avg', 'temp_max',		
		# 				'bioses','core','mem','voltage', 'watts', 'powertune']



# Main

def main() : 


	# if data file do not exist : 
	init_data_file(DATA_FOLDER, DATA_FILE)


	# main loop
	while True : 

		# just ... sleep!
		time.sleep(SLEEPER) # to avoid multiple short reboot, options 

		# DEPRECIATED : (just for local test)
		txt = load_data(DATA_FOLDER+TEMP_FILE)
		
		# proceed 
		# txt = data_from_cmd() 			# extract text
		data = convert_txt(txt)				# extract data from text				
		data = extract_data(data) 			# build data dict of int or str 
		txt = convert_organized_txt(data) 	# rebuild txt for write

		# append file
		update_data_file(DATA_FOLDER, DATA_FILE, txt)


if __name__ == '__main__':
	main()


