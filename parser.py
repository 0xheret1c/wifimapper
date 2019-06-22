#!/usr/bin/python3
from math import log10


class Circle:
    def __init__(self, radius, posX,posY):
        self.radius = radius
        self.posX = posX
        self.posY = posY
    

def dbmToMeter(dBm):
    frequency = 2417 #MHz
    fspl = 27.55 # Free-Space Path Loss adapted avarage constant for home WiFI routers and following units
    distance = 10 ** (( fspl - (20 * log10(frequency)) + dBm ) / 20 )
    return round(distance,4)

def calculatePosition(circleA, circleB, circleC):
    

def calculateInterception(circleA,circleB):

