#!/usr/bin/env python3
# -*- coding: utf-8 -*-



# import 

import os, subprocess, pickle, time

from logging import debug, warning, info
import logging

# do not use pandas on ethos 1.3.1



# Constants

DATA_FOLDER = "/home/ethos/ethOS-update-manager/data/"
debug(DATA_FOLDER)

DATA_FILE = "update.csv" 
debug(DATA_FILE) 

COUNTER_FILE = ".counter" 
debug(COUNTER_FILE) 

TEMP_FILE = "update.temp" 
debug(TEMP_FILE) 
