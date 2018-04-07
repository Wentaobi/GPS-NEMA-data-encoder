# coding: utf-8

import csv
import math
import matplotlib.pyplot as plt

# park pos
# park_lat = 42 + 39.48779/60
# park_lon = 83 + 14.61487/60
park_lat = 42.658166
park_lon = 83.243656

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


# print(math.cos(park_lat))
plt.close()
with open("3gps.csv", 'r') as csvfile:
    read = csv.reader(csvfile)
    for i, rows in enumerate(read):
        if i >= 1:
            # USB
            lat0 = 42 + float(rows[4])/60
            # C1 = math.sin(lat0) * math.sin(park_lat) + \
            #     math.cos(lat0) * math.cos(park_lat) * math.cos((-park_lon) - (-park_lon))
            # Distance1 = 6371004 * math.acos(C1) * math.pi / 180

            Distance1 = 6371004 * (lat0 - park_lat) * math.pi / 180
            Distance1 = round(Distance1, 3)
            USB_lat.append(Distance1)

            lon0 = 83 + float(rows[5])/60
            # C2 = math.sin(90-park_lat) * math.sin(90-park_lat) + \
            #     math.cos(90-park_lat) * math.cos(90-park_lat) * math.cos((-park_lon) - (-lon0))
            # Distance2 = 6371004 * math.acos(C2) * math.pi / 180

            Distance2 = -6371004 * math.cos(park_lat * math.pi / 180) * (lon0 - park_lon) * math.pi / 180
            Distance2 = round(Distance2, 3)
            USB_lon.append(Distance2)

            # NEO
            lat1 = 42 + float(rows[2])/60
            Distance3 = 6371004 * (lat1 - park_lat) * math.pi / 180
            Distance3 = round(Distance3, 3)
            NEO_lat.append(Distance3)

            lon1 = 83 + float(rows[3])/60
            # C4 = math.sin(90-park_lat) * math.sin(90-park_lat) + \
            #     math.cos(90-park_lat) * math.cos(90-park_lat) * math.cos((-park_lon) - (-lon1))
            # Distance4 = 6371004 * math.acos(C4) * math.pi / 180
            Distance4 = -6371004 * math.cos(park_lat* math.pi / 180) * (lon1 - park_lon) * math.pi / 180
            Distance4 = round(Distance4, 3)
            NEO_lon.append(Distance4)

            # G65
            lat2 = 42 + float(rows[0])/60
            # C5 = math.sin(lat2) * math.sin(park_lat) + \
            #     math.cos(lat2) * math.cos(park_lat) * math.cos((-park_lon) - (-park_lon))
            # Distance5 = 6371004 * math.acos(C5) * math.pi / 180
            Distance5 = 6371004 * (lat2 - park_lat) * math.pi / 180
            Distance5 = round(Distance5, 3)
            G65_lat.append(Distance5)

            lon2 = 83 + float(rows[1])/60
            # C6 = math.sin(90-park_lat) * math.sin(90-park_lat) + \
            #     math.cos(90-park_lat) * math.cos(90-park_lat) * math.cos((-park_lon) - (-lon2))
            # Distance6 = 6371004 * math.acos(C6) * math.pi / 180
            Distance6 = -6371004 * math.cos(park_lat* math.pi / 180) * (lon2 - park_lon) * math.pi / 180
            Distance6 = round(Distance6, 3)
            print(i, G65_lat)
            G65_lon.append(Distance6)

# plt.axis([0, 90, 0, 90])
# plt.axis('scaled')

USB_lon_max = round(max(USB_lon))
USB_lat_max = round(max(USB_lat))

USB_lon_min = round(min(USB_lon))
USB_lat_min = round(min(USB_lat))

USB_lon_len = USB_lon_max - USB_lon_min
USB_lat_len = USB_lat_max - USB_lat_min

NEO_lon_max = round(max(NEO_lon))
NEO_lat_max = round(max(NEO_lat))

NEO_lon_min = round(min(NEO_lon))
NEO_lat_min = round(min(NEO_lat))

NEO_lon_len = NEO_lon_max - NEO_lon_min
NEO_lat_len = NEO_lat_max - NEO_lat_min

G65_lon_max = round(max(G65_lon))
G65_lat_max = round(max(G65_lat))

G65_lon_min = round(min(G65_lon))
G65_lat_min = round(min(G65_lat))

G65_lon_len = G65_lon_max - G65_lon_min
G65_lat_len = G65_lat_max - G65_lat_min


plt.plot(USB_lon, USB_lat, 'r-o', label='G65 H/V:%s/%s' % (USB_lat_len, USB_lon_len))
plt.plot(NEO_lon, NEO_lat, 'g-^', label='USB H/V:%s/%s' % (NEO_lat_len, USB_lon_len))
plt.plot(G65_lon, G65_lat, 'b-o', label='NEO H/V:%s/%s' % (G65_lat_len, G65_lon_len))
# plt.axis([-10, 10, -10, 10])

# plt.xlim(0, 8)
# plt.ylim(0, 8)
plt.axis('Scaled')

plt.legend()
plt.xlabel('X-Lon: m')
plt.ylabel('Y-Lat: m')
plt.title('Based on same reference lat = 42.658166 lon = 83.243656')
plt.show()


