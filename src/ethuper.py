#!/usr/bin/env python3
#--*-- coding: utf-8 --*--



# import 

import argparse, os

from logging import debug, warning, info
import logging

"""
adding auto level reading
lev = int(var_manager(VAR__FOLDER+"log_level.pk", "r")
logging.basicConfig(level=lev)
"""

from _ethuper.manager import * 



# main 

def main() : 

	# handle args
	command, option = arg_manager()

	logging.debug(command)
	logging.debug(option)
	
	if command :     
		# execute command and option
		command_manager(command, option)



if __name__ == '__main__':
	main()

