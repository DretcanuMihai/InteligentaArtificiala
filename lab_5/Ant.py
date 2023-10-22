class Ant:

    def __init__(self):
        self.__path = []

    def advance_to(self, x):
        """
        advances ant to node x
        :param x: said node
        :return: None
        """
        self.__path.append(x)

    def get_path(self):
        """
        gets the path of the ant
        :return: said path
        """
        return self.__path
