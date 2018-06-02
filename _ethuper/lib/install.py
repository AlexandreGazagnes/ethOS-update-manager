#!/usr/bin/env python3
#--*--coding: utf-8 --*--


def install():

    with open("/home/ethos/ethOS-update-manager/_ethuper/var/install.pk", "r") as f : v = f.read()
      if v == "True" : 
        os.system("rm -f /home/ethos/ethOS-update-manager/install")
        with open("/home/ethos/ethOS-update-manager/_ethuper/var/install.pk", "w") as f : f.write("False")
