import time
from grovepi import *
import math

LED = 5 #port for LED
button = 4 #port for button

pinMode(LED,"OUTPUT")   #Assign mode for buzzer as output
pinMode(button,"INPUT")   #Assign mode for Button as input
while True:
        try:
                button_status= digitalRead(button)   #Read the Button status
                if button_status:   # if the button is in high position, run the program
                    digitalWrite(LED,1)  #print \Buzzing
                else:       #if button is off, print "off" on the screen
                    digitalWrite(LED,0)
                    #print "Off"
            except KeyboardInterrupt:
                digitalWRite(LED,0)
                break
            except(IOError,TypeError)as e:
                    print("Error")