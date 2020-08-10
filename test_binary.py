#!/usr/bin/env python3

import pytest
from binarysense import *

def test_make_column():
    assert make_column(0, red) == [black, black, black, black, black, black, black, black]
    assert make_column(1, red) == [black, black, black, black, black, black, black, red]
    assert make_column(1, blue) == [black, black, black, black, black, black, black, blue]
    assert make_column(100, red) == [black, red, red, black, black, red, black, black]
    assert make_column(100, blue) == [black, blue, blue, black, black, blue, black, black]

def test_temperature_color():
    assert temperature_to_color(19) == blue
    assert temperature_to_color(21) == green
    assert temperature_to_color(26) == red
    assert temperature_to_color(40) == red

def test_humidity_color():
    assert humidity_to_color(49) == red
    assert humidity_to_color(50) == green
    assert humidity_to_color(60) == blue

def test_pressure_color():
    assert pressure_to_color(1000) == green
    assert pressure_to_color(980) == red
    assert pressure_to_color (1050) == blue

def test_make_columns():
    assert make_temperature(25) == [black, black, black, red, red, black, black, red]
    assert make_humidity(55) == [black, black, green, green, black, green, green, green]
    assert make_pressure(1013) == [black, black, black, black, green, green, black, green]
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
