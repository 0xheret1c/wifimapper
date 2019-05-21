#!/bin/sh
DEVICE=$(printenv 'MONITOR_DEVICE') # Get the device from the enviorment.
while :
do
        echo "Hopping to channel $1"
        iwconfig $DEVICE channel $1
done

