#!/usr/bin/env python3

blue = (0,0,75)
green = (0,75,0)
red = (75,0,0)
yellow = (75,75,0)
black = (0, 0, 0)

def convert_binary(value):
    bin = "{0:8b}".format(value)
    return bin

def binary_to_array(binary_string, color, precision = 8):
    arr = []
    for i in range(0,precision):
        if binary_string[i] == '1':
            arr.append(color)
        else:
            arr.append(black)
    return arr

def value_to_color(value, thresholds, colors):
    if value < thresholds[0]:
        return colors[0]
    elif value < thresholds[1]:
        return colors[1]
    else:
        return colors[2]

def make_column(value, color):
    return binary_to_array(convert_binary(value), color)

def temperature_to_color(value):
    return value_to_color(value, [20, 25], [blue, green, red])

def humidity_to_color(value):
    return value_to_color(value, [50, 60], [red, green, blue])

def pressure_to_color(value):
    return value_to_color(value, [1000, 1050], [red, green, blue])

def make_temperature(value):
    return make_column(value, temperature_to_color(value))

def make_humidity(value):
    return make_column(value, humidity_to_color(value))

def make_pressure(value):
    return make_column(value - 1000, pressure_to_color(value))

def make_hour(value):
    return make_column(value, yellow)

def make_minute(value):
    return make_column(value, red)

def make_second(value):
    return make_column(value, blue)

def make_blank():
    return make_column(0, black)

def make_grid(columns):
    return  [y for x in columns for y in x]
