cities = {
    'stockholm': (59.3333, 18.05)
}


def get_coordinates_from_ip(ip):
    return cities['stockholm']


def get_ip():
    return "127.0.0.1"


def get_coordinates():
    return get_coordinates_from_ip(get_ip())
