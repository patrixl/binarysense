#!/usr/bin/env python3

from sense_hat import SenseHat
import time, datetime
from binarysense import *
import sys

sense = SenseHat()

temp_calibration = 10 # 10 for rpi2, 15 for rpi4?

def main(argv):
    sense.set_rotation(int(argv[0]))
    sense.clear()

    while True:
        temperature = round(sense.get_temperature()) - temp_calibration
        humidity = round(sense.get_humidity())
        pressure = round(sense.get_pressure())
        now = datetime.datetime.now()
        hour = now.hour
        minute = now.minute
        second = now.second

        sense.set_pixels(
            make_grid([
                make_temperature(temperature), make_humidity(humidity), make_pressure(pressure),
                make_blank(), make_blank(),
                make_second(second), make_minute(minute), make_hour(hour)
            ])
        )

        time.sleep(0.25)

if __name__ == "__main__":
    main(sys.argv[1:])
