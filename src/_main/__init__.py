#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
main functions
"""


# import 

import os, time, logging, urllib.parse, urllib.request
from _var import * 


# read var
USER, IP_INT, IP_EXT = load_id_var()
TELEGRAM_MODE, TOKEN, CHAT_ID, RIG = load_telegram_var()
SLEEPER, LAP_STAMP, AUTO_REBOOT, AUTO_LAUNCH, HASH_MODE, MIN_HASH, \
	TEMP_MODE, MAX_TEMP, JET_LAG, LATENCY, LOGGING_LEVEL = load_system_var()



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

	debug("return_hash called")

	try : 

		hashrate = float(data[key])
		debug("good type 'float' of hash")
		return hashrate
	
	except Exception as e: 

		try : 
			logging.warning(e)
			hashrate = str(data["hash"])
			warning("error reading 'hash' as a float for {}".format(hashrate)) 
			return hashrate
	
		except Exception as e: 
			logging.warning(e)
			warning("miner maybe not started yet")
			os.system("allow")
			time.sleep(2)
			os.system("minestart")
			time.sleep(5*60) 
			return default_hashrate


def _jet_lag(h, jet_lag=JET_LAG) : 
	"""be sue that h 24 format"""
	
	debug("_jet_lag called")

	return h-24 if h>24 else h


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

	debug("request called")

	txt = str(msg).strip()
	
	# # URL = [(" ","+"), ("/","%2F"), (":","%3A"), (",","%2C"), ("#","%23"), ("!","%21"), ("_","%5F")] 
	URL = [(i, "+") for i in [" ", "/", ":", "," ,"#", "!", "_", "(", ")", "\n", '"', "'"]]

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
		
		try : 
			logging.warning(e)
			request("request failed, please watch out logging file")
	
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
	
	logging.debug("uptime called")

	uptime  = os.popen("uptime").readlines()[0].split(",")[0]
	uptime = str(uptime.split("up")[1])
	uptime = uptime.replace(":", "h")

	return uptime


def warning(msg, rig=RIG, telegram=TELEGRAM_MODE) : 
	"""over write warning """

	debug("warning called")

	msg = "{} up{} {}".format(rig, _uptime(), msg)
	
	if telegram : 
		send_bot(msg)

	msg =  "{} {}".format(_time(), msg)
	logging.warning(msg)


def info(msg, rig=RIG, telegram=TELEGRAM_MODE):
	"""over write info """

	debug("info called")

	msg = "{} up{} {}".format(rig, _uptime(), msg)
	
	if telegram : 
		send_bot(msg)

	msg =  "{} {}".format(_time(), msg)
	logging.info(msg)


def debug(msg) : 
	"""over write debug """

	logging.debug(msg)


