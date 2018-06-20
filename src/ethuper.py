#!/usr/bin/env python3
#--*-- coding: utf-8 --*--


"""
ethuper
"""


# import 

import logging
from _var import *
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

