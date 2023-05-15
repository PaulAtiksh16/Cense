from flask import Flask, render_template, jsonify
from gpiozero import MotionSensor
from ssd_folder.seg4DigitDisplay import SevSegDisp
import threading

ssd = SevSegDisp()

# Initialize counter
counter = 0
counterstr = ""

# Initialize motion sensors
pir = MotionSensor(4) #blue/white sensor: 4
pir2 = MotionSensor(17) #green sensor: 17

# Define a function to read the sensor value and update the counter
def update_counter():
    global counter
    global counterstr
    if pir.value == 1:
        counter += 1
    if pir2.value == 1:
        counter -= 1
    if counter < 0:
        counter = 0
    
    counterstr = str(counter)
    counterstr = counterstr.rjust(4, "0")
    
    print("Counter:", counter)
    print("Counterstr:", counterstr)
    
    ssd.SSD_show(counterstr)
    
    
    

# Add an event listener for the sensor pins
pir.when_motion = update_counter
pir2.when_motion = update_counter


app = Flask(__name__, template_folder='/home/admin/Desktop/Cense2.0/templates')

@app.route('/')
def index():
    global counter
    templateData = {
        'title': 'LIBRARY OCCUPANCY',
        'counter': counter
    }
    return render_template('index.html', **templateData)

@app.route('/counter')
def get_counter():
    global counter
    return jsonify(counter=counter)

# def ssdtaskfunc():
#     global counterstr
#     print("Counter in task:", counterstr)
#     ssd.SSD_show(counterstr)
# 
# ssdthread = threading.Thread(target=ssdtaskfunc, name="ssdthread")

if __name__ == '__main__':
#     ssdthread.start()
    app.run(debug=True, port=80, host='0.0.0.0')
#     ssd.SSD_show(counterstr)
