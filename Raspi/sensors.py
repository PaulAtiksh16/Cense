import RPi.GPIO as GPIO

# Set up GPIO pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.IN) # sensor pin

# Initialize counter
counter = 0

# Define a function to read the sensor value and update the counter
# CHANGE THIS FUNCTION TO INCREMENT/DECREMENT BASED OFF SENSORS
def update_counter(channel):
    global counter
    if GPIO.input(channel):
        counter += 1
    else:
        counter -= 1

# Add an event listener for the sensor pin
GPIO.add_event_detect(18, GPIO.BOTH, callback=update_counter)

# Run an infinite loop to keep the script running
while True:
    # Do any other processing here
    pass
