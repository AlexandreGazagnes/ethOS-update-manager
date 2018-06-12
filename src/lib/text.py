#!/usr/bin/env python3
# -*- coding: utf-8 -*-



# import

import os, subprocess, pickle, time
from logging import debug, warning, info

# do not use pandas on ethos 1.3.1

from lib.params import * 
from lib.filepaths import * 



# functions

def data_from_cmd(cmd="show stats") :
	"""create a txt from a popen command, for ex "update" """ 

	info("data_from_cmd called")

	wrap = os.popen(cmd)
	txt = str()

	for i in wrap : 
		txt +=i

	if not txt : 

		info("txt is None")

	return txt


def load_data(filename) : 
	"""load data from file"""

	info("load_data called")
	
	with open(filename, "r") as f : 
		txt = f.read()
	subtxt = txt[:300]
	
	info(subtxt)

	return txt


def convert_txt(txt):
	"""from the str version of cli "update", create and return a list of
	key, values"""

	info("convert_txt called")

	# fist split lines
	li1 = txt.splitlines()

	# separate key, value with ":"
	li2 = [i.split(":") for i in li1]

	# delete null values
	li2 = [i for i in li2 if i[0]]

	# info some key values encoded on sevral lines
	li3 = [["None", i[0]] if len(i) == 1 else i for i in li2]

	# strip everything
	li3 = [[i[0].strip(), i[1].strip()] for i in li3]
	
	debug(li3)

	return li3


def convert_organized_txt(data, header=HEADER) : 
	"""from dict and in a specific order, build text to record"""

	info("convert_organized_txt called")

	li = [str(data[i]) for i in header]

	debug(li)

	txt = ",".join(li)
	txt+="\n"

	debug(txt)

	return txt