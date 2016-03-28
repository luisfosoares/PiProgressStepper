import RPi.GPIO as GPIO
import time
import lcddriver
import sys
import math
from threading import Thread
from sys import argv

# Initializers
lcd = lcddriver.lcd()
lcd.lcd_clear()


# Variables
delay = 0.015
b=0
screenLenght = 16


# Number of steps of stepper - Input from console
steps = int(argv[1])


# Enable GPIO pins for  ENA and ENB for stepper
enable_a = 18
enable_b = 22

# Enable pins for IN1-4 to control step sequence
coil_A_1_pin = 23
coil_A_2_pin = 24
coil_B_1_pin = 4
coil_B_2_pin = 17

# Setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set pin states
GPIO.setup(enable_a, GPIO.OUT)
GPIO.setup(enable_b, GPIO.OUT)
GPIO.setup(coil_A_1_pin, GPIO.OUT)
GPIO.setup(coil_A_2_pin, GPIO.OUT)
GPIO.setup(coil_B_1_pin, GPIO.OUT)
GPIO.setup(coil_B_2_pin, GPIO.OUT)

# Set ENA and ENB to high to enable stepper
GPIO.output(enable_a, True)
GPIO.output(enable_b, True)

# Function for step sequence
def setStep(w1, w2, w3, w4):
  GPIO.output(coil_A_1_pin, w1)
  GPIO.output(coil_A_2_pin, w2)
  GPIO.output(coil_B_1_pin, w3)
  GPIO.output(coil_B_2_pin, w4)

# Create custo Chars [| , ||, |||, ||||] 
custom_char = [
        # network signal
        [ 0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x10 ],
        # right arrow
        [ 0x18, 0x18, 0x18, 0x18, 0x18, 0x18, 0x18, 0x18 ],
        # left arrow
        [ 0x1C, 0x1C, 0x1C, 0x1C, 0x1C, 0x1C, 0x1C, 0x1C ],
        # enter
        [ 0x1E, 0x1E, 0x1E, 0x1E, 0x1E, 0x1E, 0x1E, 0x1E ],
        # clock
        [ 0x1F, 0x1F, 0x1F, 0x1F, 0x1F, 0x1F, 0x1F, 0x1F ],
]

# Load chars in 
lcd.lcd_load_custom_chars(custom_char)

#Default strings for step and laps - 1st row
lcd.lcd_display_string("Step", 1, 0)
lcd.lcd_display_string("Lap", 1, 9)



# Display number of steps
def myfunc(i):
    total  = float (i) / float (steps)
    total = "%.1f" % (total*100)
    lcd.lcd_display_string(str(total)+ "%", 2, 10)

    
# Calculate number of complete blocks for progress bar
def frange(x, y, jump):
    while x <= y:
        yield x
        x += jump

# Calculate number of incomplete blocks for progress bar 
def incomplete_bars():
    barsCalculation =  totalBars*5
    bars = int (barsCalculation)
    if (bars == 0):
        return
    elif (bars == 1):
        lcd.lcd_write_char(0)
        return
    elif (bars == 2):
        lcd.lcd_write_char(1)
        return
    elif (bars == 3):
        lcd.lcd_write_char(2)
        return
    elif (bars == 4):
        lcd.lcd_write_char(3)
        return
    else:
        print "Error - Incorrect number of bars"
        return

# Main loop
# Calculate and display steps
# Calculate and display progress bar
for step in range(1, steps+1):
    # Display steps
    lcd.lcd_display_string(str(step), 1, 5)
    # Display laps
    lcd.lcd_display_string(str((step/12)), 1,13)	

    # Make steps
    setStep(1,0,1,0)
    time.sleep(delay)
    setStep(0,1,1,0)
    time.sleep(delay)
    setStep(0,1,0,1)
    time.sleep(delay)
    setStep(1,0,0,1)
    time.sleep(delay)

    currentStepValue = int (step)
#    lcd.lcd_clear()
    
    #Display progress bar on 2nd row 
    # 0x80 row 1
    # 0xC0 row 2
    # 0x94 row 3
    # 0xD4 row 4
    lcd.lcd_write(0xC0)
    

    # Calculate number of complete bars
    totalBars = float(screenLenght)/float(steps)*float(currentStepValue)

    # Display complete bars
    if (totalBars >= 1):
        for i in frange(1,  totalBars , 1):
            lcd.lcd_write_char(4)
            b=totalBars

        totalBars=totalBars-b;

    # Display incomplete bars
    incomplete_bars()






