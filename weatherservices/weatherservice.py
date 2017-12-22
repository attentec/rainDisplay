# -*- coding: utf-8 -*-


class WeatherService():

    def __init__(self, coordinates, city="", country=""):
        self.lat = coordinates[0]
        self.lon = coordinates[1]
        self.city = city
        self.country = country

    def get_coordinates(self):
        return (self.lat, self.lon)

    def get_rain_estimates(self):
        return [0] * 12
