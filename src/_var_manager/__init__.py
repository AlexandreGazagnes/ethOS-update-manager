#!/usr/bin/env python3
#--*--coding: utf-8 --*--



# import 

import os, pickle
from confs.filepaths import * 



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


	if mode == "i" : 
		with open(folder+filename, "r") as f : res = f.read()
		try : 
			res = int(res)
			res +=1
			res = str(res)
			with open(folder+filename, "w") as f :  f.write(res)
		except : 
			raise ValueError("incrementation not possible, txt/bin format confusion")

	elif mode == "w" : 
		if not var : 
			raise ValueError("trying to write nothing")
		txt = str(var)
		with open(folder + filename, mode) as f : f.write(txt)
		return 1

	elif mode =="rb" :

		with open(folder+filename, mode) as f : res = f.load()	
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

		with open(folder + filename, mode) as f : 
			f.dump(var, f)
		return 1

	if mode == "ib" : 
		with open(folder+filename, "rb") as f : res = f.load()
		try : 
			res = int(res)
			res +=1
			with open(folder+filename, "wb") as f : f.dump(res, f)
		except : 
			raise ValueError("incrementation not possible, txt/bin format confusion")


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
			with open(folder+file, "rb") as f : var = str(f.load())
			if verbose : 
				print("bin format : ")
			print(var)


