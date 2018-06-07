#!/usr/bin/env python3
# -*- coding: utf-8 -*-



# import 

import os, subprocess, pickle, time, logging
from logging import debug, warning, info

from confs.params import * 
from confs.filepaths import *
from _var_manager import *




# functions

def init_data_file(folder=DATA_FOLDER, datafile=DATA_FILE, counterfile=COUNTER_FILE, header=HEADER) : 
	""" """

	logging.info("init_data_file called")

	# build header, name and ext
	header = ",".join(HEADER) + "\n"
	name, ext = datafile.split(".")
	
	logging.debug(header)
	logging.debug(name)
	logging.debug(ext)

	# if first launch
	if counterfile not in os.listdir(folder) : 
	
		logging.info("first launch--> initiate .counter and update0.csv")
		
		c = "0" # intiate counter
	
		logging.debug(c)

		# create counter file
		var_manager(counterfile, "w", c, folder)

		# build filename
		filename = name + c + "." + ext 
	
		logging.debug(filename)

		# create file with header
		var_manager(filename, "w", header, folder)

	# build filename 
	logging.info("not first launch - > check headers")
	
	c = var_manager(counterfile, "r", folder=folder) 

	filename = name + str(c) + "." + ext
	
	logging.debug(filename)

	# extract first lign and avoid  to read the entire file :)
	f = "head -n 1 " + str(folder+filename)
	f = os.popen(f)
	txt = str()
	for i in f :
		txt+=i
	
	logging.debug(txt)

	# if header has changed, change filename
	if txt != header :
	
		logging.info("Wrong headers, new file created")

		# update c and counter
		c = var_manager(counterfile, "r", folder=folder)
		var_manager(counterfile, "i", folder=folder)

		c = str(1+int(c)) 
	
		logging.debug(c)
	
		# build new filename and crete new file with new headers 
		filename = name + c + "." + ext
	
		logging.debug(filename)
	
		var_manager(filename, "w", header, folder=folder)


def update_data_file(folder=DATA_FOLDER, datafile=DATA_FILE, txt=None, counterfile=COUNTER_FILE) : 
	""" """
	
	logging.info("update_data_file called")
	
	name, ext = datafile.split(".")
	
	logging.debug(name)
	logging.debug(ext)

	# update c and counter
	var_manager(counterfile, "r", folder=folder)
	filename = name + str(c) + "." + ext
	
	logging.debug(filename)

	# save in file
	with open(folder+filename, "a") as f : 
		f.write(txt)

