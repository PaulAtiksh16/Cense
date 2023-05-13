import RPi.GPIO as GPIO
from gpiozero import MotionSensor
import time
import threading

GPIO.setmode(GPIO.BOARD)

# GPIO.setmode(GPIO.BCM)
# GPIO.setup(4, GPIO.IN)

pir = MotionSensor(4)
pir2 = MotionSensor(14)

print("bwo")

# Set up GPIO pins
GPIO.setmode(GPIO.BOARD)

# Initialize counter
counter = 0

# Define a function to read the sensor value and update the counter
# CHANGE THIS FUNCTION TO INCREMENT/DECREMENT BASED OFF SENSORS
def increment_counter():
    global counter
    if pir.wait_for_motion():
        counter += 1
    pir.wait_for_no_motion()
    print(counter)
    
def decrement_counter():
    global counter
    if pir2.wait_for_motion():
        counter -= 1
    pir.wait_for_no_motion()
    print(counter)
    
increment_thread = threading.Thread(target=increment_counter)
decrement_thread = threading.Thread(target=decrement_counter)

# Add an event listener for the sensor pin
# GPIO.add_event_detect(4, GPIO.BOTH, callback=update_counter)

# Run an infinite loop to keep the script running
while True:
#     increment_counter()
#     decrement_counter()
    increment_thread.start()
    decrement_thread.start()