import networkx as nx
import matplotlib.pyplot as plt

paths = [
    "./data/tests/easy_01_tsp.gml",
    "./data/tests/easy_02_tsp.gml",
    "./data/tests/easy_03_tsp.gml",
    "./data/tests/medium_01_tsp.gml",
    "./data/tests/medium_02_tsp.gml",
    "./data/tests/medium_03_tsp.gml",
    "./data/tests/hard_01_tsp.gml",
    "./data/tests/hard_02_tsp.gml",
    "./data/tests/hard_03_tsp.gml",
    "./data/tests/extreme_01_tsp.gml",
    "./data/tests/extreme_02_tsp.gml",
    "./data/tests/extreme_03_tsp.gml",
    "./data/tests/extreme_04_tsp.gml",
    "./data/tests/t1.gml",
    "./data/tests/t2.gml",
    "./data/tests/t3.gml"
]


def load_by_path(path):
    """
    loads a graph from a given path
    :param path: string to the .gml file representing the graph
    :return: said loaded graph
    """
    graph = nx.read_gml(path, label='id')
    graph.remove_edges_from(nx.selfloop_edges(graph))
    return graph


def load_by_index(index):
    """
    loads a graph from the given paths by an index in the list
    :param index: integer representing which path to be taken
    :return: said loaded graph
    """
    return load_by_path(paths[index])


def show_graph(graph):
    """
    shows a graph visualization
    :param graph: networkx graph
    :return: None
    """
    communities_to_send = [1] * len(graph)
    plt.figure(figsize=(16, 16))
    nx.draw(graph, node_color=communities_to_send, with_labels=True)
    plt.show()

def list_to_set(path):
    """
    transform a path in list form in a path in set form
    :param path: said path in list form
    :return: path in set form
    """
    edges = set()
    for i in range(0, len(path) - 1):
        u, v = path[i], path[i + 1]
        edges.add((u, v))
    return edges

def show_graph_and_path(graph, path):
    """
    shows a graph visualization
    :param graph: networkx graph
    :param path: a list of values representing the nodes of the graph - it gives the path taken
    :return: None
    """
    plt.figure(figsize=(16, 16))
    path_as_set = list_to_set(path)
    edge_list = list(graph.edges())
    edge_colors = []
    edge_labels = nx.get_edge_attributes(graph, 'value')
    for i in range(0, len(edge_list)):
        u, v = edge_list[i]
        if (u, v) in path_as_set or (v, u) in path_as_set:
            edge_colors.append('r')
        else:
            edge_colors.append('b')
    # pos = nx.spring_layout(graph)
    pos = nx.random_layout(graph, seed=123)
    nx.draw(graph, pos, with_labels=True)
    nx.draw_networkx_edges(graph, pos, edgelist=edge_list, edge_color=edge_colors)
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_color='black')
    plt.show()
