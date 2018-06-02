#!/usr/bin/env python3
# -*- coding: utf-8 -*-



# import 

import os, subprocess, pickle, time

from logging import debug, warning, info

# do not use pandas on ethos 1.3.1

from confs.params import * 
from confs.filepaths import * 



# functions

def select_keys(data, list_keys=KEYS_SELECTED) :
	""" just keep needed or asked keys"""

	
	info("select_keys called")

	data = [[i, j] for i,j in data if i in list_keys] 
	
	debug(data)
	
	return data


def convert_dict(data) : 
	""" convert list of list with pair key, value in a dict"""

	info("convert_dict called")
	
	di = dict() 
	
	for i,j in data : 
		try : 
			j = int(j)
			di[i] = j
		except : 
			di[i] = j
	
	debug(di)

	return di


def add_working_gpus(data) : 
	"""add working gpus : gpus curently mining"""

	info("add_working_gpus called")

	gpus = data["miner_hashes"]
	
	debug(gpus)
	
	gpus = [float(i) for i in gpus.split(" ")]
	len_gpus = len([i for i in gpus if i>0])
	
	debug(len_gpus)
 
	if not len_gpus : 
		time.sleep(10*60)
		data["working_gpus"] = int(data["gpus"])

	else : 
		data["working_gpus"] = len_gpus
	
	debug(data["working_gpus"])

	return data


def add_temps(data) : 
	"""add 2 features : max temp and avg temp"""

	info("add_temps called")
	
	temps = data["temp"]
	temps = [float(i) for i in temps.split(" ")]
	
	debug(temps)
	
	working = data["working_gpus"]
	data["temp_avg"]= int(sum(temps)/working)
	data["temp_max"]= int(max(temps))
	
	debug(data["temp_avg"])
	debug(data["temp_max"])
	
	return data


def add_timestamp(data) : 
	"""add timestamp to index the 'dataframe' """

	info("add_timestamp called")
	
	data["timestamp"] =  int(time.time())
	
	debug(data["timestamp"])

	return data


def extract_data(data) : 
	"""whole process from the comand to data dict"""
	
	info("extract_data called")
	
	data = select_keys(data)
	data = convert_dict(data)
	data = add_working_gpus(data)
	data = add_temps(data)
	data = add_timestamp(data)
	
	return data
