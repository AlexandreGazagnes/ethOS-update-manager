#!/usr/bin/env python3
#--*-- coding: utf-8 --*--



# import 

import argparse, os

from _ethuper.command import * 
from _ethuper.manager import * 



# main 

def main() : 

    # handle args
    command, option = arg_manager()
    command_manager(command, option)



if __name__ == '__main__':
    main()

