import random

"""
chromosome = Chromosome instance
extended chromosome = (chromosome, fitness)
"""


class GeneticAlgorithm:
    def __init__(self, generator_function, fitness_function, crossover_function, mutation_function, pop_size,
                 jump_mode, args):
        """
        initializes a genetic algorithm
        :param generator_function: a function that generates a random chromosome (args)
        :param fitness_function: a function that returns fitness of chromosome (chromosome, args)
        :param crossover_function: a function that returns a new chromosome from 2 parents (c1,c2,args)
        :param mutation_function: a function that generates a new chromosome (chromosome, args)
        :param pop_size: size of population
        :param jump_mode: the mode of generating new generations
        :param args: arguments to be given to some functions
        """
        self.__generator_function = generator_function
        self.__fitness_function = fitness_function
        self.__crossover_function = crossover_function
        self.__mutation_function = mutation_function
        self.__number_of_entities = pop_size
        self.__args = args
        self.__jump_mode = jump_mode
        self.__initialize()

    def __initialize(self):
        """
        initializes the rest of the GA
        :return: None
        """
        self.__set_jump()
        self.__generation_number = 0
        self.__current_generation = []
        for i in range(0, self.__number_of_entities):
            ex_chromosome = self.__generate_one()
            self.__current_generation.append(ex_chromosome)

    def __jump_one_generation(self):
        """
        jumps one generation with the basic method
        :return: None
        """
        new_generation = []
        for _ in range(0, self.__number_of_entities):
            ex_chr1 = self.__selection()
            ex_chr2 = self.__selection()
            offspring = self.__crossover_function(ex_chr1[0], ex_chr2[0], self.__args)
            offspring = self.__mutation_function(offspring, self.__args)
            ex_offspring = self.__centralize(offspring)
            new_generation.append(ex_offspring)
        self.__current_generation = new_generation
        self.__generation_number += 1

    def __jump_one_generation_elitism(self):
        """
        jumps one generation with the elitism method
        :return: None
        """
        new_generation = [self.get_best_ex_chromosome()]
        for _ in range(0, self.__number_of_entities - 1):
            ex_chr1 = self.__selection()
            ex_chr2 = self.__selection()
            offspring = self.__crossover_function(ex_chr1[0], ex_chr2[0], self.__args)
            offspring = self.__mutation_function(offspring, self.__args)
            ex_offspring = self.__centralize(offspring)
            new_generation.append(ex_offspring)
        self.__current_generation = new_generation
        self.__generation_number += 1

    def __jump_one_generation_steady(self):
        """
        jumps one generation with the steady method
        :return: None
        """
        for _ in range(0, self.__number_of_entities):
            ex_chr1 = self.__selection()
            ex_chr2 = self.__selection()
            offspring = self.__crossover_function(ex_chr1[0], ex_chr2[0], self.__args)
            offspring = self.__mutation_function(offspring, self.__args)
            ex_offspring = self.__centralize(offspring)
            worst_index = self.__worst_ex_chromosome_index()
            if ex_offspring[1] > self.__current_generation[worst_index][1]:
                self.__current_generation[worst_index] = ex_offspring
        self.__generation_number += 1

    def __set_jump(self):
        """
        sets the jump function based on jump_mode
        :return: None
        """
        mode = self.__jump_mode
        if mode == 'elitism':
            self.__jump_function = self.__jump_one_generation_elitism
        elif mode == 'steady':
            self.__jump_function = self.__jump_one_generation_steady
        else:
            self.__jump_function = self.__jump_one_generation

    def __generate_one(self):
        """
        generates a random chromosome
        :return: said chromosome and its fitness
        """
        chromosome = self.__generator_function(self.__args)
        return self.__centralize(chromosome)

    def __centralize(self, chromosome):
        """
        returns chromosome with its fitness
        :param chromosome: a Chromosome
        :return: chromosome and fitness tuple
        """
        fitness = self.__fitness_function(chromosome, self.__args)
        return chromosome, fitness

    def jump_k_generations(self, k):
        """
        jumps k generations
        :param k: number of generations
        :return: None
        """
        for i in range(0, k):
            self.__jump_function()

    def get_mode(self):
        """
        returns the jump mode
        :return: jump mode as string
        """
        return self.__jump_mode

    def get_fitness_function(self):
        """
        returns the fitness function
        :return: said function
        """
        return self.__fitness_function

    def get_generation_number(self):
        """
        gets the current generation number
        :return: said number
        """
        return self.__generation_number

    def get_all_ex_chromosomes(self):
        """
        gets a list of all the current extended chromosomes
        :return: said list
        """
        return self.__current_generation

    def get_best_ex_chromosome(self):
        """
        returns best extended chromosome
        :return: the extended chromosome
        """
        best_ex_chromosome = self.__current_generation[0]
        for ex_chromosome in self.__current_generation:
            if ex_chromosome[1] > best_ex_chromosome[1]:
                best_ex_chromosome = ex_chromosome
        return best_ex_chromosome

    def __get_worst_ex_chromosome(self):
        """
        returns worst extended chromosome
        :return: the extended chromosome
        """
        worst_ex_chromosome = self.__current_generation[0]
        for ex_chromosome in self.__current_generation:
            if ex_chromosome[1] < worst_ex_chromosome[1]:
                worst_ex_chromosome = ex_chromosome
        return worst_ex_chromosome

    def __worst_ex_chromosome_index(self):
        """
        returns index of worst extended chromosome
        :return: said index
        """
        index = 0
        current = 0
        worst_ex_chromosome = self.__current_generation[0]
        for ex_chromosome in self.__current_generation:
            if ex_chromosome[1] < worst_ex_chromosome[1]:
                worst_ex_chromosome = ex_chromosome
                index = current
            current += 1
        return index

    def __selection(self):
        """
        selects a random extended chromosome
        :return: said extended chromosome
        """
        pos1 = random.randint(0, self.__number_of_entities - 1)
        pos2 = random.randint(0, self.__number_of_entities - 1)
        ex_chr1 = self.__current_generation[pos1]
        ex_chr2 = self.__current_generation[pos2]
        if ex_chr1[1] > ex_chr2[1]:
            return ex_chr1
        else:
            return ex_chr2
