# coding: utf-8

import csv
import math
import matplotlib.pyplot as plt
# print(math.cos(park_lat))
plt.close()
j = 0


def gps2pos(str1, str2):
    Lat = float(str1) / 100
    Lon = float(str2) / 100
    return Lat, Lon


with open("ggg65.csv", 'r') as g65_file:
    g65_read = csv.reader(g65_file)
    for i, rows in enumerate(g65_read):
        if i >= 1:
            if rows[0] == '$GPRMC':
                m = [gps2pos(rows[3], rows[5])]
                print(m)
