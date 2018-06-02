# ethOS-update-manager
<p>
  
## VERSION
0.3.0
<p><p>

##  DESCRIPTION

ethOS-update-manager is a short script continuously runing and managing results from cmd ``` update ``` or ``` show stats ```, and logging it in a readable way. It is a specific log manager designed to provided good data performance and to help miners to improve their productivity by tuning easily their ``` local.conf``` .

It is designed to be run directly from the device to avoid ssh breaking connection problem (common with ethOS 1.2.7 and 1.2.9)

You're free to use ``` update```  or ``` show stats```  command, but as ``` update```  push data to the server for each call, it is recommanded to use ``` show stats```.

<p><p>

##  LICENCE

GNU General Public License v3.0
<p><p>

##  REQUIREMENTS

python :   3.4.3 + (default ethOS python3)<p>
ethos :    1.3.1+ <p>
hardware : -
<p><p>

##  INSTALL

#### Auto
from ```/home/ethos/ ``` just type```git clone https://github.com/AlexandreGazagnes/ethOS-update-manager.git```
when download completed type : 
```
$ /home/ethos/ethOS-update-manager/install
```
your system will reboot after 3 seconds

<p><p>

#### Manual

considering the folder ``` ethOS-update-manager ``` in filepath ``` /home/ethos/ ```
so as ``` $ ls /home/ethos/ethOS-update-manager ``` returning ``` ethOS-update-manager/ ``` 

prepare program and folder/file : 
```
$ cd
$ chmod +x /home/ethos/ethOS-update-manager/launch
$ chmod +x /home/ethos/ethOS-update-manager/ethOsUpdateManager/main.py
$ rm /home/ethos/ethOS-update-manager/install
```

create alias (shortcup for CLI) : 
```
$ echo "alias --ethuper--='/home/ethos/ethOS-update-manager/launch'" >>  /home/ethos/.bashrc
```

for automatic program launch (background) at each ethos stratup : 
```
$ echo "/home/ethos/ethOS-update-manager/launch" >> /home/ethos/.bashrc
```

##  USAGE / TUTORIAL


Just run : ```ethuper [COMAND] [OPTION]``` where **COMMAND** is : 
* **autoboot** : laucnh autamiaticly when booting ethos (defaut) **+ OPTION** : 
  * able  
  * disable
* **start** : start at command **+ OPTION** : 
  * fg (foreground)
  * bg (background)
* **stop** : stop at command
* **config** : manage configs **+ OPTION**:  
  * set
  * reset 
  * show 
* **merge-files** : merge all update files 
* **man** : acces to manual
* **reboot** : reboot the entire programm setting original conf **+ OPTION** : 
  * hard : -- WARNING -- delete all datafiles and log files
  * soft : Keep all datafiles and log files 


<p><p>

##  FOLDERS
* data :                data file(s) created
* doc :                 full documentation 
* ethOsUpdateManager :  main.py (called by launch) and lib
* logs :                logs files stdout and stdr
* tests :               standard test collection
* utils :               various scripts to clean, merge, split, manipulate you data files

##  CONTRIBUING
feel free to submit any issues/pull resquest you want <p>
clone, download and fork at will 
<p><p>
  
##  REWARD

1 ETH for the 100th people to star the project :) 
<p><p>
  
##  MISC

nano
```
alias BASHRC='nano .bashrc'
alias LOCAL='nano local.conf'
```

ON/OFF
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

## DEV
* create config command to handle reset show set configs of all variables
* transform in standalone program with argc/argv manager and full doc
* progress to UpdateManager to RigManager with auto reboot 
* pip?
* use logging with log external file
* write full doc and utils and test
* find a new name 
* create an install who automaticly create alias and autorun in bashrc
