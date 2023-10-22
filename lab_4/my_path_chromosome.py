import random
from my_chromosome import Chromosome

"""
args is a dictionary with:
'graph' - networkx graph
'total' - total cost of all edges
'start' - the start of the path
'finish' - the finish of the path
if start=finish, it will compute the shortest path that goes through each node in graph
"""


def correct_path(path, args):
    """
    corrects a path
    :param path: a normal chromosome path
    :param args: the extra arguments
    :return: the correct path
    """
    start = args['start']
    finish = args['finish']
    graph = args['graph']
    dif = min(graph.nodes)
    new_path = []
    inside = False
    for i in range(0, len(path)):
        u = path[i]
        """
        if not inside:
            if u==start or u==finish:
                inside=True
        else:
            if u==start or u==finish:
                inside=not inside
        """
        if start != finish and (u == start or u == finish):
            if inside:
                new_path.append(u + dif)
            inside = not inside
        if start == finish or inside:
            new_path.append(u + dif)
    if start == finish:
        new_path.append(path[0] + dif)
    return new_path


# check
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


def compute_total_weight(graph):
    """
    computes the total weight of the edges in a graph
    :param graph: said graph
    :return: said weight
    """
    total = 0.0
    for u, v in graph.edges:
        total += graph.get_edge_data(u, v)["value"]
    return total


def fitness(chromosome, args):
    """
    determines the fitness through fitness function on chromosome
    :param chromosome: said chromosome
    :param args: additional arguments
    :return: said fitness
    """
    graph = args['graph']
    if 'total' not in args:
        args['total'] = compute_total_weight(graph)
    total = args['total']
    start = args['start']
    finish = args['finish']
    permutation = chromosome.get_representation()
    val_f = 0
    inside = False
    for i in range(0, len(permutation) - 1):
        u, v = permutation[i], permutation[i + 1]
        """
        if not inside:
            if u==start or u==finish:
                inside=True
        else:
            if u==start or u==finish:
                inside=not inside
        """
        if u == start or u == finish:
            inside = not inside
        if start == finish or inside:
            val_f += get_edge_fitness(u, v, graph, total)
    if start == finish:
        u, v = permutation[-1], permutation[0]
        val_f += get_edge_fitness(u, v, graph, total)
    elif val_f >= total:
        val_f = total
    return (-1) * val_f


def get_edge_fitness(u, v, graph, substitute):
    """
    gets the fitness of an edge
    :param u: first member of edge
    :param v: second member of edge
    :param graph: the graph of the edge
    :param substitute: the weight to use if no edge exists between u and v
    :return: said value
    """
    to_return = substitute
    if graph.has_edge(u, v):
        to_return = graph.get_edge_data(u, v)["value"]
    return to_return


def generator(args):
    """
    generates a random chromosome
    :param args: args for said chromosome
    :return: said chromosome
    """
    graph = args['graph']
    no_nodes = len(graph.nodes)
    my_way = [i for i in range(0, no_nodes)]
    random.shuffle(my_way)
    chromosome = Chromosome(my_way)
    return chromosome


def cross_over(chr1, chr2, args):
    """
    generates a chromosome through crossover of two chromosomes
    :param chr1: one of the chromosomes
    :param chr2: the other chromosome
    :param args: the extra arguments
    :return: the new chromosome
    """
    repr1 = chr1.get_representation()
    repr2 = chr2.get_representation()
    my_repr = [0] * len(repr1)
    for i in range(0, len(repr1)):
        my_repr[i] = repr2[repr1[i]]
    return Chromosome(my_repr)


def mutation(chromosome, args):
    """
    generates a new chromosome through mutation
    :param chromosome: said chromosome
    :param args: said args
    :return: said generated chromosome
    """
    representation = chromosome.get_representation()
    i = random.randint(0, len(representation) - 1)
    j = random.randint(0, len(representation) - 1)
    my_repr = [elem for elem in representation]
    my_repr[i], my_repr[j] = my_repr[j], my_repr[i]
    return Chromosome(my_repr)
