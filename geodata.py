cities = {
    'stockholm': (59.3333, 18.05),
    'linkoping': (58.41086, 15.62157),
    'lund': (55.7058, 13.1932),
}


def get_coordinates_from_ip(ip):
    return cities['stockholm']


def get_ip():
    return "127.0.0.1"


def get_coordinates():
    return get_coordinates_from_ip(get_ip())
