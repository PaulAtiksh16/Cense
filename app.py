from gpiozero import MotionSensor
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/counter')
def get_counter():
    global counter
    return render_template('counter.html', counter=counter)

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
