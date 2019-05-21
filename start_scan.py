#!/usr/bin/python3
import os
import sys
import subprocess

#Export env
os.system("./monitormode.sh on")
os.system("./dump.sh")
os.system("./monitormode.sh off")
