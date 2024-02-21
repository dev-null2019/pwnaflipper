import logging

import pwnagotchi.plugins as plugins
from pwnagotchi.ui.components import LabeledValue
from pwnagotchi.ui.view import BLACK
import pwnagotchi.ui.fonts as fonts

import serial
from PIL import Image

class pwnaflipper(plugins.Plugin):
    __author__ = 'Stefan Lehner'
    __version__ = '0.0.1'
    __license__ = 'MIT'
    __description__ = 'A plugin for communicating with the Flipper Zero'

    def __init__(self, port: str = "/dev/serial0", baud: int = 230400):
        # Create a Serial object to communicate with a serial port.

        self._port = port
        self._baud = baud

        try:
            self._serialConn = serial.Serial(port, baud)
        except:
            raise "Cannot bind to port ({}) with baud ({})".format(port, baud)

    # called when the plugin is loaded
    def on_loaded(self):
        logging.info("Pwnaflipper plugin loaded" % self.options)

    # called before the plugin is unloaded
    def on_unload(self, ui):
        self._serialConn.close()
        

    def on_ui_update(self, ui):
        logging.info("Updating screen")
        # Open the image file and convert it to black and white.
        img = Image.open('/var/tmp/pwnagotchi/pwnagotchi.png').convert('1')

        flipper_y = 0
        packed_pixels = 0
        pixelcount = -15

        # Iterating over each pixel of the image.
        for y in range(64):
            for x in range(128):
                pixel = img.getpixel((x, y))
                if pixelcount < 8:
                    if pixel > 127:
                        packed_pixels |= (1 << (7 - pixelcount))
                    else:
                        packed_pixels |= (0 << (7 - pixelcount))
                else:
                    self._serialConn.write(bytes([packed_pixels]))
                    packed_pixels = 0
                    pixelcount = 0
                    if pixel > 127:
                        packed_pixels |= (1 << (7 - pixelcount))
                    else:
                        packed_pixels |= (0 << (7 - pixelcount))
                pixelcount += 1
            # Print "Y:" for every new row.
            self._serialConn.write(b"Y:")
            # Send the row identifier as a byte.
            self._serialConn.write(bytes([flipper_y]))
            flipper_y += 1
            self._serialConn.flush()
