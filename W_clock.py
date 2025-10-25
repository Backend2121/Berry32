import time
from display import getOled
from utils import centerString
from utils import settime
from utils import ActiveWidget

VERSION = 101
# Hello updater!

widget_number = 0

def run(id, active_widget):
    global widget_number
    oled = getOled()
    settime()
    while True:
        time.sleep(0.2)
        if (active_widget.value == widget_number):
            (year, month, mday, hour, minute, second, weekday, yearday) = time.gmtime()
            dateString = f'{mday}/{month}/{year}'
            timeString = '{:02d}:{:02d}:{:02d}'.format(hour, minute, second)
            oled.fill(0)
            oled.text("Data e ora", centerString("Data e ora"), 0)
            oled.text(dateString, centerString(dateString), 16)
            oled.text(timeString, centerString(timeString), 32)

            oled.show()
