import my_graph_module as mgm
import my_genetic_algorithm as mga
import my_path_chromosome as mpc
import random


class Application:
    def __init__(self):
        self.__load_commands()
        self.__graph = mgm.load_by_index(0)
        self.__filename = mgm.paths[0]
        self.__reset_GA()

    def __reset_GA(self):
        self.__GA = None

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
        self.__reset_GA()
        print("Graph loaded successfully")

    def __show_graph(self):
        mgm.show_graph(self.__graph)

    def __write_best(self):
        best_fitness = self.__GA.get_best_ex_chromosome()[1]
        for elem in self.__GA.get_all_ex_chromosomes():
            if elem[1] == best_fitness:
                self.__write_chrom(elem)

    def __begin_genetics(self):
        k = int(input("Number of entities in generation:"))
        if k <= 0:
            print("Invalid number of entities")
            return
        mode = input("normal/elitism/steady:")
        if mode not in ["normal", "elitism", "steady"]:
            print("Invalid mode")
            return
        print("Give equal values to start and finish to find shortest path that goes through each node;")
        start = int(input("Start Node(Index 0):"))
        finish = int(input("Finish Node(Indexed from 0):"))
        if start < 0 or finish < 0 or start >= len(self.__graph.nodes) or finish >= len(self.__graph.nodes):
            print("Invalid path given")
            return
        args = {'graph': self.__graph, 'start': start, 'finish': finish}
        self.__GA = mga.GeneticAlgorithm(mpc.generator, mpc.fitness, mpc.cross_over,
                                         mpc.mutation, k, mode, args)
        self.__write_best()
        print("Initiation successful!")

    def __advance(self):
        if self.__GA is None:
            print("No genetic algorithm started")
            return
        k = int(input("Number of generations to advance:"))
        if k <= 0:
            print("invalid number: should be positive")
            return
        for i in range(0, k):
            self.__GA.jump_one_generation()
            self.__write_best()
        print("Successfully jumped k generations")

    def __write_chrom(self, chrom):
        args = self.__GA.get_args()
        my_file = open("./data/output/log.txt", 'a')
        my_file.write("File:" + self.__filename + "\n")
        my_file.write("Population:" + str(len(self.__GA.get_all_ex_chromosomes())) + "\n")
        my_file.write("Mode:" + self.__GA.get_mode() + "\n")
        my_file.write("Generations:" + str(self.__GA.get_generation_number()) + "\n")
        my_file.write("Fitness:" + str(chrom[1]) + "\n")
        my_file.write("From index:" + str(args['start']) + " To index:" + str(args['finish']) + "\n")
        my_file.write("Path:" + "\n")
        path = chrom[0].get_representation()
        path = mpc.correct_path(path, args)
        for elem in path:
            my_file.write(str(elem) + " ")
        my_file.close()

    def __show_chrom(self, chrom):
        print("Solution Fitness:" + str(chrom[1]))
        path = chrom[0].get_representation()
        args = self.__GA.get_args()
        corrected_path = mpc.correct_path(path, args)
        mgm.show_graph_and_path(self.__graph, corrected_path)

    def __show_GA(self):
        if self.__GA is None:
            print("No genetic algorithm started")
            return
        print("Current generation:" + str(self.__GA.get_generation_number()))
        chrom = self.__GA.get_best_ex_chromosome()
        for elem in self.__GA.get_all_ex_chromosomes():
            if elem[1] == chrom[1]:
                self.__show_chrom(elem)

    def __show_menu(self):
        print("Menu:\n"
              "0.'exit' - stops application\n"
              "1.'menu' - shows menu\n"
              "2.'load' - loads a graph\n"
              "3.'show' - shows a graph\n"
              "4.'begin_genetics' - initiates a genetic algorithm on the current graph\n"
              "5.'advance' - advances k generations on the current graph\n"
              "6.'show_best' - shows best of the current generation\n"
              )

    def __load_commands(self):
        self.__commands = {
            'menu': self.__show_menu,
            'load': self.__load_graph,
            'show': self.__show_graph,
            'begin_genetics': self.__begin_genetics,
            'advance': self.__advance,
            'show_best': self.__show_GA
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
                try:
                    self.__commands[command]()
                except Exception as e:
                    print(str(e))
            else:
                print("Command unrecognized;\nWrite 'menu' to see possible commands")
