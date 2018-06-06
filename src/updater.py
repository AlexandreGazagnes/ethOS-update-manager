#!/usr/bin/env python3
# -*- coding: utf-8 -*-



# import 

import os, subprocess, pickle, time

from logging import debug, warning, info
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

def main() :

	autolaunch = var_manager("autolaunch_aut.pk", "r") 

	if autolaunch : 

		# handle install if needed 		
		install()

		# reset pb counters 
		var_manager("consecutive_problem.pk", "w", 0,folder=VAR_FOLDER)
		var_manager("reboot_number.pk", "w", 0, folder=VAR_FOLDER)

		# test logging level
		logging.debug("test logging debug")
		logging.info("test logging info ")
		logging.warning("test logging warning ")
		
		# file manager
		init_data_file(DATA_FOLDER, DATA_FILE)

		# main loop
		while True : 

			# just ... sleep!
			time.sleep(SLEEPER) # to avoid multiple short reboot 
			
			# proceed 
			txt = data_from_cmd()				# extract text
			
			# test MODE 
			txt = load_data("/home/ethos/ethOS-update-manager/data/", "update.temp")

			data = convert_txt(txt)				# extract data from text				
			data = extract_data(data) 			# build data dict of int or str 
			txt = convert_organized_txt(data) 	# rebuild txt for write

			# update/append file
			update_data_file(DATA_FOLDER, DATA_FILE, txt)

			with open("/home/ethos/ethOS-update-manager/src/var/reboot_aut.pk", "r") as f : reboot_aut = int(f.read())
			logging.debug(reboot_aut)

			if reboot_aut : 
				manage(data)




if __name__ == '__main__':
	main()


