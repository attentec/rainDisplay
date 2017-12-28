import unicornhat as unicorn
import math
import numpy as np
import time
from subprocess import check_output

import render_text

colors = {
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
        unicorn.set_layout(unicorn.PHAT)
	self.columns, self.rows = unicorn.get_shape()
        unicorn.clear()
        unicorn.rotation(self.rotation)
        unicorn.brightness(self.brightness)
        unicorn.show()

    def show_ip(self):
        ip = check_output(['hostname', '-I']).strip()
        self.show_text(ip)

    def test(self):
        self.show_text("testing")

    def show_text(self, text):
	unicorn.rotation(180)
        print("Text to display: {}".format(text))
        render_text.show(text, loops=1, time_delta=0.1, spaces=8)
	unicorn.rotation(0)

    def show_bars(self, values, color=colors['white']):
	for i in range(0, max(0, self.columns - len(values))):
	    values.append(0)
        values.reverse()
        unicorn.clear()
        for x in range(0, self.columns):
            for y in range(int(math.ceil(values[x]))):
                self.set_pixel(x, y, color)
        unicorn.show()

    def show_pixel(self, col, row, color):
	unicorn.clear()
        self.set_pixel(col, row, color)
	unicorn.show()

    def show(self):
        unicorn.show()

    def clear(self):
	unicorn.clear()

    def heart(self):
	unicorn.rotation(180)
	render_text.show_heart()
	unicorn.rotation(0)

    def set_pixel(self, col, row, color, brightness_scale=1.0):
	if brightness_scale > 1.0:
	    brightness_scale = 1.0
	color = tuple(int(c * brightness_scale) for c in color)
	# the resulting color value has to be > 44 with the
	# display brightness accounted for to be shown
	# color = value * brightness_scale * self.brightness
        unicorn.set_pixel(col, row, color[0], color[1], color[2])

    def status_light(self, blink_color, col=0, row=3, blinks=3, duration=0.4, pause=0.6):
	org_color = unicorn.get_pixel(col, row)
	for b in range(blinks):
	    self.set_pixel(col, row, blink_color)
	    self.show()
	    time.sleep(duration)
	    self.set_pixel(col, row, org_color)
	    self.show()
	    time.sleep(pause)


    def pixel_blink(self, col, row, blink_color, time_delta, steps, loops):
	start_color = unicorn.get_pixel(col, row)
	color_list = []
	for i, c in enumerate(start_color):
            list = np.linspace(start_color[i], blink_color[i], steps).tolist()
            color_list.append([int(r) for r in list])

	for l in range(loops):
	    for step in range(steps):
                self.set_pixel(col, row,
                               (color_list[0][step],
                                color_list[1][step],
                                color_list[2][step]))
                unicorn.show()
                time.sleep(time_delta)
            for step in range(steps, 0, -1):
                self.set_pixel(col, row,
                               (color_list[0][step - 1],
                                color_list[1][step - 1],
                                color_list[2][step - 1]))
                unicorn.show()
                time.sleep(time_delta)


