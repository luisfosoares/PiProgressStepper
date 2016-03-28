**# PiProgressStepper**
### This is the Pi Progress Stepper, follow your stepper turns with a progress bar !
![alt tag](http://s13.postimg.org/u0gdbm52v/12921057_10206018122874408_179296024_n_png.jpg)
Contents:
- What do you need
- Dependencies
- How to use it


What do you need:
	- Raspberry Pi 2 or newer with internet connection
    - i2c 16x2 lcd or similar
    - Stepper motor 
    - Stepper motor driver i.e. L289N
    - Jumper wires
	
Dependencies:
    - SMBus  
        sudo apt-get install python-smbus
    - i2c_lib 
        sudo apt-get install i2c-tools
    

How to use it:
    - Test i2C to check your display address
        sudo i2cdetect -y 0 (256MB Raspberry Pi Model B)
        sudo i2cdetect -y 1 (512MB Raspberry Pi 2 ou newer)

    - Change the Address of your screen in lcddriver.py - 
        ADDRESS = 'Your display address'
    
    - Initialize your program with number of steps
    	sudo python stepperbar.py 'Number of steps'
        	Ex.: sudo python stepperbar.py 120
