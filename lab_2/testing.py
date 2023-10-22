import my_graph_module as mgm
import networkx as nx


# grafuri prea mari - le trunchiez
def repair_graph(filename):
    graph = nx.read_gml(filename, label='id')
    while len(graph) > 100:
        graph.remove_node(len(graph) - 1)
    nx.write_gml(graph, filename)


def test_main():
    index = 0
    for filename in mgm.paths:
        print("Testing:" + str(index) + " - " + filename)
        index += 1
        graph = mgm.load_by_path(filename)
        generator_nx = nx.community.girvan_newman(graph)
        generator_me = mgm.my_girvan_newman(graph)
        for elem in generator_nx:
            my_elem = next(generator_me)
            assert (elem == my_elem)
        assert (mgm.partition_nx(graph, 3) == mgm.partition_me(graph, 3))
        print("Finished testing:" + filename)


def run_all_tests():
    print("Running tests...")
    test_main()
    print("Finished running tests!")
