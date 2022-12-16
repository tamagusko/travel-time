from __future__ import annotations

import csv
import random

# Minimum and maximum latitude and longitude for Europe
# min_lat = 34.9
# max_lat = 61.4
# min_lon = -10.4
# max_lon = 40.0

# Minimum and maximum latitude and longitude for Coimbra (aproximately)
max_lat = 40.229801301088806
max_lon = -8.481282391099144
min_lat = 40.16765197473754
min_lon = -8.362321057895329

# Generate n random coordinates
n = 50
latitudes = []
longitudes = []
for i in range(n):
    lat = random.uniform(min_lat, max_lat)
    lon = random.uniform(min_lon, max_lon)
    latitudes.append(lat)
    longitudes.append(lon)

# Save the coordinates to a CSV file
with open("coordinates.csv", "w") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["latitude", "logitude"])
    for i in range(n):
        writer.writerow([latitudes[i], longitudes[i]])
