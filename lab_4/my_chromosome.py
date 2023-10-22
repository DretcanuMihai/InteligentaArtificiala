class Chromosome:
    def __init__(self, representation):
        """
        initialize Chromosome with a representation
        :param representation: said representation
        """
        self.__representation = representation

    def get_representation(self):
        """
        returns the Chromosome's representation
        :return: said representation
        """
        return self.__representation
