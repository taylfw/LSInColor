#!/usr/bin/env python3

import subprocess

class bcolors:
    GROUPOWNER = '\033[95m'
    FILE = '\033[94m'
    PERMISSIONS = '\033[96m'
    USEROWNER= '\033[92m'
    SIZE = '\033[93m'
    TIME = '\033[91m'
    SYM = '\033[31m'
    LINKD = '\033[36m'

contents = subprocess.Popen(["ls -l"], stdout=subprocess.PIPE, shell=True)
(out, err) = contents.communicate()

out = str(out).strip("b'total 4").split("\\")

for i in out:

    i = i.lstrip('n').split()
    
    if len(i) == 9:
        print(
              bcolors.PERMISSIONS +i[0],
              bcolors.USEROWNER+ i[2],
              bcolors.GROUPOWNER+ i[3],
              bcolors.SIZE + i[4],
              bcolors.TIME + i[5],
              bcolors.TIME + i[6], 
              bcolors.TIME + i[7],  
              bcolors.FILE + i[8]
            )
    elif len(i) == 11:
        print(
              bcolors.PERMISSIONS +i[0],
              bcolors.USEROWNER+ i[2],
              bcolors.GROUPOWNER+ i[3],
              bcolors.SIZE + i[4],
              bcolors.TIME + i[5],
              bcolors.TIME + i[6], 
              bcolors.TIME + i[7],  
              bcolors.FILE + i[8],
              bcolors.SYM + i[9],
              bcolors.LINKD + i[10]
        )
