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

def main(fake_mode=False) : 

	debug("main")
	if fake_mode : logging.warning("simulation mode : handly enabled")

	# update vars
	update_all_var()
	
	# if not AUTO_LAUNCH stop the program
	if not AUTO_LAUNCH : return 0

	# init logging
	logging.warning("\n\n\n")
	warning("init new session\n")

	# to avoid multiple short reboot 
	time.sleep(SLEEPER)
	if LATENCY and (SLEEPER < (60 * 6)) : time.sleep(600 - SLEEPER)

	# init lap
	lap = 0

	# main loop
	while True :

		debug("main loop entrance") 

		# update vars
		update_all_var()

		# update ip
		update_ip_ext()

		# extract and enhance data 
		data = data_from_cmd(fake_mode=fake_mode)
		data = enhance_data(data)

		# update stats
		update_stats(data)

		# manage rig
		if HASH_MODE : 	manage_hashrate(return_hash(data), lap)
		if TEMP_MODE : 	manage_temp(return_temp(data), lap)

		# wait and lap
		time.sleep(SLEEPER)
		lap +=1


if __name__ == '__main__':
	main()
