import sys, os
from subprocess import *

def run_cmd(cmd):
# runs whatever in the cmd variable
    p = Popen(cmd, shell=True, stdout=PIPE)
    output = p.communicate()[0]
    return output
  
source_path = sys.argv[1]

if os.path.isdir(source_path) == True:
    file_list = os.listdir(source_path)
    print file_list
