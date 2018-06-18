#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
ethOS-update-manager - launcher - v0.5.0
launcher for main.py
avoid multi session launching by adding random sleeper  and
by searching in all process if program aleardy running 
for more info  please read /src/main.py
"""


# import 

import os, time, random


# main 

def main() : 

	# add a random sleeper to avoid multi boot 
	s = round(random.random() * 10 * 1, 1) 
	time.sleep(s)

	# handle working processes 
	process = os.popen("ps -aux | grep ethOS-update-manager").readlines()
	is_working = ["src/main.py" in p for p in process]

	# if 1 process break
	if True in is_working :
		print("ethOS-update-manager already running")
		return 0
	
	# else launch one
	print("ethOS-update-manager launched")
	os.system("nohup python3 /home/ethos/ethOS-update-manager/src/main.py >> /home/ethos/ethOS-update-manager/logs/log 2>&1 &")
	return 0


if __name__ == '__main__':
	main()
	
	
	
