#!/usr/bin/env python3
# -*- coding: utf-8 -*-



# import 

import logging

from _var_manager import *
from confs.filepaths import * 

# reading and setting auto log level
if not lev : 
	lev = var_manager("log_level.pk", "r")	
	logging.basicConfig(level=lev)
else :
	logging.basicConfig(level=lev)

from confs.params import * 
from _updater.file import * 
from _updater.data import * 
from _updater.text import * 
from _updater.install import *
from _updater.manage import *



# main

def main(test_mode=False, lev=None) :

	# if autolaunch mode enabled or not
	msg = "time = {} NEW SESSION\n\n\n".format(str(int(time.time())))
	logging.info(msg)

	logging.info("read autolaunch_aut")

	autolaunch = var_manager("autolaunch_aut.pk", "r")
	
	logging.debug(autolaunch)

	if autolaunch : 

		logging.info("autolaunch enabled")

		# handle install if needed 		
		install()

		# reset pb counters 
		logging.info("(re)set system counters")
		var_manager("consecutive_problem.pk", "w", 0)
		var_manager("session_number.pk", "i")
		
		# file manager
		init_data_file(DATA_FOLDER, DATA_FILE)

		logging.info("main loop")
		# main loop
		while True : 

			logging.info("sleeper")
			# just ... sleep!
			time.sleep(SLEEPER) # to avoid multiple short reboot 
			
			# log process 
			logging.info("log process")
			if not test_mode : 
				txt = data_from_cmd()				# extract text
			elif test_mode == "temp" : 
				txt = load_temp_file(DATA_FOLDER, TEMP_FILE) # just for test 
			elif test_mode = "fake_cmd" : 
				txt = load_fake_cmd()
			
			data = convert_txt(txt)				# extract data from text				
			data = extract_data(data) 			# build data dict of int or str 
			txt = convert_organized_txt(data) 	# rebuild txt for write
			
			# update/append file
			update_data_file(DATA_FOLDER, DATA_FILE, txt)

			# if reboot mode enabled or not
			logging.info("read reboot_aut")
			reboot_aut = var_manager("reboot_aut.pk", "r")
			logging.debug(reboot_aut)

			if reboot_aut : 
				check_and_reboot(data)



if __name__ == '__main__':
	main()


