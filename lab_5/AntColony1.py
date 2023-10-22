from Ant import Ant
import random

"""
args:
size - amount of entities in a generation
graph - networkx graph
p0 - probability of modification
Q - quantity of pheromone of an ant
alpha - priority of cost
beta - priority of pheromone
ntm - number of edges to modify in generation
ro - evaporation coefficient
"""


class AntColony:
    def __init__(self, args):
        """
        constructs ant colony with given args
        :param args:
        """
        self.__args = args
        self.__best_path = None
        self.__best_cost = None
        self.__current_colony_index = 0
        self.__current_colony = None
        self.__first_initialization()

    def __first_initialization(self):
        """
        initializes the Ant Colony
        :return: None
        """
        graph = self.__args["graph"]
        for u, v in graph.edges:
            graph[u][v]["total_pheromone"] = 1

    def get_current_colony_index(self):
        """
        gets the number of the current colony
        :return: said number
        """
        return self.__current_colony_index

    def get_args(self):
        """
        returns the args of the colony
        :return: said args
        """
        return self.__args

    def get_best_path(self):
        """
        returns the best path
        :return:  said path
        """
        return self.__best_path

    def get_best_cost(self):
        """
        gets the cost of the best path
        :return: said cost
        """
        return self.__best_cost

    def __initialize_next(self):
        """
        initializes next colony
        :return: None
        """
        self.__current_colony_index += 1
        self.__current_colony = []
        positions=[elem for elem in range(0,len(self.__args["graph"]))]
        random.shuffle(positions)
        for k in range(0, self.__args["size"]):
            ant = Ant()
            ant.advance_to(positions[k])
            self.__current_colony.append(ant)

    def __try_to_modify(self):
        """
        tries to modify the graph
        :return: None
        """
        p0 = self.__args["p0"]
        p = random.random()
        if p < p0:
            self.modify()

    def modify(self):
        """
        modifies the graph by altering the costs
        :return: None
        """
        print("GRAPH SUFFERS CHANGES IN COLONY " + str(self.__current_colony_index))
        graph = self.__args["graph"]
        number_to_modify = self.__args["ntm"]
        difference = self.__get_total_cost()
        new_cost = difference / len(graph)
        for _ in range(number_to_modify):
            i = random.randint(0, len(self.__args["graph"]) - 1)
            j = random.randint(0, len(self.__args["graph"]) - 1)
            while j == i:
                j = random.randint(0, len(self.__args["graph"]) - 1)
            if random.randint(0, 1) == 0:
                print("Edge " + str(i) + "-" + str(j) + " removed")
                if graph.has_edge(i, j):
                    graph.remove_edge(i, j)
            else:
                if not graph.has_edge(i, j):
                    old_value = "doesn't exist"
                    graph.add_edge(i, j)
                    graph[i][j]["value"] = new_cost
                    graph[i][j]["total_pheromone"] = 1
                else:
                    old_value = graph[i][j]["value"]
                if random.randint(0, 1) == 0:
                    graph[i][j]["value"] *= 2
                else:
                    graph[i][j]["value"] /= 2
                new_value = graph[i][j]["value"]
                print("Edge " + str(i) + "-" + str(j) + " changed value from " + str(old_value) + " to " +
                      str(new_value))
        self.__best_path = None
        self.__best_cost = None

    def __get_total_cost(self):
        cost = 0
        graph = self.__args["graph"]
        for u, v in graph.edges:
            cost += graph[u][v]["value"]
        return cost

    def __distribute_pheromone(self):
        """
        distributes the pheromone
        :return: None
        """
        Q = self.__args["Q"]
        graph = self.__args["graph"]
        for u, v in graph.edges:
            graph[u][v]["total_pheromone"] *= (1 - self.__args["ro"])
        difference = self.__get_total_cost()
        for ant in self.__current_colony:
            path = ant.get_path()
            total_cost = 0
            for i in range(0, len(path) - 1):
                u, v = path[i], path[i + 1]
                if graph.has_edge(u, v):
                    total_cost += graph[u][v]["value"]
                else:
                    total_cost += difference
            if self.__best_cost is None or total_cost < self.__best_cost:
                self.__best_cost = total_cost
                self.__best_path = path
            Q_for_edge = Q / total_cost
            for i in range(0, len(path) - 1):
                u, v = path[i], path[i + 1]
                if graph.has_edge(u, v):
                    graph[u][v]["total_pheromone"] += Q_for_edge

    def advance_one_colony(self):
        """
        advances by one colony
        :return: None
        """
        self.__try_to_modify()
        self.__initialize_next()
        graph = self.__args["graph"]
        alpha = self.__args["alpha"]
        beta = self.__args["beta"]
        for _ in range(len(graph.nodes) - 1):
            for ant in self.__current_colony:
                path = ant.get_path()
                current_node = path[-1]
                visited_nodes = set(path)
                adjacent_nodes = set(graph.neighbors(current_node))
                visitable_nodes = list(adjacent_nodes.difference(visited_nodes))
                if len(visitable_nodes) != 0:
                    probabilities_partial = []
                    for node in visitable_nodes:
                        pheromone = graph[current_node][node]["total_pheromone"] ** alpha
                        visibility = 1 / graph[current_node][node]["value"]
                        visibility = visibility ** beta
                        probabilities_partial.append(pheromone * visibility)
                    total_sum = sum(probabilities_partial)
                    probabilities_final = [prob / total_sum for prob in probabilities_partial]
                    for i in range(1, len(probabilities_final)):
                        probabilities_final[i] += probabilities_final[i - 1]
                    probabilities_final[-1] = 1.01
                    my_prob = random.random()
                    index = 0
                    while my_prob > probabilities_final[index]:
                        index += 1
                    chosen_node = visitable_nodes[index]
                    ant.advance_to(chosen_node)
                else:
                    visited_nodes = set(path)
                    all_nodes = set([elem for elem in range(len(graph))])
                    visitable_nodes = list(all_nodes.difference(visited_nodes))
                    ant.advance_to(visitable_nodes[random.randint(0, len(visitable_nodes) - 1)])
        for ant in self.__current_colony:
            path = ant.get_path()
            ant.advance_to(path[0])
        self.__distribute_pheromone()
