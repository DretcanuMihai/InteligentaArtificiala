import random

import numpy


class MyHybrid:
    def __init__(self, distanceFunction, noLabels):
        """
        creates an KNN algorithm
        :param distanceFunction: the function used to measure the distance
        :param noLabels: number of labels
        """
        self.__distanceFunction = distanceFunction
        self.__noLabels = noLabels
        self.__isTrained = False

    def __reset(self, inputs, outputs):
        """
        resets the KNN
        :param inputs: the inputs
        :param outputs: the outputs
        :return: None
        """
        self.__centroids = []
        for i in range(self.__noLabels):
            k = random.randint(0, len(outputs) - 1)
            while outputs[k] != i:
                k = random.randint(0, len(outputs) - 1)
            self.__centroids.append(inputs[k])

    def train(self, inputs, outputs, epochs=10):
        """
        the trains a KNN with given inputs and outputs
        :param inputs: said inputs
        :param outputs: said outputs
        :return: None
        """
        self.__reset(inputs, outputs)
        self.__isTrained = True
        for i in range(epochs):
            accumulator = [numpy.array([float(0) for _ in centroid]) for centroid in self.__centroids]
            amount = [0 for _ in self.__centroids]
            for input in inputs:
                myLabel = self.predict(input)
                accumulator[myLabel] += input
                amount[myLabel] += 1
            for i in range(len(self.__centroids)):
                if (amount[i] != 0):
                    self.__centroids[i] = accumulator[i] / amount[i]


    def predict(self, input):
        """
        predicts the output for an input
        :param input: said input
        :return: said prediction
        """
        if not self.__isTrained:
            raise Exception("model is not trained")
        myLabel = None
        distance = 0
        for i in range(len(self.__centroids)):
            currentDistance = self.__distanceFunction(input, self.__centroids[i])
            if myLabel is None or distance > currentDistance:
                myLabel = i
                distance = currentDistance
        return myLabel


def bagDistance(a, b):
    """
    computes the distance between inputs a and b
    :param a: an input
    :param b: another input
    :return: said distance
    """
    dist = 0
    for val in a - b:
        dist += val ** 2
    return dist ** (1 / 2)
