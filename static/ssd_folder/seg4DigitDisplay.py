# Import required libraries
import sys
import RPi.GPIO as GPIO
import time

class SevSegDisp():
    

# print(str(get_counter()))
# toDisplay= str(get_counter()) # numbers and digits to display
    def __init__(self):
        print("initializing ssd")
        self.toDisplay = "0000"

        self.delay = 0.005 # delay between digits refresh

# --------------------------------------------------------------------
# PINS MAPPING AND SETUP
# selDigit activates the 4 digits to be showed (0 is active, 1 is unactive)
# display_list maps segments to be activated to display a specific number inside the digit
# digitDP activates Dot led
# --------------------------------------------------------------------

        self.selDigit = [14,15,18,23]
# Digits:   1, 2, 3, 4

        self.display_list = [24,25,8,7,1,12,16] # define GPIO ports to use
#disp.List ref: A ,B ,C,D,E,F ,G

        self.digitDP = 20
#DOT = GPIO 20
        
        # DIGIT map as array of array ,
        #so that arrSeg[0] shows 0, arrSeg[1] shows 1, etc
        self.arrSeg = [[0,0,0,0,0,0,1],\
                  [1,0,0,1,1,1,1],\
                  [0,0,1,0,0,1,0],\
                  [0,0,0,0,1,1,0],\
                  [1,0,0,1,1,0,0],\
                  [0,1,0,0,1,0,0],\
                  [0,1,0,0,0,0,0],\
                  [0,0,0,1,1,1,1],\
                  [0,0,0,0,0,0,0],\
                  [0,0,0,0,1,0,0]]
        
        self.ssd_GPIO = GPIO

    def gpio_init(self):
# Use BCM GPIO references instead of physical pin numbers
        self.ssd_GPIO.setmode(self.ssd_GPIO.BCM)

        # Set all pins as output
        self.ssd_GPIO.setwarnings(False)
        for pin in self.display_list:
          self.ssd_GPIO.setup(pin,self.ssd_GPIO.OUT) # setting pins for segments
        for pin in self.selDigit:
          self.ssd_GPIO.setup(pin,self.ssd_GPIO.OUT) # setting pins for digit selector
        self.ssd_GPIO.setup(self.digitDP,self.ssd_GPIO.OUT) # setting dot pin
        self.ssd_GPIO.setwarnings(True)

        self.ssd_GPIO.output(self.digitDP,0) # DOT pin

# --------------------------------------------------------------------
# MAIN FUNCTIONS
# splitToDisplay(string) split a string containing numbers and dots in
#   an array to be showed
# showDisplay(array) activates DIGITS according to array. An array
#   element to space means digit deactivation
# --------------------------------------------------------------------

    def showDisplay(self, digit):
     for i in range(0, 4): #loop on 4 digits selectors (from 0 to 3 included)
      sel = [0,0,0,0]
      sel[i] = 1
      self.ssd_GPIO.output(self.selDigit, sel) # activates selected digit
      
#       print("Digit:", digit)
      
      if digit[i].replace(".", "") == ".": # space disables digit
       self.ssd_GPIO.output(self.display_list,0)
       continue
      numDisplay = int(digit[i].replace(".", ""))
      self.ssd_GPIO.output(self.display_list, self.arrSeg[numDisplay]) # segments are activated according to digit mapping
      if digit[i].count(".") == 0:
       self.ssd_GPIO.output(self.digitDP,1)
      else:
       self.ssd_GPIO.output(self.digitDP,0)
      time.sleep(self.delay)

    def splitToDisplay (self, toDisplay): # splits string to digits to display
     
#      print("toDisplay:", toDisplay)
     
     arrToDisplay=list(toDisplay)
     for i in range(len(arrToDisplay)):
      if arrToDisplay[i] == ".": arrToDisplay[(i-1)] = arrToDisplay[(i-1)] + arrToDisplay[i] # dots are concatenated to previous array element
     while "." in arrToDisplay: arrToDisplay.remove(".") # array items containing dot char alone are removed
     
#      print("ArrToDisplay:", arrToDisplay)
     
     return arrToDisplay

    # --------------------------------------------------------------------
    # MAIN LOOP
    # persistence of vision principle requires that digits are powered
    #   on and off at a specific speed. So main loop continuously calls
    #   showDisplay function in an infinite loop to let it appear as
    #   stable numbers display
    # --------------------------------------------------------------------

    def SSD_show(self, displayvar="0000"):
        try:
         self.gpio_init()
         if displayvar is None or displayvar == "":
             print("Displayvar is None")
             displayvar = "0000"
         print("Displayvar:", displayvar)
#          while True:
         self.showDisplay(self.splitToDisplay(displayvar))
         time.sleep(0.01)
        except KeyboardInterrupt:
         print('interrupted!')
         self.ssd_GPIO.cleanup()
        sys.exit()
        #copytest1


