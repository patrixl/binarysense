#!/usr/bin/env python3
# (c) 2020 Patrice LaFlamme see more details at the end of the file

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


# Binary Sense - Binary clock and binary sensor readings with a Sense HAT
#     Copyright (C) 2020 Patrice LaFlamme

#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.

#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.

#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>.
