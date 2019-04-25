#!/usr/bin/python3
import os
import sys
import subprocess

#Export env
os.system("./monitormode.sh on")
sub = subprocess.Popen(["../bash/channelhopper.sh","5"])
os.system("./dump.sh")
os.system("./monitormode.sh off")
