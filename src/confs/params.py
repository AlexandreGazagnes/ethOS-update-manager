#!/usr/bin/env python3
# -*- coding: utf-8 -*-




# constants

CMD = "show stats" # or update


SLEEPER = 10 * 60 # 10 minutes
OVER_WARMING_SLEEPER = 60 * 60 # 1 hour
MAX_TEMP = 75

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


HEADER = 		[ # global
				'timestamp', 'session_number','uptime','miner_secs','miner_version','version',				
				'hostname','ip', 'cpu_temp','gpus', 'working_gpus',
				'hash','proxy_problem',
			# for each GPU : 
				'miner_hashes','rejected_shares',
				'fanrpm','fanpercent','temp', 'temp_avg', 'temp_max',		
				'bioses','core','mem','voltage', 'watts', 'powertune']


