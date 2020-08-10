#!/usr/bin/env python3

import pytest
from src.sense import *

def test_make_column():
    assert make_column(0, red) == [black, black, black, black, black, black, black, black]
    assert make_column(1, red) == [black, black, black, black, black, black, black, red]
    assert make_column(1, blue) == [black, black, black, black, black, black, black, blue]
    assert make_column(100, red) == [black, red, red, black, black, red, black, black]
    assert make_column(100, blue) == [black, blue, blue, black, black, blue, black, black]

def test_make_temperatures():
    assert make_temperature(24) == [black, black, black, green, green, black, black, black]
    assert make_temperature(19) == [black, black, black, blue, black, black, blue, blue]
    assert make_temperature(35) == [black, black, red, black, black, black, red, red]

def test_make_humidities():
    assert make_humidity(45) == [black, black, red, black, red, red, black, red]
    assert make_humidity(55) == [black, black, green, green, black, green, green, green]
    assert make_humidity(75) == [black, blue, black, black, blue, black, blue, blue]

def test_make_pressures():
    assert make_pressure(999) == [black, black, black, black, black, black, black, red]
    assert make_pressure(1013) == [black, black, black, black, green, green, black, green]
    assert make_pressure(1053) == [black, black, blue, blue, black, blue, black, blue]

def test_make_time():
    assert make_hour(15) == [black, black, black, black, yellow, yellow, yellow, yellow]
    assert make_minute(55) == [black, black, red, red, black, red, red, red]
    assert make_second(18) == [black, black, black, blue, black, black, blue, black]

def test_grid():
    assert make_grid([[1,1,1],[0,0,0]]) == [1,1,1,0,0,0]
    assert make_grid([make_hour(15), make_minute(55), make_second(18), make_blank(),
                      make_blank(), make_pressure(1013), make_humidity(55),
                      make_temperature(25)]) == [
                          black, black, black, black, yellow, yellow, yellow, yellow,
                          black, black, red, red, black, red, red, red,
                          black, black, black, blue, black, black, blue, black,
                          black, black, black, black, black, black, black, black,
                          black, black, black, black, black, black, black, black,
                          black, black, black, black, green, green, black, green,
                          black, black, green, green, black, green, green, green,
                          black, black, black, red, red, black, black, red
                      ]
