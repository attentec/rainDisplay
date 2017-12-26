import unicornhat as unicorn
import math
from subprocess import check_output
from display import text

color = {
    'black': (0, 0, 0),
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'blue': (0, 0, 255),
    'white': (255, 255, 255)
}


class Display():

    def __init__(self, brightness=0.2, rotation=0):
        self.brightness=brightness
        self.rotation=rotation
        self.rows = 4
        self.columns = 8
        unicorn.set_layout(unicorn.PHAT)
        unicorn.clear()
        unicorn.rotation(self.rotation)
        unicorn.brightness(self.brightness)
        unicorn.show()
        self.show_ip()

    def show_ip(self):
        ip = check_output(['hostname', '-I']).strip()
        self.show_text(ip)

    def test(self):
        self.show_text("testing")

    def show_text(self, text):
        print("Text to display: {}".format(text))
        text.show(text, loops=2, time_delta=0.1, spaces=6)

    def show_bars(self, values, color=color['white']):
        unicorn.clear()
        for x in range(0, min(self.columns, len(values))):
            for y in range(int(math.ceil(values[x]))):
                self.set_pixel(x, y, color)
        unicorn.show()

    def set(self, row, col, color):
        unicorn.set_pixel(row, col, color[0], color[1], color[2])
