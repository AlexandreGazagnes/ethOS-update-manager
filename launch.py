#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os


def main() : 

	# handle working processes 
	process = os.popen("ps -aux | grep ethOS-update-manager").readlines()
	is_working = ["src/main.py" in p for p in process]

	# if 0 process launched, launch one 
	if True not in is_working :
		print("ethOS-update-manager first launch")
		os.system("nohup python3 /home/ethos/ethOS-update-manager/src/main.py >> /home/ethos/ethOS-update-manager/logs/log 2>&1 &")
		return 0

	# else if one already working, don to not launch an another
	print("ethOS-update-manager already running")
	return 0

	# # chechk instead if multiple working processes
	# working = [p for p in process if "src/main.py" in p]
	# nb = len(working)

	# # if only one process OK, return 0
	# if nb == 1 : 
	# 	print("Good : only one process is runing")

	# 	return 0

	# print("error : two identical process are runing")

	# # while multiple working processes, find pid and kill 
	# while nb > 1 : 

	# 	print("cleaning...")

	# 	# update list of process
	# 	process = os.popen("ps -aux | grep ethOS-update-manager").readlines()
	# 	working = [p for p in process if "src/main.py" in p]
		
	# 	# clean list and handle list of list
	# 	working = [p.split(" ") for p  in working]
	# 	working = [ [p for p in lign if p] for lign  in working]

	# 	# find pid and kill
	# 	pid = str(working[0][1])
	# 	cmd = "kill "+ pid
	# 	os.system(cmd)

	# 	# update nb
	# 	process = os.popen("ps -aux | grep ethOS-update-manager").readlines()
	# 	working = [p for p in process if "src/main.py" in p]
	# 	nb = len(working)

	# # at the hend check nb == 1
	# process = os.popen("ps -aux | grep ethOS-update-manager").readlines()
	# working = [p for p in process if "src/main.py" in p]
	# nb = len(working)

	# if nb == 1 : 
	# 	print("Good : only one process is runing")
	# 	return 0

	# # else 
	# print("MAJOR ERROR cleaning processes not perform well")
	# return 1


if __name__ == '__main__':
	main()
	
	
	
