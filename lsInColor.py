import subprocess

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

contents = subprocess.Popen(["ls -l"], stdout=subprocess.PIPE, shell=True)
(out, err) = contents.communicate()

out = str(out)
out = out.strip("b'total 4")
out = out.split("\\")

for i in out:
    i = i.lstrip('n')
    print(
          bcolors.OKCYAN +i[0:10],
          bcolors.OKGREEN + i[11:26],
          bcolors.WARNING + i[27:30],
          bcolors.FAIL + i[31:43], 
          bcolors.OKBLUE + i[44:]
          )


