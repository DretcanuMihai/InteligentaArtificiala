import application
import networkx as nx
import random



def create_graph(n):
    graph = nx.Graph()
    for i in range(0, n):
        graph.add_node(i)
        for j in range(0, i):
            graph.add_edge(i, j)
            graph.get_edge_data(i, j)["value"] = random.randint(1, 100)
    nx.write_gml(graph, "./data/"+str(n)+".gml")


def dist(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2)


def parse_tsp(source, destination):
    source = "./data/to_transform/" + source
    destination = "./data/tests/" + destination
    file = open(source, 'r')
    graph = nx.Graph()
    my_dict = {}
    n = 0
    for line in file:
        if line == "EOF" or line == "EOF\n":
            break
        line = line.split()
        nod = int(line[0]) - 1
        x = float(line[1])
        y = float(line[2])
        my_dict[nod] = (x, y)
        n = nod + 1
    for i in range(0, n):
        graph.add_node(i)
        for j in range(0, i):
            graph.add_edge(i, j)
            graph.get_edge_data(i, j)["value"] = dist(my_dict[i][0], my_dict[i][1], my_dict[j][0], my_dict[j][1])
    file.close()
    nx.write_gml(graph, destination)


def parse_txt(source, destination):
    source = "./data/to_transform/" + source
    destination = "./data/tests/" + destination
    graph = nx.Graph()
    file = open(source, 'r')
    line = file.readline()
    line = line.split()
    noduri = int(line[0])
    for i in range(noduri):
        graph.add_node(i)
    i = 0
    for line in file:
        line = line.split(",")
        line[-1] = line[-1].split()[0]
        for j in range(i + 1, noduri):
            graph.add_edge(i, j)
            graph.get_edge_data(i, j)["value"] = int(line[j])
        i += 1

    file.close()
    nx.write_gml(graph, destination)


if __name__ == '__main__':
    # parse_tsp("eil51.txt", "t3.gml")
    create_graph(5)
    create_graph(6)
    create_graph(7)
    create_graph(8)
    create_graph(9)
    create_graph(10)
    create_graph(11)
    create_graph(12)
    # user_interface = application.Application()
    # user_interface.run()
