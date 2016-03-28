# PiProgressStepper
This is the Pi Progress Stepper , controls your turns with a progress bar ! 



Dependencies:

    - SMBus  
        sudo apt-get install python-smbus
    - i2c_lib 
        sudo apt-get install i2c-tools
    

How to use it:
    -Test i2C to check your display address
        -sudo i2cdetect -y 0 (256MB Raspberry Pi Model B)
        -sudo i2cdetect -y 1 (512MB Raspberry Pi 2 ou newer)

    -Change the Address of your screen in lcddriver.py - 
        - ADDRESS = 'Your address'
        
![]({{site.baseurl}}/http://postimg.org/image/4uff4s3sj/)