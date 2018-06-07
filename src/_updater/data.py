#!/usr/bin/env python3
# -*- coding: utf-8 -*-



# import 

import os, subprocess, pickle, time, logging

from logging import debug, warning, info

from confs.params import * 
from confs.filepaths import * 



# functions

def select_keys(data, list_keys=KEYS_SELECTED) :
	""" just keep needed or asked keys"""

	logging.info("select_keys called")

	data = [[i, j] for i,j in data if i in list_keys] 
	
	logging.debug(data)
	
	return data


def convert_dict(data) : 
	""" convert list of list with pair key, value in a dict"""

	logging.info("convert_dict called")
	
	di = dict() 
	
	for i,j in data : 
		try : 
			j = int(j)
			di[i] = j
		except : 
			di[i] = j
	
	logging.debug(di)

	return di


def add_working_gpus(data) : 
	"""add working gpus : gpus curently mining"""

	logging.info("add_working_gpus called")

	gpus = data["miner_hashes"]
	
	logging.debug(gpus)
	
	gpus = [float(i) for i in gpus.split(" ")]
	len_gpus = len([i for i in gpus if i>0])
	
	logging.debug(len_gpus)
 
	if not len_gpus : 
		time.sleep(10*60)
		data["working_gpus"] = int(data["gpus"])

	else : 
		data["working_gpus"] = len_gpus
	
	logging.debug(data["working_gpus"])

	return data


def add_temps(data) : 
	"""add 2 features : max temp and avg temp"""

	logging.info("add_temps called")
	
	temps = data["temp"]
	temps = [float(i) for i in temps.split(" ")]
	
	logging.debug(temps)
	
	working = int(data["working_gpus"])
	data["temp_avg"]= int(sum(temps)/working)
	data["temp_max"]= int(max(temps))
	
	logging.debug(data["temp_avg"])
	logging.debug(data["temp_max"])
	
	return data


def add_timestamp(data) : 
	"""add timestamp to index the 'dataframe' """

	logging.info("add_timestamp called")
	
	data["timestamp"] =  int(time.time())
	
	logging.debug(data["timestamp"])

	return data


def add_session_number(data) : 
	""" """

	logging.info("add_session_number called")
	
	i = var_manager("session_number.pk", "r")
	data["session_number"] = str(i)

	logging.debug(data["session_number"])

	return data


def extract_data(data) : 
	"""whole process from the comand to data dict"""
	
	logging.info("extract_data called")
	
	data = select_keys(data)
	data = convert_dict(data)
	data = add_working_gpus(data)
	data = add_temps(data)
	data = add_timestamp(data)
	data = add_session_number(data)
	
	return data
