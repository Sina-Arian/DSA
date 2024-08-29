import subprocess
from subprocess import Popen, PIPE

hostname = "8.8.8.8"
process = subprocess.Popen(['ping','-c','5',hostname],
stdout=PIPE, stderr=PIPE)
stdout, stderr = process.communicate()
print(stdout)