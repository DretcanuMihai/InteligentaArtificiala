class MyDataSet:

    def __init__(self):
        self.__traits = {}

    def add_trait_and_values(self, trait_name, trait_values):
        """
        adds a trait and its values
        :param trait_name: said trait
        :param trait_values: said values
        :return: None
        """
        self.__traits[trait_name] = trait_values

    def get_traits(self):
        """
        gets the dictionary of traits
        :return: said dictionary
        """
        return self.__traits

    def get_trait_values(self, trait_name):
        """
        gets the values of a trait
        :param trait_name: said trait's name
        :return: said values
        """
        return self.__traits[trait_name]
