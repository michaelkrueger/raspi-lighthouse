import time

from neopixel import *

import argparse
import signal
import sys


class Strip:

  # LED strip configuration:
  LED_COUNT      = 45      # Number of LED pixels.
  LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
  LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
  LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
  LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
  LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
  LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
               
  LED_STRIP      = 0x00081000   # Strip type and colour ordering


  def __init__():
    # Create NeoPixel object with appropriate configuration.
    self.strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
    # Intialize the library (must be called once before other functions).
    self.strip.begin()
  
  def zeile_1(color):
    colorWipe(color, range(0,15), 5)
	
  def zeile_2(color):
    colorWipe(color, range(16,30), 5)
	
  def zeile_3(color):
    colorWipe(color, range(31,45), 5)
	
  def test():
    print ('Theater chase animations.')
    theaterChase(self.strip, Color(127, 127, 127))  # White theater chase
    theaterChase(self.strip, Color(127,   0,   0))  # Red theater chase
    theaterChase(self.strip, Color(  0,   0, 127))  # Blue theater chase
    print ('Rainbow animations.')
    rainbow(self.strip)
    rainbowCycle(self.strip)
    theaterChaseRainbow(self.strip)
	
  # Define functions which animate LEDs in various ways.
  def colorWipe(color, range = range(self.strip.numPixels()), wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range:
        self.strip.setPixelColor(i, color)
        self.strip.show()
        time.sleep(wait_ms/1000.0)

  def theaterChase(color, wait_ms=50, iterations=10):
    """Movie theater light style chaser animation."""
    for j in range(iterations):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                self.strip.setPixelColor(i+q, color)
            self.strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 3):
                self.strip.setPixelColor(i+q, 0)

  def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)

  def rainbow(wait_ms=20, iterations=1):
    """Draw rainbow that fades across all pixels at once."""
    for j in range(256*iterations):
        for i in range(self.strip.numPixels()):
            self.strip.setPixelColor(i, wheel((i+j) & 255))
        self.strip.show()
        time.sleep(wait_ms/1000.0)

  def rainbowCycle(wait_ms=20, iterations=5):
    """Draw rainbow that uniformly distributes itself across all pixels."""
    for j in range(256*iterations):
        for i in range(self.strip.numPixels()):
            self.strip.setPixelColor(i, wheel((int(i * 256 / self.strip.numPixels()) + j) & 255))
        self.strip.show()
        time.sleep(wait_ms/1000.0)

  def theaterChaseRainbow(wait_ms=50):
    """Rainbow movie theater light style chaser animation."""
    for j in range(256):
        for q in range(3):
            for i in range(0, self.strip.numPixels(), 3):
                self.strip.setPixelColor(i+q, wheel((i+j) % 255))
            self.strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, self.strip.numPixels(), 3):
                self.strip.setPixelColor(i+q, 0)        