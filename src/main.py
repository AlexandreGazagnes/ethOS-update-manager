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

SLEEPER 	= 10 * 60 		# IN SECONDS think to multiply by 60 for minutes ;)
MIN_HASH 	= 179			# 30 ou 120 ou 180 ... depends of your perf and GPU's number
JET_LAG 	= 1				# depends of your local/sys time 
LATENCY 	= True			# if LATENCY additionnal sleeper added to give time 
							# to rig to be fully operational (STRONGLY RECOMMANDED)


ENABLE_TELEGRAM_MSG = True
TOKEN = "5464657szzs33:AAHXfOQb5zYqVHShspgomsCwA"
CHAT_ID = "49zsz24419"
RIG = "Rig"


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
		warning("error unknown --> Please debug  MANUALY!")


def data_from_cmd(cmd="show stats", fake_file=None) :
	"""create a txt from a popen command, for ex "show stats" """ 

	debug("data_from_cmd called")

	# define default fake file
	if not fake_file : 
		fake_file = "/home/ethos/ethOS-update-manager/.show_stats.txt"
	
	# handle cmd result
	li = os.popen(cmd).readlines()

	debug("command executed and handled")
	
	if not li : 
		res = os.system(cmd)

		if res : 
			warning("command unknown --> simulation mode ON")
			li = os.popen("cat {}".format(fake_file))

		else : 
			warning("error unknown --> Please debug  MANUALY!")
			li = os.popen("cat {}".format(fake_file))
	

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


def return_hash(data, key="hash") : 
	""" return hash float"""

	debug ("return_hash called")

	try : 
		hashrate = float(data[key])
		debug("good type 'float' of hash")
		return hashrate
	except : 
		hashrate = str(data["hash"])
		warning("error reading 'hash' as a float for : {}".format(hashrate)) 
		return hashrate


def _time(jet_lag=JET_LAG) : 
	""" give local time in personal str format"""
	
	debug("_time called") 
	
	t = time.localtime()
	txt = "{:0>2}/{:0>2}/{:0>2} {:0>2}:{:0>2}".format(
		t.tm_mday, t.tm_mon, t.tm_year - 2000, t.tm_hour+jet_lag, t.tm_min)

	return txt


def send_bot(bot_message="", rig=RIG , token=TOKEN, chat_id=CHAT_ID):
	"""useful function to send a message to your bot in cli"""

	debug("send_bot called")

	msg = str(bot_message)
	if not bot_message : 
		msg = "error : bot_message : invalid argument"
	
	txt = urllib.parse.urlencode({"text":msg})
	
	req = 	 'https://api.telegram.org/bot' + token \
					+ '/sendMessage?chat_id=' + chat_id \
					+ '&parse_mode=Markdown&' + txt

	with urllib.request.urlopen(req) as f : none = f.read()


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


def uptime() : 
	"""record uptime """
	
	debug("uptime called")

	uptime  = os.popen("uptime").readlines()[0].split(",")[0]
	uptime = uptime.split("up")[1]

	return uptime


def warning(msg, rig=RIG , token=TOKEN, chat_id=CHAT_ID, telegram=ENABLE_TELEGRAM_MSG) : 
	"""over write warning """

	debug("warning called")

	msg = rig + " up " + str(uptime()) + ": " + msg
	if telegram : send_bot(msg, token, chat_id)

	msg = _time() + " : " + msg
	logging.warning(msg)


def info(msg, rig=RIG , token=TOKEN, chat_id=CHAT_ID,  telegram=ENABLE_TELEGRAM_MSG):
	"""over write info """

	debug("info called")

	if telegram : send_bot(msg, rig , token, chat_id)

	msg = rig + " up " + str(uptime()) + ": " + msg
	if telegram : send_bot(msg, token, chat_id)

	msg = _time() + " : " + msg

	logging.info(msg) 


def debug(msg) : 
	"""over write debug """

	logging.debug(msg)


# main

def main() : 

	# init logging
	warning("\n\n\n")
	warning("init new session!")

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
				warning("rebooting due to hashrate : {}\n".format(hashrate))
				reboot()

			else : 
				debug("hashrate OK")

		else : 
			warning("invalid hrate type {} \n".format(type(hashrate)))

		# wait
		time.sleep(SLEEPER) # to avoid multiple short reboot 


if __name__ == '__main__':
	main()

