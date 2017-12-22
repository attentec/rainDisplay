from display import display
import weatherservices.smhi
import geodata



coord = geodata.get_coordinates()
weather = weatherservices.smhi.Smhi(coord)
print("lat: {}, lon: {}".format(weather.lat, weather.lon))
disp = display.Display()
disp.show_ip
disp.show_text("Rain Display")

rain_est = weather.get_rain_estimates()
disp.show_bars(rain_est[0:disp.columns], color='blue')
