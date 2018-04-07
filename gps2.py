# coding: utf-8

import csv
import math
import matplotlib.pyplot as plt

# park pos
park_lat = 42 + 39.48779/60
park_lon = 83 + 14.61487/60
# park_lat = 42.658166
# park_lon = 83.243656

# USB GPS
USB_lat = []
USB_lon = []

# NEO GPS
NEO_lat = []
NEO_lon = []

# G65 GPS
G65_lat = []
G65_lon = []

plt.close()

with open("22.csv", 'r') as csvfile:
    read = csv.reader(csvfile)
    for i, rows in enumerate(read):
        if i >= 1:
            # USB
            lat0 = 42 + float(rows[4])/60
            C1 = math.sin(lat0) * math.sin(park_lat) + \
                math.cos(lat0) * math.cos(park_lat) * math.cos((-park_lon) - (-park_lon))
            Distance1 = 6371004 * math.acos(C1) * math.pi / 180
            Distance1 = round(Distance1, 3)
            USB_lat.append(Distance1)

            lon0 = 83 + float(rows[5])/60
            C2 = math.sin(park_lat) * math.sin(park_lat) + \
                math.cos(park_lat) * math.cos(park_lat) * math.cos((-park_lon) - (-lon0))
            Distance2 = 6371004 * math.acos(C2) * math.pi / 180
            Distance2 = round(Distance2, 3)
            USB_lon.append(Distance2)

            # NEO
            lat1 = 42 + float(rows[2])/60
            C3 = math.sin(lat1) * math.sin(park_lat) + \
                math.cos(lat1) * math.cos(park_lat) * math.cos((-park_lon) - (-park_lon))
            Distance3 = 6371004 * math.acos(C3) * math.pi / 180
            Distance3 = round(Distance3, 3)
            NEO_lat.append(Distance3)

            lon1 = 83 + float(rows[3])/60
            C4 = math.sin(park_lat) * math.sin(park_lat) + \
                math.cos(park_lat) * math.cos(park_lat) * math.cos((-park_lon) - (-lon1))
            Distance4 = 6371004 * math.acos(C4) * math.pi / 180
            Distance4 = round(Distance4, 3)
            NEO_lon.append(Distance4)

            # G65
            lat2 = 42 + float(rows[0])/60
            C5 = math.sin(lat2) * math.sin(park_lat) + \
                math.cos(lat2) * math.cos(park_lat) * math.cos((-park_lon) - (-park_lon))
            Distance5 = 6371004 * math.acos(C5) * math.pi / 180
            Distance5 = round(Distance5, 3)
            G65_lat.append(Distance5)

            lon2 = 83 + float(rows[1])/60
            C6 = math.sin(park_lat) * math.sin(park_lat) + \
                math.cos(park_lat) * math.cos(park_lat) * math.cos((-park_lon) - (-lon2))
            Distance6 = 6371004 * math.acos(C6) * math.pi / 180
            Distance6 = round(Distance6, 3)
            print(i, Distance6)
            G65_lon.append(Distance6)

plt.plot(USB_lon, USB_lat, 'r-o', label='g65')
plt.plot(NEO_lon, NEO_lat, 'g-^', label='USB')
plt.plot(G65_lon, G65_lat, 'b-o', label='neo')

plt.legend()
plt.xlabel('X-Lon: m')
plt.ylabel('Y-Lat: m')
plt.title('Based on same reference lat = 42.658166 lon = 83.243656')
plt.show()


