import time
from display import display
from display.display import colors

disp = display.Display(brightness=0.2)
while True:
    disp.show_text("emilia")
    disp.heart()
    time.sleep(5)
