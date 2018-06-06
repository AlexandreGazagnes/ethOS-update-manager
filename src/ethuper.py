#!/usr/bin/env python3
#--*-- coding: utf-8 --*--



# import 

import logging

from _var_manager import *
from confs.filepaths import * 

# reading and setting auto log level
lev = var_manager("log_level.pk", "r", folder=VAR_FOLDER)	
logging.basicConfig(level=int(lev))

from _ethuper.manager import * 


# main 

def main() : 

	# handle argparse
	command, option = arg_manager()

	logging.debug(command)
	logging.debug(option)
	
	if command :     
		# execute command and option
		command_manager(command, option)



if __name__ == '__main__':
	main()

