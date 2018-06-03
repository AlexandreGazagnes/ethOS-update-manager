
#!/usr/bin/env python3
#--*-- coding: utf-8 --*--


import argparse, os, system

from ethuper.command import * 
from ethuper.manager import * 



def main() : 

    # handle arg c/gar v
    command, option = arg_manager()

    command_manager(command, option)



if __name__ == '__main__':
    main()

