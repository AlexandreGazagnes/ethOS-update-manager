#!/usr/bin/env python3
#--*--coding: utf-8 --*--


import os 


def install():

	with open("/home/ethos/ethOS-update-manager/src/var/install.pk", "r") as f : inst = int(f.read())

	if not inst  : 
		os.system("rm -f /home/ethos/ethOS-update-manager/install")
		with open("/home/ethos/ethOS-update-manager/src/var/install.pk", "w") as f : f.write("0")
