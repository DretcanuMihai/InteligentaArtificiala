import networkx as nx
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
         # "./data/tests/my_simple.gml",
         "./data/tests/my_soc-firm-hi-tech.gml",
         "./data/tests/my_SW100.gml"
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


def append_partition_to_file(partition, output_filename="./data/output/log.txt"):
    """
    writes a partition to an output file
    :param partition: the repartition - an iterable of sets of nodes
    :param output_filename: a string representing the path of the file to which to write
    :return: None
    """
    file = open(output_filename, 'a')
    for community in partition:
        for elem in community:
            file.write(str(elem))
            file.write(" ")
        file.write("\n")
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
    plt.figure(figsize=(16, 16))
    nx.draw(graph, node_color=communities_to_send, with_labels=True)
    plt.show()
