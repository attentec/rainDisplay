import display
import weatherservices.weatherservice

weather = weatherservices.weatherservice.WeatherService()
disp = display.Display()
disp.show_ip
disp.show_text("Rain Display for {}".format(weather.city))

rain_est = weather.get_rain_estimates()[0:disp.columns]
disp.show_bars(rain_est)
