# -*- coding: utf-8 -*-


class WeatherService():

    def __init__(self, city="Linköping", country="Sweden"):
        self.city = city
        self.country = country

    def get_rain_estimates(self):
        return [0] * 12
