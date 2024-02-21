import logging

import pwnagotchi.ui.fonts as fonts
from pwnagotchi.ui.hw.base import DisplayImpl


class DummyDisplay(DisplayImpl):
    def __init__(self, config):
        super(DummyDisplay, self).__init__(config, 'dummydisplay')

    def layout(self):
        fonts.setup(8, 6, 8, 18, 18, 8)
        self._layout['width'] = 128
        self._layout['height'] = 64
        self._layout['face'] = (0, 20)
        self._layout['name'] = (5, 10)
        self._layout['channel'] = (0, 0)
        self._layout['aps'] = (20, 0)
        self._layout['uptime'] = (73, 0)
        self._layout['line1'] = [0, 9, 128, 9]
        self._layout['line2'] = [0, 55, 128, 55]
        self._layout['friend_face'] = (0, 76)
        self._layout['friend_name'] = (40, 78)
        self._layout['shakes'] = (0, 55)
        self._layout['mode'] = (103, 55)
        self._layout['status'] = {
            'pos': (64, 13),
            'font': fonts.status_font(fonts.Small),
            'max': 12
        }
        return self._layout

    def initialize(self):
        return

    def render(self, canvas):
        return

    def clear(self):
        return
