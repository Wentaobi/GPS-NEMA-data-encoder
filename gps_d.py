# coding: utf-8

import csv
import math

with open("USB_NEO_G65.csv", 'r') as csvfile:
    with open("USB_NEO_G65_D.csv", 'w', newline='') as File:
        writer = csv.writer(File)
        read = csv.reader(csvfile)
        for i, rows in enumerate(read):
            if i >= 1:
                # USB
                print(rows[0])
                lat0 = 42 + float(rows[0])/60
                lon0 = 83 + float(rows[1])/60
                # NEO
                lat1 = 42 + float(rows[2])/60
                lon1 = 83 + float(rows[3])/60
                # G65
                lat2 = 42 + float(rows[4])/60
                lon2 = 83 + float(rows[5])/60

                # print(rows[0])

                C1 = math.sin(lat1) * math.sin(lat0) + math.cos(lat1) * math.cos(lat0) * math.cos((-lon1) - (-lon0))
                Distance1 = 6371004 * math.acos(C1) * math.pi / 180
                Distance1 = [Distance1]

                C2 = math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos((-lon1) - (-lon2))
                Distance2 = 6371004 * math.acos(C2) * math.pi / 180
                Distance2 = [Distance2]

                C3 = math.sin(lat2) * math.sin(lat0) + math.cos(lat2) * math.cos(lat0) * math.cos((-lon2) - (-lon0))
                Distance3 = 6371004 * math.acos(C3) * math.pi / 180
                Distance3 = [Distance3]

                Distance = [Distance1, Distance2, Distance3]
                print(Distance)

                writer.writerow(Distance)
    File.close()



