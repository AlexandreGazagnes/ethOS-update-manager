#!/usr/bin/env python3
# -*- coding: utf-8 -*-



# import 

import os, subprocess, pickle, time

from logging import debug, warning, info
import logging



# Constants

DATA_FOLDER = "/home/alex/ethOS-update-manager/data/"
debug(DATA_FOLDER)

DATA_FILE = "update.csv" 
debug(DATA_FILE) 

COUNTER_FILE = ".counter" 
debug(COUNTER_FILE) 

TEMP_FILE = "update.temp" 
debug(TEMP_FILE) 

VAR_FOLDER = "/home/alex/ethOS-update-manager/src/var"
debug(VAR_FOLDER)
