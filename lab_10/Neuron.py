import random
import math


class Neuron:
    def __init__(self, no_inputs):
        """
        creates a neuron
        :param no_inputs: the number of neurons that enter it
        """
        self.inputs_weights = [random.random() - 0.5 for _ in range(no_inputs)]
        self.bias = random.random() - 0.5
        self.output = 0.0

    def activate(self, values):
        """
        activates a neuron, setting its output
        :param values: the input values
        :return: None
        """
        self.output = self.bias + sum([value * weight for value, weight in zip(values, self.inputs_weights)])
        # self.output = 1 / (1 + math.exp((-1) * (self.bias + sum([value * weight for value, weight in zip(values, self.inputs_weights)]))))
        # relu
        # self.output=max([0,self.output])
