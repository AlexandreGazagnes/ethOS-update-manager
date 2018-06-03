#!/usr/bin/env python3
# -*- coding: utf-8 -*-



# import 

import os, subprocess, pickle, time

from logging import debug, warning, info
import logging

# please do not use pandas on ethos 1.3.1

from confs.filepaths import * 
from confs.params import * 

from _updater.file import * 
from _updater.data import * 
from _updater.text import * 
from _updater.install import *
from _updater.manage import *



# main

def main() : 

	# def loggig level
	logging.basicConfig(level=logging.INFO)

	# handle install if needed 		
	install()
	
	# file manager
	init_data_file(DATA_FOLDER, DATA_FILE)


	# main loop
	while True : 

		# just ... sleep!
		time.sleep(SLEEPER) # to avoid multiple short reboot 
		
		# proceed 
		txt = data_from_cmd() 				# extract text
		data = convert_txt(txt)				# extract data from text				
		data = extract_data(data) 			# build data dict of int or str 
		txt = convert_organized_txt(data) 	# rebuild txt for write

		# update/append file
		update_data_file(DATA_FOLDER, DATA_FILE, txt)

		with("./var/reboot_aut.pk", "r") as f : reboot_aut = int(f.read())
		if reboot_aut : 
			manage(data)




if __name__ == '__main__':
	main()


