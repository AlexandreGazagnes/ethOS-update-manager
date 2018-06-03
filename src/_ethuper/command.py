#!/usr/bin/env python3
#--*-- coding: utf-8 --*--



# import 

import argparse, os, system



# functions

def auto_launch(option) : 
    """ """
    if option == "on" :
        pass 
    elif option == "fg" :
        pass 
    else : 
        print("option error")


def start(option) : 
    """ """

    if option == "fg" :
        pass 
    elif option == "bg" :

        # os.system(/home/ethos/ethOS-update-manager/auto-launch)
        pass 
    else : 
        print("option error")
    

def stop() : 
    """ """
    pass
    # os.system(stop updater.py)


def restart() : 
    """ """
    pass
    # os.system(stop updater.py)
    # os.system(/home/ethos/ethOs-update-manager/auto-launch)


def config(option) : 
    """ """
    if option == "set" :
        pass 
    elif option == "reset" :
        pass 
    elif option == "show" :
        pass 
    else : 
        print("option error")


def reboot_aut(option) : 
    """ """
    
    if option == "on" : 
        pass
    elif option == "off" : 
        pass
    elif option == "set" :
        pass 
    elif option == "reset" :
        pass 
    elif option == "show" :
        pass 
    else : 
        print("option error")


def merge_files() : 
    """ """
    pass 
    # os.system(/home/ethos/ethOS-update-manager/utils/merge-files.py)


def man(): 
    """ """
    pass
    # print /home/ethos/ethOS-update-manager/docs/doc.txt


def unistall(option) :
    """ """ 
    if option == "hard" : 
        pass
    elif option == "medium" : 
        pass
    elif option == "soft" :
        pass 
    else : 
        print("option error")

