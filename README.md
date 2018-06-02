# ethOS-update-manager
<p>
  
## Version
0.2.1 
<p><p>

## Description

This is a short script to manage results from cmd ``` update ``` or ``` show stats ``` and log it in a readable way. It is designed to be run directly from the device to avoid ssh breaking connection problem

You're free to use update or show stats command but, update push data to there server for each call, so it is not recommanded

<p><p>

## Licence

GNU General Public License v3.0
<p><p>

##  Requirements

python :   3.4.3 + (default ethOS python3)<p>
ethos :    1.3.1+ <p>
hardware : -
<p><p>

##  Installation
from ```/home/ethos/ ``` just ```git clone https://github.com/AlexandreGazagnes/ethOS-update-manager.git```
<p><p>

## Usage

considering the folder ``` ethOS-update-manager ``` in filepath ``` /home/ethos/ ```
so as ``` $ ls /home/ethos/ethOS-update-manager ``` returning ``` ethOS-update-manager/ ``` 

prepare program and folder/file : 
```
$ cd
$ mkdir /home/ethos/Script/
$ mv  ./ethOS-update-manager* /home/ethos/Script/
$ chmod +x ./Script/ethOS-update-manager/launcher
```

for manual launch : 
```
$ ./Script/ethOS-update-manager/launcher
```

create alias (shortcup for CLI) : 
```
$ echo "alias --your_shortcut--='./Script/ethOS-update-manager/launcher'" >>  /home/ethos/.bashrc
```

for program launch at ethos stratup, type in interpretor : 
```
$ echo "./Script/ethOS-update-manager/launcher" >> /home/ethos/.bashrc
```
<p><p>
  
## Contributing
feel free to submit any issues/pull resquest you want <p>
clone, download and fork at will 
<p><p>
  
## Reward

1 ETH for the 100th people to star the project :) 
<p><p>
  
##  Misc : useful aliases

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

