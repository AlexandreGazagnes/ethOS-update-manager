#!/usr/bin/env python3
# -*- coding: utf-8 -*-



# import 

import os, subprocess, pickle, time

# do not use pandas on ethos 1.3.1

from confs.params import * 
from confs.filepaths import * 




# functions


def init_data_file(folder, datafile, counterfile=COUNTER_FILE, header=HEADER) : 

	info("init_data_file called")

	# build header, name and ext
	header = ",".join(header) + "\n"
	name, ext = datafile.split(".")
	
	debug(header)
	debug(name)
	debug(ext)

	# if first launch
	if counterfile not in os.listdir(folder) : 
	
		info("first launch--> initiate .counter and update0.csv")
		
		c = "0" # intiate counter
	
		debug(c)

		# create counter file
		with open(folder+counterfile, "w") as f :  f.write(c)

		filename = name + c + "." + ext # build filename
	
		debug(filename)

		# create file with header
		with open(folder+filename, "w") as f : f.write(header)

	# build filename 
	info("not first launch - > check headers")
	
	with open(folder+counterfile, "r") as f : c = f.read()
	filename = name + c + "." + ext
	
	debug(filename)

	# extract first lign and avoid  to read the entire file :)
	f = "head -n 1 " + str(folder+filename)
	f = os.popen(f)
	txt = str()
	for i in f :
		txt+=i
	
	debug(txt)

	# if header has changed, change filename
	if txt != header :
	
		info("Wrong headers, new file created")

		# update c and counter
		with open(folder+counterfile, "r") as f : c = f.read()
		c = str(1+int(c)) 
	
		debug(c)
	
		with open(folder+counterfile, "w") as f :  f.write(c)

		# build new filename and crete new file with new headers 
		filename = name + c + "." + ext
	
		debug(filename)
	
		with open(folder+filename, "w") as f : 
			f.write(header)


def update_data_file(folder, datafile, txt, counterfile=COUNTER_FILE) : 

	info("update_data_file called")
	
	name, ext = datafile.split(".")
	
	debug(name)
	debug(ext)

	# update c and counter
	with open(folder+counterfile, "r") as f : c = f.read()
	filename = name + c + "." + ext
	
	debug(filename)

	# save in file
	with open(folder+filename, "a") as f : 
		f.write(txt)
