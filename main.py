import time
from display import display
from display.display import colors
import weatherservices.smhi
import geodata

def rain_est_to_bars(est):
    est = [x * 2 for x in est] # Show half mill as one bar
    bars = [0] * 8
    if len(est) <= 8:
	bars = est
    else:
	for i in range(4):
	    bars[i] = est[i]
	for i in range(4, 8):
	    est_i = ((i - 4) * 2 + 4)
	    bars[i] = est[est_i] + est[est_i + 1]
    return bars

loc = geodata.Location()
loc.print()
weather = weatherservices.smhi.Smhi(loc.coordinates)
disp = display.Display(brightness=0.2)
disp.show_text(loc.city)

while True:
    rain_est = weather.get_rain_estimates()
    if rain_est is not None:
	rain_bars = rain_est_to_bars(rain_est)
        disp.show_bars(rain_bars, colors['blue'])
	disp.set_pixel(0, 3, colors['white'], brightness_scale=0.86)
	disp.show()
	disp.status_light(colors['blue'])
    else:
	disp.clear()
	disp.show_pixel(0, 3, colors['red'])
    time.sleep(600)
    # TODO: at random points, display msg
