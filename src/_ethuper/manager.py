#!/usr/bin/env python3
#--*-- coding: utf-8 --*--



import argparse, os, system



def arg_manager() : 
    """ """

    return command, option


def command_manager(command, option) : 
    """ """
    
    if not command  : 
        print("error you have to chose an command" )

    elif command == "auto-launch" : 
        auto_launch()

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

    elif command == "man" : 
        man()

    elif command == "unistall" : 
        unistall(option)

    else : 
        print("error : command not reconized")