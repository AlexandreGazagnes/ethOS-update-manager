#!/usr/bin/env python3
#--*-- coding: utf-8 --*--



# import 

import os, time
from logging import debug, info, warning
import logging

from _installer.user import * 
from _installer.system import * 

# main

def main() : 

	# update install.pk
	with open("/home/ethos/ethOS-update-manager/src/var/install.pk", "w") as f:
		f.write("1")

	# manage user level of confidence 
	user_settings()

	# prepare sys
	prepare_sys()

	# create alias
	add_aliases()

	# for automatic program launch (background) at each ethos stratup : 
	add_autolaunch()

	# rebbot atrer install
	reboot_install()
	


if __name__ == '__main__':
	main()
