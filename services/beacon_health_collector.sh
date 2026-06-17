#!/bin/bash
# This code will ONLY work on a RasPi

POWER=$(vcgencmd get_throttled)
# check current power status (over,under) max output = 15 bytes

PITEMP=$(vcgencmd measure_temp)
# check temperature max output = 16 bytes

CAMTEMP=$(python3 cam_temp.py)

DATENOW=$(date -u)
# check date/time UTC format

LASTERROR=$(date -r /logs/errors.log) # PLEASE PUT ABSOLUTE PATH
# Last time error log updated

echo "Power $POWER Temp $PITEMP Date $DATENOW Last Error $LASTERROR" >> # PLEASE PUT ABSOLUTE PATH
