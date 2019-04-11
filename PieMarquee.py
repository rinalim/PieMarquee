#!/usr/bin/python

import os
from subprocess import *
from time import *

def run_cmd(cmd):
# runs whatever in the cmd variable
    p = Popen(cmd, shell=True, stdout=PIPE)
    output = p.communicate()[0]
    return output

cur_romname = ""
while True:
   romname = "maintitle"
   ps_grep = run_cmd("ps -aux | grep emulator | grep -v 'grep' | awk '{print $12}'")
   if len(adv_romfile) > 1: 
       romename = ps_grep
   print romname
   sleep(1)

#path = '"/home/user/RetroPie/roms/arcade/1941.zip"'
#romname = path.replace('"','').split("/")[-1].split(".")[0
