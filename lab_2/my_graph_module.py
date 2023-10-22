import queue

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

paths = ["./data/tests/dolphins.gml",
         "./data/tests/football.gml",
         "./data/tests/karate.gml",
         "./data/tests/krebs.gml",
         "./data/tests/my_test1.gml",
         "./data/tests/my_adjnoun.gml",
         "./data/tests/my_as-22july06.gml",
         "./data/tests/my_ca-sandi_auths.gml",
         "./data/tests/my_lesmis.gml",
         #"./data/tests/my_simple.gml",
         "./data/tests/my_soc-firm-hi-tech.gml",
         "./data/tests/my_SW100.gml"
         ]

"""
everything was made with undirected weightless graphs in mind
it also works on multigraphs
"""


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


def write_partition_to_file(partition, output_filename="./data/output/output.txt"):
    """
    writes a partition to an output file
    :param partition: the repartition - an iterable of sets of nodes
    :param output_filename: a string representing the path of the file to which to write
    :return: None
    """
    file = open(output_filename, 'w')
    for community in partition:
        for elem in community:
            file.write(str(elem))
            file.write(" ")
        file.write("\n")
    file.close()


def show_graph(graph, communities=None):
    """
    shows a graph visualization
    :param graph: networkx graph
    :param communities: an iterable of sets of integers which represent communities
    :return: None
    """
    communities_to_send = [1] * len(graph)
    if communities is not None:
        index = 1
        for community in communities:
            for elem in community:
                communities_to_send[elem - min(graph.nodes)] = index
            index += 1
    np.random.seed(123)
    plt.figure(figsize=(16, 16))
    nx.draw(graph, node_color=communities_to_send, with_labels=True)
    plt.show()


def partition_nx(graph, k):
    """
    returns a network's partition in communities using networkx's girvan-newman implementation
    :param graph: networkx graph representation of the graph
    :param k: the number of communities
    :return: an iterable of sets representing the communities
    """
    number_of_components = compute_connected_components_number(graph)
    if k == number_of_components:
        return tuple(generate_connected_components(graph))
    partition_generator = nx.community.girvan_newman(graph)
    for partition in partition_generator:
        if len(partition) == k:
            write_partition_to_file(partition, "./data/output/output_nx.txt")
            return partition


def best_partition_nx(graph):
    """
    returns a network's best partition in communities using networkx's girvan-newman implementation
    :param graph: networkx graph representation of the graph
    :return: an iterable of sets representing the communities
    """
    partition_generator = nx.community.girvan_newman(graph)
    best_partition = tuple(generate_connected_components(graph))
    max_q = nx.community.modularity(graph, best_partition)
    for partition in partition_generator:
        new_q = nx.community.modularity(graph, partition)
        if new_q > max_q:
            max_q = new_q
            best_partition = partition
    write_partition_to_file(best_partition, "./data/output/output_nx.txt")
    return best_partition


def generate_connected_components(graph):
    """
    returns a generator of the connected components of the graph
    :param graph: networkx graph
    :return: a generator over the connected components
    """
    visited = set()
    for vertex in graph.nodes:
        if vertex not in visited:
            current_component = set()
            my_queue = queue.Queue()
            my_queue.put(vertex)
            current_component.add(vertex)
            visited.add(vertex)
            while my_queue.qsize() > 0:
                current_vertex = my_queue.get()
                for adjacent_node in graph.neighbors(current_vertex):
                    if adjacent_node not in current_component:
                        my_queue.put(adjacent_node)
                        current_component.add(adjacent_node)
                        visited.add(adjacent_node)
            yield current_component


def compute_connected_components_number(graph):
    """
    returns the number of connected components of the graph
    :param graph: networkx graph
    :return: the number of components as int
    """
    return sum(1 for _ in generate_connected_components(graph))


def map_edges(graph):
    """
    maps the edges of a graph with the coresponding number of smallest paths that go through them

    :param graph: networkx graph on which we work
    :return: a dictionary that represents a mapping of edges to their values
    """

    """
    edges_mapping = {}
    for u, v in graph.edges:
        if v < u:
            u, v = v, u
        edges_mapping[(u, v)] = 0.0
    node=0
    visited = {node: 0}
    visited_paths = {node: [[node]]}
    my_queue = queue.Queue()
    my_queue.put(node)
    while my_queue.qsize() > 0:
        current = my_queue.get()
        for path in visited_paths[current]:
            a = path[0]
            for i in range(1, len(path)):
                b = path[i]
                u, v = a, b
                if v < u:
                    u, v = v, u
                edges_mapping[(u, v)] += 1 / len(visited_paths[current])
                a = b
        for adjacent in graph.neighbors(current):
            if adjacent not in visited:
                visited[adjacent] = visited[current] + 1
                visited_paths[adjacent] = []
                my_queue.put(adjacent)
            if visited[adjacent] == visited[current] + 1:
                for path in visited_paths[current]:
                    to_add = path.copy()
                    to_add.append(adjacent)
                    visited_paths[adjacent].append(to_add)
    for edge in edges_mapping:
        edges_mapping[edge] /= 2
    """
    edges_mapping = nx.edge_betweenness_centrality(graph)
    return edges_mapping


def best_edge(graph):
    """
    returns the best edge to remove for girvan_newman algorithm
    :param graph: the graph for which we find the edge - NetworkX graph
    :return: said edge
    """
    the_best_edge = None
    the_best_value = -1.0
    edge_value_mapping = map_edges(graph)
    for edge in edge_value_mapping:
        if edge_value_mapping[edge] > the_best_value:
            the_best_value = edge_value_mapping[edge]
            the_best_edge = edge
    return the_best_edge


def my_girvan_newman(graph_original):
    """
    returns a generator function that iterates over the status of communities at each step of the girvan newman
    algorithm
    :param graph_original: networkx graph representation of the graph
    :return: generator of each step of the girvan-newman algorithm, from 2 to n communities
    """
    graph = graph_original.copy()  # creez copie ca sa nu stric graful dinafara
    current_number_of_connected_components = compute_connected_components_number(graph)
    # last - last number of connected components before last return
    last_number_of_connected_components = current_number_of_connected_components
    while len(graph.edges) > 0:
        while current_number_of_connected_components == last_number_of_connected_components:
            u, v = best_edge(graph)
            graph.remove_edge(u, v)
            current_number_of_connected_components = compute_connected_components_number(graph)
        last_number_of_connected_components = current_number_of_connected_components
        yield tuple(generate_connected_components(graph))


def partition_me(graph, k):
    """
    returns a network's partition in communities using my girvan-newman implementation
    :param graph: networkx graph representation of the graph
    :param k: the number of communities
    :return: an iterable of sets representing the communities
    """
    partition_generator = my_girvan_newman(graph)
    for partition in partition_generator:
        if len(partition) == k:
            write_partition_to_file(partition)
            return partition


def best_partition_me(graph):
    """
    returns a network's best partition in communities using my girvan-newman implementation
    :param graph: networkx graph representation of the graph
    :return: an iterable of sets representing the communities
    """
    partition_generator = my_girvan_newman(graph)
    best_partition = tuple(generate_connected_components(graph))
    max_q = nx.community.modularity(graph, best_partition)
    for partition in partition_generator:
        new_q = nx.community.modularity(graph, partition)
        if new_q > max_q:
            max_q = new_q
            best_partition = partition
    write_partition_to_file(best_partition)
    return best_partition
