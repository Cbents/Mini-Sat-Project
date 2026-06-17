from gpiozero import AngularServo
from time import sleep

# Initialize the servo on GPIO 18 with 180-degree limits
servo1 = AngularServo(12, min_angle=0, max_angle=180)

servo1.angle = 90

# Servo TWO!!!!
servo2 = AngularServo(32, min_angle=0, max_angle=180)

servo2.angle = 90

servo3 = AngularServo(35, min_angle=0, max_angle=180)

servo3.angle = 45

sleep(2) # Wait 2 seconds so it has time to reach the position

servo1.close() # Safely clean up the pin
servo2.close() # Safely clean up the pin
servo3.close()
