from __future__ import annotations

import osmnx as ox

ox.config(use_cache=True, log_console=True)


def create_network(location, filename="road_network.graphml"):
    # Function to create a network of roads (this function can be slow to run)

    # Use OSMnx to download the road network
    graph = ox.graph_from_place(
        location,
        network_type="drive",
        custom_filter='["highway"~"motorway"]',
    )

    ox.add_edge_speeds(graph)
    ox.add_edge_travel_times(graph)
    # Save the network
    ox.save_graphml(graph, filename)


# example usage:
create_network("Coimbra", "road_network.graphml")
#  create_network('Portugal', 'road_network.graphml')
# create_network('Europe', 'road_network.graphml') # this will take a long time to run
