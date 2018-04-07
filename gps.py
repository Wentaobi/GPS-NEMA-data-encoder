# coding: utf-8

import csv
import math

with open("USB.csv", 'r') as csvfile:
    with open("USB.csv", 'w', newline='') as File:
        writer = csv.writer(File)
        read = csv.reader(csvfile)
        for i, rows in enumerate(read):
            if i == 0:
                lat1 = 42 + float(rows[0])/60
                lon1 = 83 + float(rows[1])/60
                print(lat1, lon1)
                writer.writerow(Distance)
            if i >= 1:
                lat = 42 + float(rows[0])/60
                lon = 83 + float(rows[1])/60
                # print(lat, lon)

                C = math.sin(lat1) * math.sin(lat) + math.cos(lat1) * math.cos(lat) * math.cos((-lon1) - (-lon))
                Distance = 6371004 * math.acos(C) * math.pi / 180
                Distance = [Distance]
                # print(Distance)

                writer.writerow(Distance)

    File.close()



