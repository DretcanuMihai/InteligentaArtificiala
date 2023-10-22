import my_graph_module as mgm


class Application:
    def __init__(self):
        self.__load_commands()
        self.__graph = mgm.load_by_index(0)
        self.__partition = None

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
        self.__partition = None
        print("Graph loaded successfully")

    def __show_graph(self):
        mgm.show_graph(self.__graph)

    def __partition1(self):
        k = int(input("How many communities:"))
        self.__partition = mgm.partition_nx(self.__graph, k)
        if self.__partition is None:
            print("No such partition found - partition reset")
        print("Partition loaded successfully")

    def __partition2(self):
        k = int(input("How many communities:"))
        self.__partition = mgm.partition_me(self.__graph, k)
        if self.__partition is None:
            print("No such partition found - partition reset")
        print("Partition loaded successfully")

    def __partition1q(self):
        self.__partition = mgm.best_partition_nx(self.__graph)
        print("Partition loaded successfully")

    def __partition2q(self):
        self.__partition = mgm.best_partition_me(self.__graph)
        print("Partition loaded successfully")

    def __show_partition(self):
        mgm.show_graph(self.__graph, self.__partition)

    def __show_menu(self):
        print("Menu:\n"
              "0.'exit' - stops application\n"
              "1.'menu' - shows menu\n"
              "2.'load' - loads a graph\n"
              "3.'show' - shows a graph\n"
              "4.'partition1' - partitions network in k communities using nx\n"
              "5.'partition2' - partitions network in k communities using own algorithm\n"
              "6.'partition1Q' - best partitions network using nx\n"
              "7.'partition2Q' - best partitions network using own algorithm\n"
              "8.'show_partition' - shows a graph's generated communities partition\n")

    def __load_commands(self):
        self.__commands = {
            'menu': self.__show_menu,
            'load': self.__load_graph,
            'show': self.__show_graph,
            'partition1': self.__partition1,
            'partition2': self.__partition2,
            'partition1Q': self.__partition1q,
            'partition2Q': self.__partition2q,
            'show_partition': self.__show_partition
        }

    def run(self):
        print("Application started;\nWrite 'menu' to see possible commands")
        while True:
            command = input(">>>")
            if command == 'exit':
                print("Closing Application...")
                break
            elif command in self.__commands:
                try:
                    self.__commands[command]()
                except Exception as exception:
                    print(str(exception))
            else:
                print("Command unrecognized;\nWrite 'menu' to see possible commands")
