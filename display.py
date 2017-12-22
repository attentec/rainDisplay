

color = {
    'black': (0, 0, 0),
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'blue': (0, 0, 255),
    'white': (255, 255, 255)
}


class Display():

    def __init__(self):
        self.rows = 4
        self.columns = 8

    def show_ip(self):
        print("my ip is 127.0.0.1")

    def test(self):
        print("testing testing")

    def show_text(self, text):
        print("Text to display: {}".format(text))

    def show_bars(self, values, color=color['white']):
        assert len(values) is 8, "len(show_bars) != 8"
        print(values)

    def set(self, row, col, color):
        print("set: {r}, {c}, {color}".format(r=row, c=col, color=color))
