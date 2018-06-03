
#!/usr/bin/env python3
#--*-- coding: utf-8 --*--



""""
where COMMAND is :

    auto : updater auto launched or not when booting ethos + OPTION :
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

""""