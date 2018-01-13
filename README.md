# raspi-lighthouse

A raspi-lightpanel that is controlled by a webserver written in python.

# Running

  - cmd>  ./startup.sh
  
A Webserver will start and listen on Port 5000:
![Webserver](/build-instructions/Web-Frontend.png)

# Build you own lighthouse
 
[The Build-Instructions are located here](/build-instructions/readme.md)

# Dependencies

  - Python and the WS2812 GPIO library from here
    * https://tutorials-raspberrypi.de/raspberry-pi-ws2812-ws2811b-rgb-led-streifen-steuern/
	* Git-Repo: git clone https://github.com/jgarff/rpi_ws281x
	* Perform the build and setup-steps
	* pip install .
  - Install Python pip:
    * apt-get update && apt-get install python-pip
  - Python Flask Framework as a Webserver
    * http://flask.pocoo.org/docs/0.12/tutorial/#tutorial
  - Create a symbolic link to neopixel.py in lighthouse_web/lighthouse_web
    * ln -s ../../../rpi_ws281x/python/neopixel.py .
	
	
# Autostart

   - Add the following line to /etc/rc.local before "exit 0"
   /home/pi/raspi-lighthouse/startup.sh
 
# Installation 


## Python Libs

###Initial Setup

  - sudo raspi-config
    * Setup Hostname
	* Change Password of user pi
	* Change Keyboardlayout & Locale
	* Enable ssh
  - sudo apt-get update
  - sudo apt-get install gcc make build-essential python-dev git scons swig python-pip
  - Deactivate Audio (Create file)
    sudo nano /etc/modprobe.d/snd-blacklist.conf
	Add line: 
	blacklist snd_bcm2835
	
  - Edit file 
    sudo nano /boot/config.txt
	Deactivate Line: dtparam=audio=on 
	
  - sudo reboot
  
### Install Python Libs

  - cd ~
  - git clone https://github.com/jgarff/rpi_ws281x
  - cd rpi_ws281x/
  Build SCons
  - sudo scons
  
  Python build & Installation
  - cd python
  - sudo python setup.py build
  - sudo python setup.py install
  
### Configure and Test

  - cd examples
  - nano strandtest.py
  Set LED_COUNT=45  
  Start the test
  - sudo python strandtest.py
  
## Lighthouse Webserver

### Download

  - cd ~
  - git clone https://github.com/michaelkrueger/raspi-lighthouse.git
  - cd raspi-lighthouse
  - chmod +x startup.sh
  - cd lighthouse_web
  - sudo python setup.py build
  - sudo python setup.py install  
  - sudo pip install .
  
  
### Start / Register as service
  
  
