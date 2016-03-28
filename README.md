This is the Pi Progress Stepper, follow your stepper turns with a progress bar !
------------------------------------------------------------------------

<p align="center">
  <img src="http://s12.postimg.org/itm0p51l9/12910901_10206020561495372_728780836_n.jpg">
  ![Screenshot](demo.gif)
</p>

Table of contents:
------------------

* [About](#about)
* [What do you need](#what-do-you-need)
* [Dependencies](#dependencies)
* [How to use it](#how-to-use-it)
* [License](#license)

<br>

#About

This code is a proof of concept for the use of steppers with lcd's.

The progress bar was meant to display the progress of the number of steps that the user inputs

Possible use cases:
		
 - sewing thread winder
 - food mixer timer 
 - wind pinwheel timer
 - others...
 
###What do you need

 - Raspberry Pi 2 or newer with internet connection 	
 -  i2c 16x2 lcd or similar
 - Stepper motor 
 - Stepper motor driver i.e. L289N
 - Jumper wires

###Dependencies

- SMBus

		sudo apt-get install python-smbus
- i2c_lib 

        sudo apt-get install i2c-tools
    

###How to use it


 - Test i2C to check your display address

        sudo i2cdetect -y 0 (256MB Raspberry Pi Model B)
        
        sudo i2cdetect -y 1 (512MB Raspberry Pi 2 ou newer)

 - Change the Address of your screen in lcddriver.py
 
        ADDRESS = 'Your display address'
    
 - Initialize your program with number of steps
 
    	sudo python stepperbar.py 'Number of steps'
    	
        	Ex.: sudo python stepperbar.py 120


###License
Copyright (c) 2016 Luís Soares

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
