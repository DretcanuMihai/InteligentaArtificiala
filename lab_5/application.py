import AntColony
import AntColony1
import my_graph_module as mgm
import random


class Application:
    def __init__(self):
        self.__load_commands()
        self.__graph = mgm.load_by_index(0)
        self.__filename = mgm.paths[0]
        self.__reset_AS()

    def __reset_AS(self):
        self.__AC = None

    def __load_graph(self):
        print("Choose graph sample:\n")
        start = 0
        for elem in mgm.paths:
            print(str(start) + ". - " + elem)
            start += 1
        index = int(input("Index:"))
        if index < 0:
            raise Exception("Error: index shouldn't be negative")
        self.__graph = mgm.load_by_index(index)
        self.__filename = mgm.paths[index]
        self.__reset_AS()
        print("Graph loaded successfully")

    def __show_graph(self):
        mgm.show_graph(self.__graph)

    def __total_cost(self):
        cost = 0
        for u, v in self.__graph.edges:
            cost += self.__graph[u][v]["value"]
        return cost

    def __begin_colony(self):
        k = int(input("Number of entities in colony:"))
        if k <= 0:
            print("Invalid number of entities")
            return
        p0 = float(input("probability of modification:"))
        if p0 < 0 or 1 < p0:
            print("Invalid probability")
            return
        ntm = int(input("number of modifications:"))
        if ntm < 0:
            print("Invalid number")
            return
        ro = float(input("ro:"))
        if ro < 0 or 1 < ro:
            print("Invalid percent")
            return
        alpha = float(input("alpha:"))
        beta = float(input("beta:"))
        args = {'size': k, 'graph': self.__graph, 'p0': p0, 'Q': 1, 'alpha': alpha, 'beta': beta,
                'ntm': ntm, 'ro': ro}
        self.__AC = AntColony1.AntColony(args)
        print("Initiation successful!")

    def __advance(self):
        if self.__AC is None:
            print("No genetic algorithm started")
            return
        k = int(input("Number of colonies to advance:"))
        if k <= 0:
            print("invalid number: should be positive")
            return
        for i in range(0, k):
            self.__AC.advance_one_colony()
            self.__write_best()
        print("Successfully jumped k generations")

    def __write_best(self):
        args = self.__AC.get_args()
        my_file = open("./data/output/log.txt", 'a')
        my_file.write("File:" + self.__filename + "\n")
        my_file.write("Population:" + str(args["size"]) + "\n")
        my_file.write("Colony Index:" + str(self.__AC.get_current_colony_index()) + "\n")
        my_file.write("Cost:" + str(self.__AC.get_best_cost()) + "\n")
        my_file.write("Alpha"+str(args["alpha"]))
        my_file.write("Beta"+str(args["beta"]))
        my_file.write("Path:" + "\n")
        path = self.__AC.get_best_path()
        for elem in path:
            my_file.write(str(elem) + " ")
        my_file.write("\n")
        my_file.close()

    def __show_best(self):
        cost = self.__AC.get_best_cost()
        path = self.__AC.get_best_path()
        print("Solution Cost:" + str(cost))
        args = self.__AC.get_args()
        mgm.show_graph_and_path(args["graph"], path)

    def __show_menu(self):
        print("Menu:\n"
              "0.'exit' - stops application\n"
              "1.'menu' - shows menu\n"
              "2.'load' - loads a graph\n"
              "3.'show' - shows a graph\n"
              "4.'begin' - initiates a genetic algorithm on the current graph\n"
              "5.'advance' - advances k colonies on the current graph\n"
              "6.'show_best' - shows best of the current generation\n"
              "7.'modify' - modifies graph\n"
              )

    def __modify(self):
        self.__AC.modify()
        print("Modification completed")

    def __load_commands(self):
        self.__commands = {
            'menu': self.__show_menu,
            'load': self.__load_graph,
            'show': self.__show_graph,
            'begin': self.__begin_colony,
            'advance': self.__advance,
            'show_best': self.__show_best,
            'modify':self.__modify
        }

    def run(self):
        random.seed(123)
        print("Application started;\nWrite 'menu' to see possible commands")
        while True:
            command = input(">>>")
            if command == 'exit':
                print("Closing Application...")
                break
            elif command in self.__commands:
                self.__commands[command]()
            else:
                print("Command unrecognized;\nWrite 'menu' to see possible commands")
