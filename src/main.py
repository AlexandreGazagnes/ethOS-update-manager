#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
ethOS-update-manager - main - v0.5.0 

Handle results from a CMD 'show stats' or  and reboot 
if nedeed, ie your hashrate is too low (aka MIN_HASH).

Manage bot telegram and send warning msg to your personnal bot 
if you don't want this feature, please just set TELEGRAM_MODE = False/0

Please update with your personal settings : SLEEPER, JET_LAG, LATENCY 
and MIN_HASH. You can of course use default settings

if TELERAM_MODE set to True, you will have to set TOKEN, CHAT_ID, and RIG ame
"""


# logging

import logging

logging.basicConfig(	level=logging.INFO, 
						format='%(levelname)s %(message)s')


# import 
from _main import * 
from _var import * 


# main

def main() : 

	debug("main")

	# read var
	USER, INT_IP, EXT_IP = load_id_var()
	TELEGRAM_MODE, TOKEN, CHAT_ID, RIG = load_telegram_var()
	SLEEPER, LAP_STAMP, AUTO_REBOOT, AUTO_LAUNCH, HASH_MODE, MIN_HASH, \
		TEMP_MODE, MAX_TEMP, JET_LAG, LATENCY, LOGGING_LEVEL = load_system_var()


	# if not AUTO_LAUNCH stop the program
	if not AUTO_LAUNCH : 
		return 0

	# init logging
	logging.warning("\n\n\n")
	warning("init new session")

	# to avoid multiple short reboot 
	time.sleep(SLEEPER)
	
	if LATENCY and (SLEEPER < (60 * 6)) :  
		time.sleep(600 - SLEEPER)

	# init lap
	lap = 0


	# main loop
	while True :

		debug("main loop entrance") 

		# update var
		USER, INT_IP, EXT_IP = load_id_var()
		TELEGRAM_MODE, TOKEN, CHAT_ID, RIG = load_telegram_var()
	 	SLEEPER, LAP_STAMP, AUTO_REBOOT, AUTO_LAUNCH, HASH_MODE, MIN_HASH, \
			TEMP_MODE, MAX_TEMP, JET_LAG, LATENCY, LOGGING_LEVEL = load_system_var()
			
		# proceed 
		data = data_from_cmd() 	# extract data from cmd 
		hashrate = return_hash(data)

		# reboot option
		if (isinstance(hashrate, float) or isinstance(hashrate, int)) : 
			
			if hashrate < MIN_HASH : 
				
				if AUTO_REBOOT : 
					warning("rebooting due to hashrate {}\n auto reboot mode enabled\n".format(hashrate))
					reboot()
				
				else : 
					warning("hashrate problem {}\n auto reboot mode disabled".format(hashrate))

			else : 
				debug("hashrate OK")
				
				if not lap % LAP_STAMP : 
					warning("everything is fine, hashrate {}\n".format(hashrate))

		else : 
			warning("invalid hashrate type {}\n".format(type(hashrate)))

		# wait and lap
		time.sleep(SLEEPER) # to avoid multiple short reboot 
		lap +=1


if __name__ == '__main__':
	main()

