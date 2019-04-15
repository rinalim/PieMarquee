#!/usr/bin/python

import os
from subprocess import *
from time import *

INTRO = "/opt/retropie/configs/all/PieMarquee/intro.mp4"

def run_cmd(cmd):
# runs whatever in the cmd variable
    p = Popen(cmd, shell=True, stdout=PIPE)
    output = p.communicate()[0]
    return output

if os.path.isfile(INTRO) == True:
    run_cmd("omxplayer --display 4 " + INTRO)

cur_imgpath = ""
while True:
    sleep_interval = 1
    romname = ""
    sysname = ""
    ps_grep = run_cmd("ps -aux | grep emulators | grep -v 'grep'")
    if len(ps_grep) > 1: 
        words = ps_grep.split()
        if 'advmame' in ps_grep:
            sysname = "mame-advmame"
            romname = words[-1]
        else:
            for i in words:
                if 'roms' in i:
                    path = i
                    break
            sysname = path.replace('"','').split("/")[-2]
            romname = path.replace('"','').split("/")[-1].split(".")[0]

    elif os.path.isfile("/tmp/PieMarquee.log") == True:
        f = open('/tmp/PieMarquee.log', 'r')
        line = f.readline()
        f.close()
        words = line.split()
        if len(words) == 2: # In the gamelist: Game /home/pi/.../*.zip
            sysname = words[1].replace('"','').split("/")[-2]
            romname = words[1].replace('"','').split("/")[-1].split(".")[0]
            sleep_interval = 0.1 # for quick view
        elif len(words) == 1:
            if words[0] == "SystemView":
                romname = "maintitle"
            else:
                romname = words[0]

    else:
        romname = "maintitle"
   
    if os.path.isfile("/home/pi/PieMarquee/marquee/" + romname + ".png") == True:
        imgpath = romname
    elif os.path.isfile("/home/pi/PieMarquee/marquee/" + sysname + ".png") == True:
        imgpath = sysname
    else:
        imgpath = "maintitle"
        
    #print romname
    if imgpath != cur_imgpath:
        #print imgpath 
        run_cmd("killall -9 pngview")
        os.system("/usr/bin/pngview -d4 /home/pi/PieMarquee/marquee/" + imgpath + ".png &")
        cur_imgpath = imgpath

    sleep(sleep_interval)
