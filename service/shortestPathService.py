import osmnx as ox
import taxicab as tc

first_lon_coordinate: float
first_lat_coordinate: float
second_lon_coordinate: float
second_lat_coordinate: float


def getShortestPath(local):
    G = ox.graph_from_point((local.first_lat_coordinate, local.first_lon_coordinate), dist=3000, network_type='drive', simplify=True)

    G = ox.speed.add_edge_speeds(G)
    G = ox.speed.add_edge_travel_times(G)

    orig = (local.first_lat_coordinate, local.first_lon_coordinate)
    dest = (local.second_lat_coordinate, local.second_lon_coordinate)

    route = tc.distance.shortest_path(G, orig, dest)
    return route[0]