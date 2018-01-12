import requests
import sys

from weatherservices import weatherservice

# http://opendata.smhi.se/apidocs/metfcst/get-forecast.html


class Smhi(weatherservice.WeatherService):
    def get_rain_estimates(self):
        return self.get_data(data_point_name="pmax")

    def get_data(self, data_point_name):
        values = []
        smhi_url = "https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/{lon}/lat/{lat}/data.json".format(lon=self.lon, lat=self.lat)
        try:
            data = requests.get(smhi_url).json()
        except:
            print("Unexpected error:", sys.exc_info()[0])
            return None

        timeseries = data['timeSeries']
        for ts in timeseries[:self.hours]:
            for p in ts['parameters']:
                if p['name'] == data_point_name:
                    values.append(p['values'][0])
        return values


if __name__ == '__main__':
    cities = {
        'stockholm': (59.3333, 18.05),
        'linkoping': (58.41086, 15.62157),
        'lund': (55.7058, 13.1932),
    }
    smhi = Smhi(cities['lund'])
    print(smhi.get_rain_estimates())
