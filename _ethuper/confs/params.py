#!/usr/bin/env python3
# -*- coding: utf-8 -*-



# import 

import os, subprocess, pickle, time

from logging import debug, warning, info
import logging

# do not use pandas on ethos 1.3.1



# log level

logging.basicConfig(level=logging.WARNING)



# constants

CMD = "show stats" # or update
debug(CMD)


SLEEPER = 60 * 5 # 5 minutes
debug(SLEEPER)


KEYS_SELECTED= [ # global :
				'uptime','miner_secs', 				# time
				'miner_version','version',			# ethos
				'hostname','ip',   				# id 
				'cpu_temp','gpus','hash','proxy_problem', 	#status and perf 
				
		# for each GPU : 
				'miner_hashes','rejected_shares',		# perf
				'fanrpm','fanpercent','temp',			# temp
				'bioses',					# id 
				'core','mem','voltage',				# local config
				'watts',					# conso 
				'powertune']					# DEPRICIATED
debug(KEYS_SELECTED)


HEADER = 		[ # global
				'timestamp', 'uptime','miner_secs','miner_version','version',				
				'hostname','ip', 'cpu_temp','gpus', 'working_gpus',
				'hash','proxy_problem',
			# for each GPU : 
				'miner_hashes','rejected_shares',
				'fanrpm','fanpercent','temp', 'temp_avg', 'temp_max',		
				'bioses','core','mem','voltage', 'watts', 'powertune']
debug(HEADER)
