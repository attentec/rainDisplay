import requests

cities = {
    'stockholm': (59.3333, 18.05),
    'linkoping': (58.41086, 15.62157),
    'lund': (55.7058, 13.1932),
    'uppsala': (59.8586, 17.6389),
    'norrkoping': (58.5877, 16.1924)
}


class Location():
    def __init__(self, city=None):
        if city is None:
            self.get_data()
        else:
            self.city = city
            self.coordinates = cities[city]
            self.ip = "IP unknown"

    def get_data(self):
        ext_url = "http://ip-api.com/json"
        data = requests.get(ext_url).json()
        self.city = data['city']
        self.ip = data['query']
        self.lat = data['lat']
        self.lon = data['lon']
        self.coordinates = (self.lat, self.lon)

    def print(self):
        print(self.city)
        print(self.ip)
        print(self.coordinates)


if __name__ == '__main__':
    loc = Location()
    loc.print()
