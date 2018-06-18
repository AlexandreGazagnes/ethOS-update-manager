#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
var functions
"""


# import 

import pickle, random, urllib.request


# sys params

SLEEPER 	= 10 * 60		# IN SECONDS think to multiply by 60 for minutes ;)
LAP_STAMP	= 6 * 4			# update normal status each LAP_STAMP * SLEEPER sec
MIN_HASH 	= 179			# 30 ou 120 ou 180 ... depends of your perf and GPU's number
AUTO_REBOOT = True			# enable auto reboot if min hashrate threshold reached
JET_LAG 	= 8				# depends of your local/sys time 
LATENCY 	= True			# if LATENCY additionnal sleeper added to give time 
							# to rig to be fully operational (STRONGLY RECOMMANDED)
VAR_FOLDER 	= "/home/ethos/ethOS-update-manager/src/var/"


# telegram params

TELEGRAM_MODE 	= False 	
TOKEN 			= "YourToken"
CHAT_ID 		= "YourChatId"
RIG 			= "YourRigName"


# functions 

def var_manager(filename, mode, var=None, folder=VAR_FOLDER) : 
	""" """

	if mode == "r" : 
		with open(folder+filename, mode) as f : res = f.read()
		try : 
			res = int(res)
		except : 
			pass
		return res

	elif mode == "i" : 
		with open(folder+filename, "r") as f : res = f.read()
		try : 
			res = str(int(res) + 1)
			with open(folder+filename, "w") as f :  f.write(res)
		except : 
			raise ValueError("incrementation not possible, txt/bin format confusion")

	elif mode == "w" : 
		with open(folder + filename, mode) as f : f.write(str(var))
		return 1

	elif mode =="rb" :
		with open(folder+filename, mode) as f : res = pickle.load(f)	
		try : 
			res = int(res)
		except : 
			pass
		return res
	
	elif mode == "wb" :
		try : 
			var = int(var)
		except : 
			pass 
		with open(folder + filename, mode) as f : pickle.dump(var, f)
		return 1

	elif  mode == "ib" : 
		with open(folder+filename, "rb") as f : res = pickle.load(f)
		try : 
			res = int(res) + 1
			with open(folder+filename, "wb") as f : pickle.dump(res, f)
		except : 
			raise ValueError("incrementation not possible, txt/bin format confusion")

	else : 
		raise ValueError("Fatal Error")

def var_list(folder=VAR_FOLDER): 
	""" """ 

	print(os.listdir(folder))
	return(os.listdir(folder)) 


def var_read(folder=VAR_FOLDER, verbose=False) : 
	""" """

	file_list = os.listdir(folder)
	if verbose : 
		print(file_list) 

	for file in file_list : 
		print(str(file + " : "), end="  ")
		try : 
			with open(folder+file, "r") as f : var = f.read()
			if verbose : 
				print("txt format : ")
			print(var)
		
		except : 
			with open(folder+file, "rb") as f : var = str(pickle.load(f))
			if verbose : 
				print("bin format : ")
			print(str(var), str(type(var)))


def handle_bool() : 
	"""read a bool response"""

	ans = input("y/n\n")
	
	while True: 

		if ans.lower() == "y" : 
			return True
		elif ans.lower() == "n":
			return False
		else : 
			ans = input("\nwrong input, expected 'y' or 'n'\n")
			

def handle_int(mi=0, ma=10000) : 
	"""read a int response"""

	ans = input("number between {} and {}\n".format(mi, ma))
	
	while True: 

		try : 
			ans = int(ans)
			if (ans > mi) and (ans < ma) : 
				return ans
			else : 
				ans = input("\nwrong input, expected number between {} and {}\n".format(mi, ma))
		except :  
			ans = input("\nwrong input, expected number between {} and {}\n".format(mi, ma))


def set_system_var(mode="w", folder=VAR_FOLDER) : 
	""" """

	print("do you want to use system default var ?")
	ans = handle_bool()

	if ans : 
		var_manager("SLEEPER", mode, SLEEPER, folder=folder)
		var_manager("LAP_STAMP", mode, LAP_STAMP, folder=folder)
		var_manager("MIN_HASH", mode, MIN_HASH, folder=folder)
		var_manager("AUTO_REBOOT", mode, AUTO_REBOOT, folder=folder)		
		var_manager("JET_LAG", mode, JET_LAG, folder=folder)
		var_manager("LATENCY", mode, LATENCY, folder=folder)

	else : 
		print("\nSLEEPER : the time of loop processing -- in seconds --, default value (STRONGLY RECOMMANDED) : {}".format(SLEEPER))
		print("define sleeper : ")
		ans = handle_int(60, 60*60)
		var_manager("SLEEPER", mode, ans, folder=folder)

		print("\nLAP_STAMP : the rate of info logging (inform you if everything is fine), the more it is important the less you will be informed -- in lap --, default value (STRONGLY RECOMMANDED) : {}".format(LAP_STAMP))
		print("define lap_stamp : ")
		ans = handle_int(1, 6*24)
		var_manager("LAP_STAMP", mode, ans, folder=folder)		

		print("\nMIN_HASH : if your miner's hashrate fall bellow this threshold you will be warned and miner will reboot. Consider nb of GPUS x min GPU expected rate -- in global summed hashrate --, default value : {}".format(MIN_HASH))
		print("\ndefine min_hash : ")
		ans = handle_int(15, 12 * 35)
		var_manager("MIN_HASH", mode, ans, folder=folder)

		print("\nAUTO_REBOOT : Boolean value -- y/n--, if set, your miner will reboot if MIN_HASH threshold is reached, default value (STRONGLY RECOMMANDED) : {}".format("y"))		
		print("\ndefine auto reboot : ")
		ans = handle_bool()
		if not ans : ans=0
		var_manager("AUTO_REBOOT", mode, ans, folder=folder)

		print("\nJET_LAG : the time stamp -- in hours -- between your local time and your system time, default value : {}".format(JET_LAG))		
		print("define jet_lag : ")
		ans = handle_int(-24, +24)
		var_manager("JET_LAG", mode, ans, folder=folder)
	
		print("\nLATENCY : Boolean value -- y/n--, if set, your miner will have the time to wake up and to launch all GPUs before being scanned, default value (STRONGLY RECOMMANDED) : {}".format("y"))		
		print("\ndefine latency : ")
		ans = handle_bool()
		if not ans : ans=0
		var_manager("LATENCY", mode, ans, folder=folder)


def set_telegram_var(mode="w", folder=VAR_FOLDER) :
	""" """ 
	
	print("do you want to enable telegram auto push logging ?")
	ans = handle_bool()

	connect_not_confirmed = True 

	if ans : 

		while connect_not_confirmed :  

			var_manager("TELEGRAM_MODE", mode, True)

			print("\ndefine token : ")
			token = input("alphanumeric input\n")
			var_manager("TOKEN", mode, token)

			print("\ndefine chat_id : ")
			chat_id = input("alphanumeric input\n")
			var_manager("CHAT_ID", mode, chat_id)		

			print("\ndefine rig_name : ")
			rig = input("alphanumeric input\n")
			var_manager("RIG", mode, rig)

			connect_not_confirmed = confirm_connexion(token, chat_id)
			if confirm_connexion == 2 : 
				var_manager("TELEGRAM_MODE", mode, False)
				connect_not_confirmed = 0
	
	else :
		var_manager("TELEGRAM_MODE", mode, False)


def confirm_connexion(token, chat_id, mi=100000, ma=999999) : 
	""" """

	code = random.randint(mi, ma)

	try : 
		req = str('https://api.telegram.org/bot' + str(token) + '/sendMessage?chat_id=' + str(chat_id) + '&parse_mode=Markdown&text=' + str(code))	
		urllib.request.urlopen(req)

		print("\nto autorize connection, a personnal code was sent to your telegram account, please check")
		print("\nconnection code : ")
		ans = handle_int(mi, ma)

		if ans == code : 	
			print("\nconnection established")
			return 0
		else : 
			print("\nconnection error, try again (y) or disable telegram mode (n)")
			ans = handle_bool()

			if ans  : return 1
			else 	: return 2 
	
	except : 
		print("\nconnection error, try again (y) or disable telegram mode (n)")
		ans = handle_bool()
		
		if ans  : return 1
		else 	: return 2 





def load_system_var(folder = VAR_FOLDER) : 
	""" """

	SLEEPER 	= var_manager("SLEEPER", "rb")
	LAP_STAMP 	= var_manager("LAP_STAMP", "rb")
	MIN_HASH 	= var_manager("MIN_HASH", "rb")
	AUTO_REBOOT	= var_manager("AUTO_REBOOT", "rb")	
	JET_LAG 	= var_manager("JET_LAG", "rb")
	LATENCY 	= var_manager("LATENCY", "rb")

	return SLEEPER, LAP_STAMP, MIN_HASH, AUTO_REBOOT, LATENCY


def load_telegram_var(folder=VAR_FOLDER) : 
	""" """

	TELEGRAM_MODE 	= var_manager("TELEGRAM_MODE", "rb")

	if not TELEGRAM_MODE : 
		return False, None, None, None

	else :
		TOKEN 	= var_manager("TOKEN", "rb")
		CHAT_ID	= var_manager("CHAT_ID", "rb")
		RIG 	= var_manager("RIG", "rb")

		return True, TOKEN, CHAT_ID, RIG



