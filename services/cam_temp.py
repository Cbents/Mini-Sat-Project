import time
from w1thermsensor import W1ThermSensor
sensor = W1ThermSensor()
# CAMERA Temperature sensor

try:
    while True:
        temperature = sensor.get_temperature()
        print("%s" % temperature)
except Exception as err:
    pass
# Possibly add errors here to the watchdog/err logs
