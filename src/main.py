#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Import 

import os,  time

from logging import debug, warning, info
import logging ; logging.basicConfig(level=logging.INFO)


# Consts

CMD = "show stats"	# CMD = "show stats" # or update
SLEEPER = 10 * 60 	# 5/10/15 minutes
MIN_HASH = 179		# 30 ou 120 ou 180 ...


# Functions

def data_from_cmd(cmd="show stats") :
	"""create a txt from a popen command, for ex "show stats" """ 

	debug("data_from_cmd called")

	wrap = os.popen(cmd)
	txt = str()

	for i in wrap : 
		txt +=i

	if not txt : 
		warning("time {} : txt is None".format(_time()))

	return txt


def convert_txt(txt):
	"""from the str version of cli "show stats", create and return a list of
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
	"""convert list of list with pair key, value in a dict"""

	debug("convert_dict called")
	
	di = dict() 
	
	for i,j in data : 
		try :
			j = float(j)
			di[str(i)] = j
		except : 
			di[str(i)] = str(j)

	return di


def return_hash(data, key="hash") : 
	""" return hash float"""

	try : 
		k = float(data[key])
		debug("good type 'float' of hash")
		return k
	except : 
		k = str(data["hash"])
		msg = "time {} : error reading 'hash' as a float for : {}".format(
				_time(), k)
		warning(msg)
		return k


def _time() : 
	""" give local time in personal str format"""
	
	debug("_time called") 
	
	t = time.localtime()
	txt = "{:0>2}/{:0>2}/{:0>2} at {:0>2}:{:0>2}".format(
		t.tm_mday, t.tm_mon, t.tm_year - 2000, t.tm_hour, t.tm_min)

	return txt


# Main

def main() : 

	# init logging
	print("\n\n\n")
	msg = "time {} : init new session!".format(_time())
	warning(msg) 

	# main loop
	while True : 

		# wait
		time.sleep(SLEEPER) 				# to avoid multiple short reboot 
		
		# proceed 
		txt = data_from_cmd("show stats") 	# extract text
		data = convert_txt(txt)				# extract data from text				
		data = convert_dict(data)			# build data dict of int or str 
		hashrate = return_hash(data, "hash")

		# reboot option
		if isinstance(hashrate, float) : 
			if hashrate < MIN_HASH : 
				msg = "time : {} rebooting due to hashrate : {}\n".format(
				_time(), hashrate)
				warning(msg)
				os.system("r")
			else : 
				info("time : {} hashrate OK : {}\n".format(
				_time(), hashrate))
		else : 
			warning("time : {} Invalid hrate type\n".format(hashrate))

		# record uptime
		uptime  = os.popen("uptime").readlines()[0].split(",")[0]
		uptime = uptime.split("up")[1]
		msg = "Uptime : {}".format(uptime)
		info(msg)


if __name__ == '__main__':
	main()

