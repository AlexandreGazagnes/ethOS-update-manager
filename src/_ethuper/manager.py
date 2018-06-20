#!/usr/bin/env python3
#--*-- coding: utf-8 --*--


"""
ethuper : manager functions
"""


# import 

import argparse, os, sys
from src._var import * 
from _ethuper.command import * 


# functions

def arg_manager() : 
    """ hanle CLI arguments with full doc"""

    s = str(sys.argv)
    logging.debug(s)

    if len(sys.argv) == 1 : 
        print("You have to call 'ethuper COMMAND + [OPTION]' (if needed)")
        helper()
        return None, None
    elif len(sys.argv) == 3 : 
        return sys.argv[1], sys.argv[2] 
    elif len(sys.argv) == 2 :
        return sys.argv[1], None
    else : 
        print("to many command/option, tryin with {} and {}"
                .format(sys.argv[0],sys.argv[1] ))
        helper()
        return sys.argv[0], sys.argv[1]


def command_manager(command, option) : 
    """ """
    
    if not command  : 
        print("error you have to chose an command" )
        helper()

    elif command == "auto-launch" : 
        auto_launch(option)

    elif command == "start" :
        start()
        
    elif command == "is-working" :
        is_working()

    elif command == "stop" :
        stop()

    elif command == "restart" :
        restart()

    elif command == "config" : 
        config(option)

    elif command == "reboot-aut" :
        reboot_aut(option) 

    elif command == "merge-files" : 
        merge_files()

    elif (command == "man") or (command == "help"): 
        man()

    elif command == "unistall" : 
        unistall(option)
    else : 
        print("Error command not avialable")
        helper()


def helper() : 
    """ """
    print("type 'ethuper man' or 'ethuper help' for full info")
