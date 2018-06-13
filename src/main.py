#!/usr/bin/env python3
# -*- coding: utf-8 -*-



# import 

import os, subprocess, pickle, time

from logging import debug, warning, info
import logging
logging.basicConfig(level=logging.INFO)


# Consts

CMD = "show stats"	# CMD = "show stats" # or update

SLEEPER = 5 * 60 	# 5 minutes

MIN_HASH = 179


# Functions

def data_from_cmd(cmd="show stats") :
	"""create a txt from a popen command, for ex "update" """ 

	debug("data_from_cmd called")

	wrap = os.popen(cmd)
	txt = str()

	for i in wrap : 
		txt +=i

	if not txt : 

		info("txt is None")

	return txt


def convert_txt(txt):
	"""from the str version of cli "update", create and return a list of
	key, values"""

	debug("convert_txt called")

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
	
	return li3


def convert_dict(data) : 
	""" convert list of list with pair key, value in a dict"""

	debug("convert_dict called")
	
	di = dict() 
	
	for i,j in data : 
		try :
			j = int(j)
			di[str(i)] = j
		except : 
			di[str(i)] = str(j)

	return di


def return_hash(data, key="hash") : 
	""" return hash int"""

	try : 
		k = int(float(data["hash"]))
		info("good int of hash")
		return k
	except : 
		k = str(data["hash"])
		error = "error reading hash at {} for value : {}".format(
				str(int(time.time())), k)
		info(error)
		return k


# Main

def main() : 

	# init logging
	msg = "time : {} init new session!\n\n".format(str(int(time.time())))
	logging.info(msg) 

	# wait
	time.sleep(SLEEPER)

	# main loop
	while True : 

		# wait
		time.sleep(SLEEPER) # to avoid multiple short reboot 
		
		# proceed 
		txt = data_from_cmd("show stats") 	# extract text
		data = convert_txt(txt)				# extract data from text				
		data = convert_dict(data)			# build data dict of int or str 
		hashrate = return_hash(data, "hash")

		# reboot option
		if isinstance(hashrate, int) : 
			if hashrate < MIN_HASH : 
				error = "rebooting due to hashrate at {} for value : {}".format(
				str(int(time.time())), hashrate)
				os.system("r")

		# record uptime
		uptime = uptime = os.popen("uptime").readlines()[0].split(",")[0]
		uptime = uptime.split("up")[1]
		msg = "Uptime : {}".format(uptime)
		logging.info(msg)



if __name__ == '__main__':
	main()


