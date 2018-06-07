#!/usr/bin/env python3
# -*- coding: utf-8 -*-



import os


# Constants

folder = os.getcwd()
folder = foler.split("/")
MAIN_FOLDER = "/{}/{}/ethOS-update-manager/".format(folder[0], folder[1])


DATA_FOLDER = MAIN_FOLDER+"data/"

DATA_FILE = "update.csv" 

COUNTER_FILE = ".counter" 

TEMP_FILE = "update.temp" 


VAR_FOLDER = MAIN_FOLDER+"src/var/"


DOC_FOLDER = MAIN_FOLDER+"docs/"


LOG_FOLDER = MAIN_FOLDER+"logs/"
