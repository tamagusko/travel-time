from __future__ import annotations

import csv

import networkx as nx
import numpy as np
import osmnx as ox


def calc_travel_time(graph, point1, point2):
    # Get the nearest network node to each point
    origin_lat, origin_lon = point1
    dest_lat, dest_lon = point2
    orig_node = ox.nearest_nodes(
        graph,
        origin_lat,
        origin_lon,
        return_dist=False,
    )
    dest_node = ox.nearest_nodes(graph, dest_lat, dest_lon, return_dist=False)

    # Calculate shortest path time in minutes
    shortest_path_time = (
        nx.shortest_path_length(
            graph,
            orig_node,
            dest_node,
            weight="travel_time",
        )
        / 60
    )
    return shortest_path_time


# Read coordinates from CSV file
latitudes, longitudes = [], []
with open("coordinates.csv") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # skip header row
    for row in reader:
        latitudes.append(float(row[0]))
        longitudes.append(float(row[1]))

# Load road network
graph = ox.load_graphml("road_network.graphml")

# Calculate travel time between all pairs of points and store in matrix
n = len(latitudes)
results = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        point1 = (latitudes[i], longitudes[i])
        point2 = (latitudes[j], longitudes[j])
        results[i, j] = calc_travel_time(graph, point1, point2)

# Save results to text file
np.savetxt("results.txt", results)
