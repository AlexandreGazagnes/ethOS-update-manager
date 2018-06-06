#!/usr/bin/env python3
#--*-- coding: utf-8 --*--



# import 

import os, time
from logging import debug, info, warning
import logging

from _var_manager import *
from confs.filepaths import * 

# reading and setting auto log level
lev = var_manager("log_level.pk", "r", folder=VAR_FOLDER)	
logging.basicConfig(level=int(lev))

from _installer.user import * 
from _installer.system import * 



# main

def main() : 

	# update install.pk
	var_manager("install.pk", "w", str(1), folder=VAR_FOLDER)

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
