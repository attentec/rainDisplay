import display
import weatherservices.weatherservice
import geodata

coord = geodata.get_coordinates()
weather = weatherservices.weatherservice.WeatherService(coord)
print("lat: {}, lon: {}".format(weather.lat, weather.lon))
disp = display.Display()
disp.show_ip
disp.show_text("Rain Display")

rain_est = weather.get_rain_estimates()[0:disp.columns]
disp.show_bars(rain_est)
