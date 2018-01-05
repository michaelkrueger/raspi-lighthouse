# Adafruit NeoPixel library port to the rpi_ws281x library.
# Author: Tony DiCola (tony@tonydicola.com), Jeremy Garff (jer@jers.net)
import atexit

import _rpi_ws281x as ws

# LED strip configuration:
LED_COUNT      = 45      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP      = ws.WS2811_STRIP_GRB   # Strip type and colour ordering

def Color(red, green, blue, white = 0):
    """Convert the provided red, green, blue color to a 24-bit color value.
    Each color component should be a value 0-255 where 0 is the lowest intensity
    and 255 is the highest intensity.
    """
    return (white << 24) | (red << 16)| (green << 8) | blue


class _LED_Data(object):
    """Wrapper class which makes a SWIG LED color data array look and feel like
    a Python list of integers.
    """
    def __init__(self, channel, size):
        self.size = size
        self.channel = channel

    def __getitem__(self, pos):
        """Return the 24-bit RGB color value at the provided position or slice
        of positions.
        """
        # Handle if a slice of positions are passed in by grabbing all the values
        # and returning them in a list.
        if isinstance(pos, slice):
            return [ws.ws2811_led_get(self.channel, n) for n in xrange(*pos.indices(self.size))]
        # Else assume the passed in value is a number to the position.
        else:
            return ws.ws2811_led_get(self.channel, pos)

    def __setitem__(self, pos, value):
        """Set the 24-bit RGB color value at the provided position or slice of
        positions.
        """
        # Handle if a slice of positions are passed in by setting the appropriate
        # LED data values to the provided values.
        if isinstance(pos, slice):
            index = 0
            for n in xrange(*pos.indices(self.size)):
                ws.ws2811_led_set(self.channel, n, value[index])
                index += 1
        # Else assume the passed in value is a number to the position.
        else:
            return ws.ws2811_led_set(self.channel, pos, value)

class Lighthouse(object):
    def __init__(self):

    def zeile_1(self, color):
        print "Zeile1"
        
    def zeile_2(self, color):
        print "Zeile2"
        
    def zeile_3(self, color):
        print "Zeile3"
        
    def test(self):
        print "Test"
            
class neo_Lighthouse(object):

    def __init__(self):
        self.strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
        self.strip.begin()
    
    def stop(self):
        self.strip._cleanup()
    
    def zeile_1(self, color):
        self.strip.colorWipe(color, range(0,15), 0)
        
    def zeile_2(self, color):
        self.strip.colorWipe(color, range(16,30),0)
        
    def zeile_3(self, color):
        self.strip.colorWipe(color, range(31,45),0)
        
    # Define functions which animate LEDs in various ways.
    def colorWipe(self, color, leds = range(LED_COUNT), wait_ms=50):
        """Wipe color across display a pixel at a time."""
        for i in leds:
            self.strip.setPixelColor(i, color)
            self.strip.show()
            time.sleep(wait_ms/1000.0)

    def theaterChase(self, color, wait_ms=50, iterations=10):
        """Movie theater light style chaser animation."""
        for j in range(iterations):
            for q in range(3):
                for i in range(0, self.strip.numPixels(), 3):
                    self.strip.setPixelColor(i+q, color)
                self.strip.show()
                time.sleep(wait_ms/1000.0)
                for i in range(0, self.strip.numPixels(), 3):
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

    def rainbow(self, wait_ms=20, iterations=1):
        """Draw rainbow that fades across all pixels at once."""
        for j in range(256*iterations):
            for i in range(self.strip.numPixels()):
                self.strip.setPixelColor(i, wheel((i+j) & 255))
            self.strip.show()
            time.sleep(wait_ms/1000.0)

    def rainbowCycle(self, wait_ms=20, iterations=5):
        """Draw rainbow that uniformly distributes itself across all pixels."""
        for j in range(256*iterations):
            for i in range(self.strip.numPixels()):
                self.strip.setPixelColor(i, wheel((int(i * 256 / self.strip.numPixels()) + j) & 255))
            self.strip.show()
            time.sleep(wait_ms/1000.0)

    def theaterChaseRainbow(self, wait_ms=50):
        """Rainbow movie theater light style chaser animation."""
        for j in range(256):
            for q in range(3):
                for i in range(0, self.strip.numPixels(), 3):
                    self.strip.setPixelColor(i+q, wheel((i+j) % 255))
                self.strip.show()
                time.sleep(wait_ms/1000.0)
                for i in range(0, self.strip.numPixels(), 3):
                    self.strip.setPixelColor(i+q, 0)

    def test(self):
        print ('Color wipe animations.')
        colorWipe(self.strip, Color(255, 0, 0))  # Red wipe
        colorWipe(self.strip, Color(0, 255, 0))  # Blue wipe
        colorWipe(self.strip, Color(0, 0, 255))  # Green wipe
        print ('Theater chase animations.')
        theaterChase(self.strip, Color(127, 127, 127))  # White theater chase
        theaterChase(self.strip, Color(127,   0,   0))  # Red theater chase
        theaterChase(self.strip, Color(  0,   0, 127))  # Blue theater chase
        print ('Rainbow animations.')
        rainbow(self.strip)
        rainbowCycle(self.strip)
        theaterChaseRainbow(self.strip)
        
    
class Adafruit_NeoPixel(object):
    def __init__(self, num, pin, freq_hz=800000, dma=5, invert=False,
            brightness=255, channel=0, strip_type=ws.WS2811_STRIP_RGB):
        """Class to represent a NeoPixel/WS281x LED display.  Num should be the
        number of pixels in the display, and pin should be the GPIO pin connected
        to the display signal line (must be a PWM pin like 18!).  Optional
        parameters are freq, the frequency of the display signal in hertz (default
        800khz), dma, the DMA channel to use (default 5), invert, a boolean
        specifying if the signal line should be inverted (default False), and
        channel, the PWM channel to use (defaults to 0).
        """
        # Create ws2811_t structure and fill in parameters.
        self._leds = ws.new_ws2811_t()

        # Initialize the channels to zero
        for channum in range(2):
            chan = ws.ws2811_channel_get(self._leds, channum)
            ws.ws2811_channel_t_count_set(chan, 0)
            ws.ws2811_channel_t_gpionum_set(chan, 0)
            ws.ws2811_channel_t_invert_set(chan, 0)
            ws.ws2811_channel_t_brightness_set(chan, 0)

        # Initialize the channel in use
        self._channel = ws.ws2811_channel_get(self._leds, channel)
        ws.ws2811_channel_t_count_set(self._channel, num)
        ws.ws2811_channel_t_gpionum_set(self._channel, pin)
        ws.ws2811_channel_t_invert_set(self._channel, 0 if not invert else 1)
        ws.ws2811_channel_t_brightness_set(self._channel, brightness)
        ws.ws2811_channel_t_strip_type_set(self._channel, strip_type)

        # Initialize the controller
        ws.ws2811_t_freq_set(self._leds, freq_hz)
        ws.ws2811_t_dmanum_set(self._leds, dma)

        # Grab the led data array.
        self._led_data = _LED_Data(self._channel, num)

        # Substitute for __del__, traps an exit condition and cleans up properly
        atexit.register(self._cleanup)

    def _cleanup(self):
        # Clean up memory used by the library when not needed anymore.
        if self._leds is not None:
            ws.delete_ws2811_t(self._leds)
            self._leds = None
            self._channel = None

    def begin(self):
        """Initialize library, must be called once before other functions are
        called.
        """
        resp = ws.ws2811_init(self._leds)
        if resp != ws.WS2811_SUCCESS:
            message = ws.ws2811_get_return_t_str(resp)
            raise RuntimeError('ws2811_init failed with code {0} ({1})'.format(resp, message))

    def show(self):
        """Update the display with the data from the LED buffer."""
        resp = ws.ws2811_render(self._leds)
        if resp != ws.WS2811_SUCCESS:
            message = ws.ws2811_get_return_t_str(resp)
            raise RuntimeError('ws2811_render failed with code {0} ({1})'.format(resp, message))

    def setPixelColor(self, n, color):
        """Set LED at position n to the provided 24-bit color value (in RGB order).
        """
        self._led_data[n] = color

    def setPixelColorRGB(self, n, red, green, blue, white = 0):
        """Set LED at position n to the provided red, green, and blue color.
        Each color component should be a value from 0 to 255 (where 0 is the
        lowest intensity and 255 is the highest intensity).
        """
        self.setPixelColor(n, Color(red, green, blue, white))

    def setBrightness(self, brightness):
        """Scale each LED in the buffer by the provided brightness.  A brightness
        of 0 is the darkest and 255 is the brightest.
        """
        ws.ws2811_channel_t_brightness_set(self._channel, brightness)

    def getPixels(self):
        """Return an object which allows access to the LED display data as if
        it were a sequence of 24-bit RGB values.
        """
        return self._led_data

    def numPixels(self):
        """Return the number of pixels in the display."""
        return ws.ws2811_channel_t_count_get(self._channel)

    def getPixelColor(self, n):
        """Get the 24-bit RGB color value for the LED at position n."""
        return self._led_data[n]
