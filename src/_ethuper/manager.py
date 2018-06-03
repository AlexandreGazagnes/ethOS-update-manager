#!/usr/bin/env python3
#--*-- coding: utf-8 --*--



# import 

import argparse, os, sys



# functions

def arg_manager() : 
    """ hanle CLI arguments with full doc"""

    if not len(sys.argv) : 
        print("You have to call 'ehtuper COMMAND + [OPTION] (if needed)")
    elif len(sys.argv) == 2 : 
        return sys.argv
    elif len(sys.argv) == 1 :
        return sys.argv[0], None
    else : 
        print("to many command/option, tryin with {} and {}"
                .format(sys.argv[0],sys.argv[1] ))
        return sys.argv[0], sys.argv[1]


def command_manager(command, option) : 
    """ """
    
    if not command  : 
        print("error you have to chose an command" )

    elif command == "auto-launch" : 
        auto_launch(option)

    elif command == "start" :
        start()

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
        print("error : command not reconized")