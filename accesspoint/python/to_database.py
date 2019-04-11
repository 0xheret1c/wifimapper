#!/usr/bin/python3

import sys
import time

while True:
    data = sys.stdin.readline()
    if(len(data) > 0):
        print(data, end ='')
        time.sleep(1/59)