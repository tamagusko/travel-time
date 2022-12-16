# create_network.py

This program uses the osmnx library to download a network of roads from OpenStreetMap (OSM) for a given location and save it to a file in GraphML format.

## Usage

1. Edit location in line 25 (there are some examples on lines 26 and 27)
2. Run command:
`python create_network.py`

# create_dummy_coordinates.py

This program generates a list of n random geographical coordinates within a specified latitude and longitude range and saves them to a CSV file. This code was created just to test the other programs.

## Usage

1. Edit lines 13 (max_lat), 14 (max_lon), 15 (min_lat), 16 (min_lon) and 19 (n).
2. Run command:  
`python create_dummy_coordinates.py`


# travel_times.py (need to be fixed)

This program is a tool for calculating the travel time between pairs of points using a road network data. It takes in the coordinates for the pairs of points and a file containing the road network data, and outputs the travel times between the pairs of points in a matrix. The program uses functions from several libraries to help it read and analyze the data, and perform the calculations. It then stores the results in a file for later use.

## Usage

1. Prepare two files: "coordinates.csv" (format: latitude, longitude) and "road_network.graphml (using create_network.py)"
2. Run command:  
`python travel_times.py`
