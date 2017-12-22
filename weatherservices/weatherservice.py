# -*- coding: utf-8 -*-
import abc

class WeatherService():
    __metaclass__ = abc.ABCMeta

    def __init__(self, coordinates, hours=12, city="", country=""):
        self.lat = coordinates[0]
        self.lon = coordinates[1]
        self.hours = hours
        self.city = city
        self.country = country

    def get_coordinates(self):
        return (self.lat, self.lon)

    @abc.abstractmethod
    def get_rain_estimates(self):
        """Return a list with rain estimates for
           the next self.hours hours"""
