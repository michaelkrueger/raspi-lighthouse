# raspi-lighthouse
A raspi-lightpanel that is controlled by a webserver written in python.

# Running
  - cmd>  cd lighthouse_web/lighthouse_web
  - cmd>  export FLASK_APP="lighthouse_web"
  - cmd>  flask run --host=0.0.0.0
  

# Dependencies

  - Python and the WS2812 GPIO library from here
    * https://tutorials-raspberrypi.de/raspberry-pi-ws2812-ws2811b-rgb-led-streifen-steuern/
	* Git-Repo: git clone https://github.com/jgarff/rpi_ws281x
  - Install Python pip:
    * apt-get update && apt-get install python-pip
  - Python Flask Framework as a Webserver
    * http://flask.pocoo.org/docs/0.12/tutorial/#tutorial
	
	
  