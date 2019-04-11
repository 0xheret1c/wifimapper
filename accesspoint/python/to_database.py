#!/usr/bin/python3

import sys
import time
LOCATION = "LOCATION_A"
DEVICE_NUMBER = "1S"

def sendToDB(data):
    print(DEVICE_NUMBER + " " + LOCATION + " " + data, end ='')

while True:
    data = sys.stdin.readline()
    if(len(data) > 0):
        sendToDB(data)

