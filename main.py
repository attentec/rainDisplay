import time
from display import display
import weatherservices.smhi
import geodata



coord = geodata.get_coordinates()
weather = weatherservices.smhi.Smhi(coord)
print("lat: {}, lon: {}".format(weather.lat, weather.lon))
disp = display.Display()
disp.show_ip
disp.show_text("Rain Display")

while True:
    rain_est = weather.get_rain_estimates()
    if rain_est is not None:
        disp.show_bars(rain_est, disp.color['blue'])
    else:
        disp.show_bars([1], color=disp.color['red'])
    time.sleep(60)
