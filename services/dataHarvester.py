import os
import spidev
import time

#Camera!!!

os.system("rpicam-jpeg -o /home/pi/Documents/output.jpg -q 50 --nopreview")




spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1350000

def read_channel(ch):
    cmd = [1, (8+ch)<<4, 0]
    reply = spi.xfer2(cmd)
    value = ((reply[1] & 3) << 8) + reply[2]
    return value

while True:
    uv = read_channel(0)
    print("UV reading:", uv)
    time.sleep(1)

