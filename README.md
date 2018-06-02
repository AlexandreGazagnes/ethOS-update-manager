# ethOS-update-manager
<p>
  
## Version
0.2.1 
<p><p>

## Description

ethOS-update-manager is a short script continuously runing and managing results from cmd ``` update ``` or ``` show stats ```, and logging it in a readable way. It is a specific log manager designed to provided good data performance and to help miners to improve their productivity by tuning easily their ``` local.conf``` .

It is designed to be run directly from the device to avoid ssh breaking connection problem (common with ethOS 1.2.7 and 1.2.9)

You're free to use ``` update```  or ``` show stats```  command, but as ``` update```  push data to the server for each call, it is recommanded to use ``` show stats```.

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
$ chmod +x /home/ethos/ethOS-update-manager/launcher
$ chmod +x /home/ethos/ethOS-update-manager/ethOsUpdateManager/main.py
```

for manual launch but background work: 
```
$ /home/ethos/ethOS-update-manager/launcher
```

for manual launch but foreground work: 
```
$ /home/ethos/ethOS-update-manager/ethOsUpdateManager/main.py
```


create alias (shortcup for CLI) : 
```
$ echo "alias --your_shortcut--='/home/ethos/ethOS-update-manager/launcher'" >>  /home/ethos/.bashrc
```

for automatic program launch (background) at each ethos stratup : 
```
$ echo "/home/ethos/ethOS-update-manager/launcher" >> /home/ethos/.bashrc
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

