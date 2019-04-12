#!/usr/bin/python2

import mysql.connector as mariadb
import sys
import time
LOCATION = "LOCATION_A"
AP_NUMBER = "0"
SERVER_IP = "127.0.0.1"
SERVER_PORT = "1337"
SERVER_USER = "mariadb"
SERVER_PASS = "root"



def connect():
    return mariadb.connect(host=SERVER_IP,port=SERVER_PORT,user=SERVER_USER, password=SERVER_PASS, database='data')

connection = connect()

def sendToDB(data):
    splt = data.split()
    if(len(splt) <= 0):
        return
    
    time = splt[0]
    strength = splt[6]
    source = splt[13].replace("SA:","")
    print("Time: " + time)
    print("Strength: " + strength)
    print("Source: " + source)
    print(" ")


    cursor = connection.cursor()
    cursor.execute("INSERT INTO captures (location,ap,time,strength,source) VALUES (%s,%s)", (LOCATION, AP_NUMBER,time,strength,source))


while True:
    data = sys.stdin.readline()
    if(len(data) > 0):
        sendToDB(data)

