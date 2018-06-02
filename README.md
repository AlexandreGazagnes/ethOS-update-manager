# ethOS-update-manager
<br><br>
  
## VERSION
0.3.0
<br><br>

##  DESCRIPTION

ethOS-update-manager is a short script continuously runing/managing results from cmd ``` update ``` or ``` show stats ```, and logging it in a readable way. It is a specific log manager designed to provide good data performance and to help miners to improve their productivity by tuning in an easier way their ``` local.conf```.

It is designed to be run directly from the device to avoid ssh breaking connection problem (common with ethOS 1.2.7 and 1.2.9)

You're free to use ``` update```  or ``` show stats```  command, but as ``` update```  push data to the server for each call, it is recommanded to use ``` show stats```.
<br><br>
##  LICENCE

GNU General Public License v3.0
<br><br>

##  REQUIREMENTS

python :   3.4.3 + (default ethOS python3)<p>
ethos :    1.3.1+ <p>
hardware : -
<br><br>

##  DOWNLOAD

from ```/home/ethos/ ``` just type```git clone https://github.com/AlexandreGazagnes/ethOS-update-manager.git```
<br><br>

##  INSTALL

#### Auto
Considering the folder ``` ethOS-update-manager ``` in filepath ``` /home/ethos/ ```
so as ``` $ ls /home/ethos/ethOS-update-manager ``` returning ``` ethOS-update-manager/ ``` 

```
$ chmod +x /home/ethos/ethOS-update-manager/install
$ /home/ethos/ethOS-update-manager/install
```
Warning : Your system will reboot after 3 seconds, nothing unusual by the way


#### Manual

Considering the folder ``` ethOS-update-manager ``` in filepath ``` /home/ethos/ ```
so as ``` $ ls /home/ethos/ethOS-update-manager ``` returning ``` ethOS-update-manager/ ``` 

Prepare program and folder/file : 
```
$ cd
$ chmod +x /home/ethos/ethOS-update-manager/autolaunch-updater
$ chmod +x /home/ethos/ethOS-update-manager/ethuper
$ chmod +x /home/ethos/ethOS-update-manager/_ethuper/updater.py
$ chmod +x /home/ethos/ethOS-update-manager/_ethuper/ethuper.py
```


Create alias (shortcup for CLI) : 
```
$ echo "alias ethuper='/home/ethos/ethOS-update-manager/ethuper'" >>  /home/ethos/.bashrc
```

For automatic program launch (background) at each ethos stratup : 
```
$ echo '/home/ethos/ethOS-update-manager/autolaunch-updater' >> /home/ethos/.bashrc
```

Reboot to update .bashrc
```
$ r
```
<br><br>

##  USAGE / TUTORIAL


Just run : ```ethuper [COMAND] [OPTION]``` where **COMMAND** is : 
* **autoboot** : updater automatiticaly launched or not when booting ethos **+ OPTION** : 
  * on  : enable (default)
  * off : disable
* **start** : start at command **+ OPTION** : 
  * fg (foreground)
  * bg (background)
* **stop** : stop at command
* **config** : manage configs **+ OPTION**:  
  * set : set specific config parametre(s)
  * reset : reset all parametres to orginal configuration
  * show : print out all parametres in use
* **merge-files** : merge all update files 
* **man** : acces to manual (eg doc/)
* **reboot** : reboot the entire programm setting original conf **+ OPTION** : 
  * hard : -- WARNING -- delete all datafiles and log files
  * soft : Keep all datafiles and log files 


<br><br>

##  FOLDERS
* data :                data file(s) created
* doc :                 full documentation 
* _ ethuper :  			contain core code, scripts and libraires, free to read, not to change
* logs :                logs files stdout and stdr
* tests :               standard test collection
* utils :               various scripts to clean, merge, split, manipulate you data files
<br><br>

##  CONTRIBUING
Feel free to submit any issues/pull resquest you want <p>
Clone, download and fork at will <p>
Staring and following also strongly recomanded
<br><br>
  
##  MISC

Find bellow various helpful aliases for very popular command 
nano
```
alias BASHRC='nano .bashrc'
alias LOCAL='nano local.conf'
```

on / off
```
alias DISALLOW='disallow and minestop'
alias ALLOW='allow && minestart'
alias R='allow && minestart && r'
```

show
```
alias SHOWMINER='show miner'
alias SHOWSTATS='show stats'
```

azerty
```
alias qwerty='setxkbmap fr'
```
<br><br>

## DEV
* PARTIAL : find a new name 
* PARTIAL : create an install who automaticly create alias and autorun in bashrc

* create config command to handle reset show set configs of all variables
* transform in standalone program with argc/argv manager and full doc
* progress to UpdateManager to RigManager with auto reboot 
* pip?
* use logging with log external file
* write full doc and utils and test
<br><br>

##  DONATION
Feel free to make a BTC / ETH / XMR / ZEC or any coin you want to NPO :) 
<br><br>
