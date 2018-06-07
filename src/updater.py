#!/usr/bin/env python3
# -*- coding: utf-8 -*-



# import 

import logging

from _var_manager import *
from confs.filepaths import * 

# reading and setting auto log level
lev = var_manager("log_level.pk", "r", folder=VAR_FOLDER)	
logging.basicConfig(level=lev)

from confs.params import * 
from _updater.file import * 
from _updater.data import * 
from _updater.text import * 
from _updater.install import *
from _updater.manage import *



# main

def main(test_mode=False) :

	# if autolaunch mode enabled or not
	autolaunch = var_manager("autolaunch_aut.pk", "r")
	logging.debug(autolaunch)

	if autolaunch : 

		# handle install if needed 		
		install()
		logging.debug("install")

		# reset pb counters 
		var_manager("consecutive_problem.pk", "w", 0)
		var_manager("reboot_number.pk", "i")
		logging.debug("reset system counters")
		
		# file manager
		init_data_file(DATA_FOLDER, DATA_FILE)
		logging.debug("init data file")

		# main loop
		while True : 

			# just ... sleep!
			time.sleep(SLEEPER) # to avoid multiple short reboot 
			
			# proceed 
			if not test_mode : 
				txt = data_from_cmd()				# extract text
			else : 
				txt = load_data("DATA_FOLDER", "update.temp") # JUST FOR TEST MODE 
			data = convert_txt(txt)				# extract data from text				
			data = extract_data(data) 			# build data dict of int or str 
			txt = convert_organized_txt(data) 	# rebuild txt for write
			logging.debug("command, text, data processing")

			# update/append file
			update_data_file(DATA_FOLDER, DATA_FILE, txt)
			logging.debug("update data file")

			# if reboot mode enabled or not
			reboot_aut = var_manager("reboot_aut.pk", "r")
			logging.debug(reboot_aut)

			if reboot_aut : 
				check_and_reboot(data)
				loging.debug("check and reboot")



if __name__ == '__main__':
	main()


