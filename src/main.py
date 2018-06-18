#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
ethOS-update-manager - main - v0.5.0 

Handle results from a CMD 'show stats' or 'update' and reboot 
if nedeed, ie your hashrate is too low (aka MIN_HASH).

Manage bot telegram and send warning msg to your personnal bot 

Please update with your personal settings : SLEEPER, JET_LAG, LATENCY 
and MIN_HASH. You can of course use default settings
"""


# import 

import os, time, logging, urllib.parse, urllib.request


# logging 

logging.basicConfig(	level=logging.INFO, 
						format='%(levelname)s %(message)s')



# consts

SLEEPER 	= 10 * 5		# IN SECONDS think to multiply by 60 for minutes ;)
MIN_HASH 	= 179			# 30 ou 120 ou 180 ... depends of your perf and GPU's number
JET_LAG 	= 7				# depends of your local/sys time 
LATENCY 	= False			# if LATENCY additionnal sleeper added to give time 
							# to rig to be fully operational (STRONGLY RECOMMANDED)


# telegram params

TELEGRAM_MODE 	= True
TOKEN 			= "546465733:AAHXfrCs7pYWeRbOQb5zYqVHShspgomsCwA"
CHAT_ID 		= "487924419"
RIG 			= "Bold_Eagle"


# functions

def not_the_first_process_launched() : 
	""" check if on porcess is already running"""

	debug("not_the_first_process_launched called")

	time.sleep(3)

	process = os.popen("ps -aux | grep ethOS-update-manager").readlines()
	working = [p for p in process if "src/main.py" in p]
	nb = len(working)

	if nb > 1 :	return True
	else : 		return False


def search_and_autokill() : 
	""" search pid of other instance and kill it"""

	debug("search_and_autokill called")

	time.sleep(3)

	process = os.popen("ps -aux | grep ethOS-update-manager").readlines()
	working = [p for p in process if "src/main.py" in p]
	working = [line.split(" ") for line in working]
	working = [[i for i in line if i] for line in working]
	pids = [i[1] for i in working]

	l = len(pids)
	if l  == 1 : 
		debug("good number of process")
	elif l > 1 : 
		warning("invalid number of process : {}, kill first one".format(pids))
		try : 
			os.system(str("kill " + pids[0]))
			warning("process killed")
		except : 
			warning("autokill failed, please kill it MANUALY")
	else : 
		warning("error unknown, please debug  MANUALY!")


def data_from_cmd(cmd="show stats", fake_mode=False, fake_cmd="cat", fake_file=None) :
	"""create a txt from a popen command, for ex "show stats" """ 

	debug("data_from_cmd called")

	# define default fake file
	if not fake_file : 
		fake_file = "/home/ethos/ethOS-update-manager/.show_stats.txt"
	
	# handle cmd result
	if not fake_mode : 
		debug("real mode")
		li = os.popen(cmd).readlines()
	else : 
		warning("fake_mode, simulation mode ON")
		li = os.popen("{} {}".format(fake_cmd, fake_file))

	debug("command executed and handled")
	
	if not li : 
		res = os.system(cmd)

		if res : 
			warning("command unknown, simulation mode ON")
			li = os.popen("{} {}".format(fake_cmd, fake_file))

		else : 
			warning("error unknown, Please debug  MANUALY!")
			li = os.popen("{} {}".format(fake_cmd, fake_file))
	

	# list operations
	li = [i.replace("\n", "") for i in li if i.replace("\n", "")] # delete '\n' and null lines
	li = [i for i in li if i[0] != " "] # delete lines with no keys (mem info and models)
	li = [i.split(":") for i in li] # separate key, value with ":"
	li = [i for i in li if i[0]] 	# delete null keys
	li = [i for i in li if i[1]] # delete null values
	li = [[i[0].strip(), i[1].strip()] for i in li] # strip everything

	# dict operations
	data = {i[0] : i[1] for i in li} # create dict
	for i, j in data.items() : # auto cast
		try : data[i] = float(j)
		except : data[i] = str(j)

	return data


def return_hash(data, key="hash", default_hashrate=187) : 
	""" return hash float"""

	debug ("return_hash called")

	try : 

		hashrate = float(data[key])
		debug("good type 'float' of hash")
		return hashrate
	
	except Exception as e: 

		try : 
			warning(e)
			hashrate = str(data["hash"])
			warning("error reading 'hash' as a float for {}".format(hashrate)) 
			return hashrate
	
		except Exception as e: 
			warning(e)
			warning("Miner maybe not started yet")
			os.system("allow")
			os.system("minestart")
			time.sleep(5*60) 
			return default_hashrate


def _jet_lag(h, jet_lag=JET_LAG) : 
	"""be sue that h 24 format"""
	
	debug("_jet_lag called")

	return h = h-24 if h>24 else h


def _time(jet_lag=JET_LAG) : 
	""" give local time in personal str format"""
	
	debug("_time called") 
	
	t = time.localtime()
	txt = "{:0>2}/{:0>2}/{:0>2} {:0>2}:{:0>2}".format(
						t.tm_mday, t.tm_mon, t.tm_year - 2000, 
						_jet_lag(t.tm_hour,jet_lag), t.tm_min)

	return txt


def request(msg, token=TOKEN, chat_id=CHAT_ID) :
	""" format text and send a request""" 

	debug("request")

	txt = str(msg).strip()
	
	# # URL = [(" ","+"), ("/","%2F"), (":","%3A"), (",","%2C"), ("#","%23"), ("!","%21"), ("_","%5F")] 
	URL = [(i, "+") for i in [" ", "/", ":", "," ,"#", "!", "_"]]

	for i,j in URL : 
		txt = txt.replace(i, j)

	req = str('https://api.telegram.org/bot' + str(token) + '/sendMessage?chat_id=' + str(chat_id) + '&parse_mode=Markdown&text=' + str(txt))
	
	urllib.request.urlopen(req)	


def send_bot(msg=""):
	"""useful function to send a message to your bot in cli"""

	debug("send_bot called")

	try : 
		request(msg)	
	
	except Exception as e:
		logging.warning(e) ; 
		logging.warning("first request failed, trying a second one")

		try : 
			request("Error+Calling+Request+As+Normal")
			
		except Exception as e :
			logging.warning(e) ; 
			logging.warning("error send_bot, bad request")


def reboot() : 
	"""reboot process from ethos cmd 'r' to 'reboot' to 'sudo reboot' """

	debug("reboot called")

	res = os.system("r")
	if res : 

		warning("previous command fail 'r', trying 'reboot' ")
		res = os.system("reboot")

		if res : 
			warning("previous command fail 'reboot', trying 'sudo reboot' ")
			res = os.system("sudo reboot")

			if res : 
				msg=str("\n\n"
					"##################################################\n"
					"##################################################\n\n\n"
					"-->  auto reboot fail : please reboot manualy  <--\n\n\n"
					"##################################################\n"
					"##################################################\n"
					"\n\n")
				
				warning(msg)
				raise ValueError("auto reboot impossible")


def _uptime() : 
	"""record uptime """
	
	debug("uptime called")

	uptime  = os.popen("uptime").readlines()[0].split(",")[0]
	uptime = str(uptime.split("up")[1])
	uptime = uptime.replace(":", "h")

	return uptime


def warning(msg, rig=RIG, t = _uptime(), telegram=TELEGRAM_MODE) : 
	"""over write warning """

	debug("warning called")

	msg = rig + " up" + t + " " + msg
	if telegram : 
		send_bot(msg)

	msg = _time() + " " + msg
	logging.warning(msg)


def info(msg, rig=RIG, t = _uptime(), telegram=TELEGRAM_MODE):
	"""over write info """

	debug("info called")

	msg = rig + " up" + t + " " + msg
	if telegram : 
		send_bot(msg)

	msg = _time() + " " + msg
	logging.info(msg)


def debug(msg) : 
	"""over write debug """

	debug("msg")

	logging.debug(msg)


# main

def main() : 

	debug("main")

	# init logging
	logging.warning("\n\n\n")
	warning("init new session")

	# to avoid multiple short reboot 
	time.sleep(SLEEPER)
	
	if LATENCY and (SLEEPER < (60 * 6)) :  
		time.sleep(600 - SLEEPER)

	# main loop
	while True :

		debug("main loop entrance") 
		
		# proceed 
		data = data_from_cmd() 	# extract data from cmd 
		hashrate = return_hash(data)

		# reboot option
		if isinstance(hashrate, float) : 
			
			if hashrate < MIN_HASH : 
				warning("rebooting due to hashrate {}\n".format(hashrate))
				reboot()

			else : 
				debug("hashrate OK")

		else : 
			warning("invalid hrate type {}\n".format(type(hashrate)))

		# wait
		time.sleep(SLEEPER) # to avoid multiple short reboot 

		# DELETE, JUST FOR TESTS
		# info("new loop!!!")

if __name__ == '__main__':
	main()

