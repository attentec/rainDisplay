import requests

cities = {
    'stockholm': (59.3333, 18.05),
    'linkoping': (58.41086, 15.62157),
    'lund': (55.7058, 13.1932),
}

# TODO: get token from settings file
token = "3f9ee20ef054ba"


class Location():
    def __init__(self, city=None):
        if city is None:
            self.get_data()
        else:
            self.city = city
            self.coordinates = cities[city]
            self.ip = "IP unknown"

    def get_data(self):
        ext_url = "http://ipinfo.io/?token={}".format(token)
        data = requests.get(ext_url).json()
        self.city = data['city']
        self.ip = data['ip']
        self.coordinates = data['loc'].split(',')
        self.lat = self.coordinates[0]
        self.lon = self.coordinates[1]

    def print(self):
        print(self.city)
        print(self.ip)
        print(self.coordinates)


if __name__ == '__main__':
    loc = Location()
    loc.print()
