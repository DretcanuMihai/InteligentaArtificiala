import networkx
import random
from my_chromosome import Chromosome

"""
args is a dictionary with:
'graph' - networkx graph
'limit' - integer representing the number of wanted communities
"""


def list_to_tuple(community_partition, graph):
    """
    converts a community from list representation to tuple representation
    :param community_partition: said community as list
    :param graph: the graph of the community
    :return: community as tuple
    """
    my_dict = {}
    dif = min(graph.nodes)
    for i in range(0, len(community_partition)):
        if community_partition[i] not in my_dict:
            my_dict[community_partition[i]] = set()
        my_dict[community_partition[i]].add(i + dif)
    return tuple(my_dict.values())


def tuple_to_list(community_partition, graph):
    """
    converts a community from tuple representation to list representation
    :param community_partition: said community as tuple
    :param graph: the graph of the community
    :return: community as list
    """
    my_list = [0] * len(graph.nodes)
    dif = min(graph.nodes)
    index = 0
    for community in community_partition:
        index += 1
        for elem in community:
            my_list[elem - dif] = index
    return my_list


def nc_check(chromosome, limit):
    """
    determines the penalisation of a chromosome for breaking the community number contract
    :param chromosome: the chromosome
    :param limit: the number of communities
    :return: said penalisation
    """
    return -abs(len(set(chromosome.get_representation())) - limit)*(1/len(chromosome.get_representation()))
    #return 0


def community_score(chromosome, args):
    """
    determines the fitness through score function on chromosome
    :param chromosome: said chromosome
    :param args: additional arguments
    :return: said fitness
    """
    graph = args['graph']
    a1 = 1
    a2 = 1
    partition = chromosome.get_representation()
    partition = list_to_tuple(partition, graph)
    val_f = 0
    for C in partition:
        mod_C = len(C)
        val = 0
        for elem in C:
            suma = 0
            for other_elem in C:
                if other_elem in graph.neighbors(elem):
                    suma += 1
            suma /= mod_C
            val += suma
        val = val / mod_C
        suma = 0
        for elem in C:
            for other_elem in C:
                if other_elem in graph.neighbors(elem):
                    suma += 1
        val = val * suma
        val_f += val
    return a1 * val_f + a2 * nc_check(chromosome, args['limit'])


def community_fitness(chromosome, args):
    """
    determines the fitness through fitness function on chromosome
    :param chromosome: said chromosome
    :param args: additional arguments
    :return: said fitness
    """
    graph = args['graph']
    a1 = 1
    a2 = 1
    partition = chromosome.get_representation()
    partition = list_to_tuple(partition, graph)
    val_f = 0
    for C in partition:
        val = 0
        for elem in C:
            val_in = 0
            val_out = 0
            for other_elem in C:
                if other_elem in graph.neighbors(elem):
                    val_in += 1
                else:
                    val_out += 1
            val += val_in / (val_in + val_out)
        val_f += val
    return a1 * val_f + a2 * nc_check(chromosome, args['limit'])


def community_modularity(chromosome, args):
    """
    determines the fitness through modularity function on chromosome
    :param chromosome: said chromosome
    :param args: additional arguments
    :return: said fitness
    """
    graph = args['graph']
    a1 = 1
    a2 = 1
    partition = chromosome.get_representation()
    partition = list_to_tuple(partition, graph)
    # return networkx.community.modularity(graph, partition)
    return a1 * networkx.community.modularity(graph, partition) + a2 * nc_check(chromosome, args['limit'])


def community_generator(args):
    """
    generates a random chromosome
    :param args: args for said chromosome
    :return: said chromosome
    """
    graph = args['graph']
    no_nodes = len(graph.nodes)
    limit = no_nodes
    community_partition = [random.randint(1, limit) for _ in range(0, no_nodes)]
    chromosome = Chromosome(community_partition)
    return chromosome


def cross_over(chr1, chr2, args):
    """
    generates a chromosome through crossover of two chromosomes
    :param chr1: one of the chromosomes
    :param chr2: the other chromosome
    :param args: the extra arguments
    :return: the new chromosome
    """
    graph = args['graph']
    index = random.randint(0, len(graph.nodes) - 1)
    repr1 = chr1.get_representation()
    repr2 = chr2.get_representation()
    com = repr1[index]
    my_repr = []
    for i in range(0, len(repr1)):
        my_repr.append(repr2[i])
        if repr1[i] == com:
            my_repr[i] = com
    return Chromosome(my_repr)


def mutation(chromosome, args):
    """
    generates a new chromosome through mutation
    :param chromosome: said chromosome
    :param args: said args
    :return: said generated chromosome
    """
    graph = args['graph']
    limit = len(graph.nodes)
    representation = chromosome.get_representation()
    index = random.randint(0, len(graph.nodes) - 1)
    my_repr = []
    for elem in representation:
        my_repr.append(elem)
    my_repr[index] = random.randint(1, limit)
    return Chromosome(my_repr)
