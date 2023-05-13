from gpiozero import MotionSensor

# Initialize motion sensors
pir = MotionSensor(4)
pir2 = MotionSensor(14)

# Initialize counter
counter = 0

# Define a function to read the sensor value and update the counter
def update_counter():
    global counter
    if pir.value == 1:
        counter += 1
    elif pir2.value == 1:
        counter -= 1
    print(counter)

# Add an event listener for the sensor pins
pir.when_motion = update_counter
pir2.when_motion = update_counter

# Run an infinite loop to keep the script running
while True:
    pass
