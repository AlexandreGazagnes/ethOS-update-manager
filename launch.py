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

from src._launch import *


# main 

def main() : 
	
	randomize_start()
	launch_if_needed(working_process())


if __name__ == '__main__':
	main()
	
	
	
