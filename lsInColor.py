#!/usr/bin/env python3

import subprocess

class bcolors:
    GROUP = '\033[95m'
    FILE = '\033[94m'
    PERMISSIONS = '\033[96m'
    USERGRP= '\033[92m'
    SIZE = '\033[93m'
    TIME = '\033[91m'

contents = subprocess.Popen(["ls -l"], stdout=subprocess.PIPE, shell=True)
(out, err) = contents.communicate()

out = str(out)
out = out.strip("b'total 4")
out = out.split("\\")

for i in out:
    i = i.lstrip('n')
    i = i.split()
    
    if len(i) == 9:
        print(

              bcolors.PERMISSIONS +i[0],
              bcolors.USERGRP+ i[2],
              bcolors.GROUP+ i[3],
              bcolors.SIZE + i[4],
              bcolors.TIME + i[5],
              bcolors.TIME + i[6], 
              bcolors.TIME + i[7],  
              bcolors.FILE + i[8]
            )


