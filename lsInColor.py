#!/usr/bin/env python3

import subprocess

class bcolors:
    GROUPOWNER = '\033[95m'
    FILE = '\033[32m'
    PERMISSIONS = '\033[96m'
    USEROWNER= '\033[92m'
    SIZE = '\033[93m'
    TIME = '\033[91m'
    SYM = '\033[31m'
    LINKD = '\033[36m'
    DIR = '\033[35m'

# Gather output of the ls -l command
contents = subprocess.Popen(["ls -l"], stdout=subprocess.PIPE, shell=True)
(out, err) = contents.communicate()

# Sanatize the output
out = str(out).split("\\")

# For each file in output, check the length and color accordingly.
for i in out:

    i = i.lstrip('n').split()

    
    
    # Check if the output is a directory.
    if len(i) == 9 and i[0][0] == 'd':
        
        print(
              bcolors.PERMISSIONS +i[0],
              bcolors.SYM + i[1],
              bcolors.USEROWNER+ i[2],
              bcolors.GROUPOWNER+ i[3],
              bcolors.SIZE + i[4],
              bcolors.TIME + i[5],
              bcolors.TIME + i[6], 
              bcolors.TIME + i[7],  
              bcolors.DIR + i[8],

            )
    # Coloring for Symbolic links.
    elif len(i) == 11:

        print(
              bcolors.PERMISSIONS +i[0],
              bcolors.SYM + i[1],
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
    # checks if the directory has space in title.
    elif len(i) == 10 and i[0][0] == 'd':
        print(
              bcolors.PERMISSIONS +i[0],
              bcolors.SYM + i[1],
              bcolors.USEROWNER+ i[2],
              bcolors.GROUPOWNER+ i[3],
              bcolors.SIZE + i[4],
              bcolors.TIME + i[5],
              bcolors.TIME + i[6], 
              bcolors.TIME + i[7],  
              bcolors.DIR + i[8],
              bcolors.DIR + i[9]
            )

    elif len(i) == 9:
        print(
              bcolors.PERMISSIONS +i[0],
              bcolors.SYM + i[1],
              bcolors.USEROWNER+ i[2],
              bcolors.GROUPOWNER+ i[3],
              bcolors.SIZE + i[4],
              bcolors.TIME + i[5],
              bcolors.TIME + i[6], 
              bcolors.TIME + i[7],  
              bcolors.FILE + i[8]
            )
    elif len(i) == 2:
        
        
        print(
            bcolors.SIZE + i[0],
            bcolors.SIZE + i[1]
            )
        
