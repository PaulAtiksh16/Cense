from flask import Flask, render_template
from gpiozero import MotionSensor


# Initialize counter
counter = 0

# Initialize motion sensors
pir = MotionSensor(4)
# pir2 = MotionSensor(14)

# Define a function to read the sensor value and update the counter
def update_counter():
    global counter
    if pir.value == 1:
        counter += 1
#     elif pir2.value == 1:
#         counter -= 1
    print(counter)

# Add an event listener for the sensor pins
pir.when_motion = update_counter
# pir2.when_motion = update_counter


app = Flask(__name__, template_folder='/home/admin/Desktop/Cense2.0/templates')
@app.route('/')
def index():
    global counter
    templateData = {
      'title' : 'LIBRARY OCCUPANCY',
      'occupancy': str(counter)
      }
    return render_template('index.html', **templateData)

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')
