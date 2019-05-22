#!/usr/bin/python3
import os
import json
import sys

with open("./conf.json", 'r') as f:
    config = json.load(f)

dev = config["ap"]["network_monitor_dev"]

#Turn monitor-mode for DEVICE on.
def on():
	os.system("ifconfig" + dev + "down")
	os.system("iwconfig" + dev + "mode monitor")
	os.system("ifconfig" + dev + "up")


#Turn monitor-mode for DEVICE off.
def off():
	os.system("ifconfig" + dev + "down")
	os.system("iwconfig" + dev + "mode managed")
	os.system("ifconfig" + dev + "up")


if (sys.argv[0] == "on"):
	on()
elif (sys.argv[0] == "off"):
	off()


