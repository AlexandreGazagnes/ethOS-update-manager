#!/usr/bin/env python3
#--*--coding: utf-8 --*--



# import 

import os



# functions 

def var_manager(filename, mode, var=None, folder="/home/alex/ethOS-update-manager/src/var/") : 
	""" """

	if mode == "r" : 
		with open(folder+filename, mode) as f : 
			res = f.read()
		try : 
			res = int(res)
		except : 
			pass
		return res

	elif mode == "w" : 
		if not var : 
			raise ValueError("trying to write nothing")
		txt = str(var)
		with open(folder + filename, mode) as f : 
			f.write(txt)
		return 1

	elif mode =="rb" : 
		print("not implemented : bin format (pickle)")	
	
	elif mode == "wb" : 
		print("not implemented : bin format (pickle)")	


def var_list(folder="/home/ethos/ethOS-update-manager/src/var/"): 
	""" """ 

	return os.listdir(folder)


def var_read(folder="/home/ethos/ethOS-update-manager/src/var/", verbose=False) : 
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
			print("not implemented : bin format (pickle)")	

	