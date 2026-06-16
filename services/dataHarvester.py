import os
import spidev
import RPi.GPIO as GPIO
import serial, time, struct, zlib, base64
from PIL import Image


#Camera!!!

os.system("rpicam-jpeg -o /home/pi/Documents/photo.jpg -q 50 --nopreview")




#spi = spidev.SpiDev()
#spi.open(0, 0)
#spi.max_speed_hz = 1350000
#runCount = 0
#uvData = []
#
#def read_channel(ch):
#    cmd = [1, (8+ch)<<4, 0]
#    reply = spi.xfer2(cmd)
#    value = ((reply[1] & 3) << 8) + reply[2]
#    return value
#
#while runCount < 18000: #Gather Data for 5 minutes
#    uv = read_channel(0)
#    uvData.append(uv)
#    
#    time.sleep(1)
#    runCount += 1
#

#avgUV = sum(uvData) // len(uvData)

IMAGE = "/home/pi/Documents/photo.jpg"
PAYLOAD = 50          # raw bytes per chunk (before base64)
PACKET_GAP = 0.5     # seconds between packets — tune if you drop data

M0, M1 = 22, 27
GPIO.setmode(GPIO.BCM); GPIO.setwarnings(False)
GPIO.setup(M0, GPIO.OUT); GPIO.setup(M1, GPIO.OUT)
GPIO.output(M0, 0); GPIO.output(M1, 0)   # normal mode
time.sleep(0.5)

s = serial.Serial("/dev/serial0", 9600, timeout=1)

with open(IMAGE, "rb") as f:
    data = f.read()

chunks = [data[i:i+PAYLOAD] for i in range(0, len(data), PAYLOAD)]
total = len(chunks)
print(f"{len(data)} bytes -> {total} chunks")

# START frame: marker + total count
s.write(b"<START>" + struct.pack(">H", total) + b"\n")
time.sleep(PACKET_GAP)

for seq, chunk in enumerate(chunks):
    crc = zlib.crc32(chunk) & 0xFFFFFFFF
    raw = struct.pack(">HI", seq, crc) + chunk     # 2-byte seq, 4-byte crc, payload
    line = base64.b64encode(raw) + b"\n"           # text-safe, newline-terminated
    s.write(line)
    print(f"sent {seq+1}/{total}")
    time.sleep(PACKET_GAP)

s.write(b"<END>\n")
s.write(b"<END>\n")
s.write(b"<END>\n")
print("done")




