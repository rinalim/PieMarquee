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
   adv_romfile = run_cmd("ps -aux | grep advmame/bin/advmame | grep -v 'grep' | awk '{print $12}'")
   if words[0] == "maintitle" and len(adv_romfile) <= 1: 
       romfile = "maintitle"
   else:
       if len(adv_romfile) > 1 :
           system = "mame-advmame"
           romfile = adv_romfile.replace("\n","")
