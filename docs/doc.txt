#!/bin/sh


ethOS-update-manager : ethuper



In the following text or in files / scripts, ethOS-update-manager will be replaced by ethuper which stands for ETHos UPdate managER.

DESCRIPTION

ethOS-update-manager is complete solution deisgned to run, log, manage and reboot (if needed) automaticly yours miners.

Two main features are runing / managing results from cmd update or show stats, logging it in a readable way, and providing a complete automatic reboot manager to prevent overwarming, gpu failure and under performance issues by rebooting (hard or soft way), allowing and/or restarting miner.

As a log/performance manager, it is designed to provide good and helpful data information, and to help miners to improve their productivity by tuning in an easier way their local.conf.

As a rebooting manager, it is designed to provide a clever solution to increase uptime by rebooting, allowing, restarting with specific strategy for each problem.

Every log, reboot, allow or restart option is handly configurable with the ethuper command. See bellow or doc/ for dull information.

It is designed to be run directly from the device to avoid ssh breaking connection problem (common with ethOS 1.2.7 and 1.2.9)

You're free to use update or show stats command, but as update push data to the server for each call, it is recommanded to use show stats.



VERSION

0.3.0



LICENCE

GNU General Public License v3.0



REQUIREMENTS

python : 3.4.3 + (default ethOS python3)

ethos : 1.3.1+

hardware : -



DOWNLOAD

Just type :

$ cd
$ git clone https://github.com/AlexandreGazagnes/ethOS-update-manager.git



INSTALL
Auto

Just type :

$ cd
$ chmod +x ethOS-update-manager/install
$ ethOS-update-manager/install

Warning : Your system will reboot after 3 seconds, nothing unusual by the way
Manual

Considering the folder ethOS-update-manager in filepath /home/ethos/ so as $ ls /home/ethos/ethOS-update-manager returning ethOS-update-manager/

Prepare program and folder/file :

$ cd
$ chmod +x /home/ethos/ethOS-update-manager/autolaunch-updater
$ chmod +x /home/ethos/ethOS-update-manager/ethuper
$ chmod +x /home/ethos/ethOS-update-manager/_ethuper/updater.py
$ chmod +x /home/ethos/ethOS-update-manager/_ethuper/ethuper.py

Create alias (shortcup for CLI) :

$ echo "alias ethuper='/home/ethos/ethOS-update-manager/ethuper'" >>  /home/ethos/.bashrc

For automatic program launch (background) at each ethos stratup :

$ echo '/home/ethos/ethOS-update-manager/autolaunch-updater' >> /home/ethos/.bashrc

Reboot to update .bashrc

$ r



USAGE

Just type :

$ ethuper [COMAND] [OPTION]

where COMMAND is :

    auto-launch : updater auto launched or not when booting ethos + OPTION :
        on : enable (DEFAULT and RECOMMENDED)
        off : disable

    start : start at command + OPTION :
        fg : foreground, print out on stdout all info
        bg : background, dont not show any info about logging (DEFAULT and RECOMMENDED)

    stop : stop at command

    restart : stop and start at command to enable configs modification - RECOMMANDED after [CONFIG] - [SET] or [RESET]

    config : manage configs + OPTION:
        set : set specific config parametre(s)
        reset : reset all parametres to orginal configuration
        show : print out all parametres in use

    reboot-aut : set auto reboot autorisation to enale automatic rig management mode. Rig will reboot when GPUs no detected/no working, hrate obvious problem, overwarming. (Full list in doc/) + OPTION:
        on : enable (DEFAULT and RECOMMENDED)
        off : disable
        set : set specific auto reboot parametre(s) : temp, hrate...
        reset : reset all parametres to orginal configuration
        show : print out all parametres in use

    merge-files : merge all update files

    man : acces to manual (eg doc/)

    unistall : uninstall entire programm, setting original conf and deletting dependencies + OPTION :
        hard : -- WARNING -- delete all datafiles and log files
        medium : unistall but Keep all datafiles and log files
        soft : unistall but reinstall from scrach by saving data and logs files (DEFAULT and RECOMMENDED)



FOLDERS

    data : data file(s) created
    doc : full documentation
    logs : logs files stdout and stdr
    src : contain core code, scripts and libraires, FEEL FREE TO READ NOT TO CHANGE
    tests : standard test collection
    utils : various scripts to clean, merge, split, manipulate you data files



CONTRIBUTING

Feel free to submit any issues / pull resquest you want

Clone, download and fork at will

Staring and following also strongly recommended



DEV

    develop an alarm manager to send sms, twitter, mail, telegram (...) warning logs.
    create config command to handle reset show set configs of all variables.
    transform in standalone program with argc/argv manager and full doc.
    pip ?
    use logging with log external file
    write full doc, utils and test



DONATION

Feel free to make a BTC / ETH / XMR / ZEC or any coin you want to NPO :)



BONUS

Find bellow various helpful aliases for very popular command

nano

alias BASHRC='nano .bashrc'
alias LOCAL='nano local.conf'

on / off

alias DISALLOW='disallow and minestop'
alias ALLOW='allow && minestart'
alias R='allow && minestart && r'

show

alias SHOWMINER='show miner'
alias SHOWSTATS='show stats'

azerty

alias qwerty='setxkbmap fr'



    © 2018 GitHub, Inc.
    Terms
    Privacy
    Security
    Status
    Help

    Contact GitHub
    API
    Training
    Shop
    Blog
    About


data

find here your data file(s)
if first launch

.counter created that not should be removed/touched/modified

update0.csv file created
for each reboot

if headers are correct, data file will be appended

if not, an new file update1.csv, update2.csv will be created
merging various data files

use utils/merge_datafiles.py
droping dupliacted data

use utils/drop_duplicated.py


tests

find here all testing scripts for ethOS-update-manager


utils

find here various scripts to handle, clean or manipulate your data files Warning every new file create in utils/ not in data/
drop duplicated

for each file in data/ search, find and drop duplicated data
merge datafiles

merge all data files in data/ in one

use drop_duplicated.py after to clean new file if needed
split gpu data

auto split gpu data into data file or in specific file for each gpu
