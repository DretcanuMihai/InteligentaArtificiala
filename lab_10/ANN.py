import utils
from Neuron import *


class ANN:
    """
    this ANN is complete
    """

    def __init__(self, hidden_layers_sizes=(5, 5, 5), no_iter=100, learning_rate=0.01):
        """
        creates an ANN with given parameters
        :param hidden_layers_sizes: the sizes of each hidden layer
        :param no_iter: number of iterations
        :param learning_rate: the learning rate
        """
        self.__hidden_layers_sizes = hidden_layers_sizes
        self.__no_iter = no_iter
        self.__learning_rate = learning_rate
        self.__is_ready = False

    def __reset(self, no_inputs, no_outputs):
        """
        resets the ANN
        :return: None
        """
        random.seed(120)
        self.__layers = []
        self.__layers.append([Neuron(0) for _ in range(no_inputs)])
        last_number_of_neurons = no_inputs
        for size in self.__hidden_layers_sizes:
            self.__layers.append([Neuron(last_number_of_neurons) for _ in range(size)])
            last_number_of_neurons = size
        self.__layers.append([Neuron(last_number_of_neurons) for _ in range(no_outputs)])

    def __compute(self, input):
        """
        computes the outputs for an input
        :param input: said input
        :return: a list of said output
        """
        for input_value, neuron in zip(input, self.__layers[0]):
            neuron.output = input_value
            # neuron.output = 1 / (1 + math.exp((-1) * input_value))
        for i in range(1, len(self.__layers)):
            precedent_layer = self.__layers[i - 1]
            current_layer = self.__layers[i]
            for neuron in current_layer:
                neuron.activate([prec_neuron.output for prec_neuron in precedent_layer])

    def __actualize(self, errors):
        """
        actualizes weights
        :param errors: the errors
        :return: None
        """
        last_layer = None
        for layer, error in zip(self.__layers, errors):
            for neuron, index in zip(layer, range(len(layer))):
                ok = False
                for i in range(len(neuron.inputs_weights)):
                    ok = True
                    neuron.inputs_weights[i] -= self.__learning_rate * error[index] * last_layer[i].output
                if ok:
                    neuron.bias -= self.__learning_rate * neuron.bias
            last_layer = layer

    def __back_propagation(self, output):
        """
        executes back propagation
        :param output: the expected output
        :return: None
        """
        output_layer = self.__layers[-1]
        errors = []
        error = []
        for neuron, value in zip(output_layer, output):
            error.append(neuron.output - value)
            # error.append((neuron.output - value) * neuron.output * (1 - neuron.output))
        errors.append(error)
        for index in range(len(self.__layers) - 1):
            # for inverse iteration
            index = len(self.__layers) - index - 2
            error = []
            current_layer = self.__layers[index]
            next_layer = self.__layers[index + 1]
            for i in range(len(current_layer)):
                e = 0.0
                for neuron, j in zip(next_layer, range(len(next_layer))):
                    e += neuron.inputs_weights[i] * errors[0][j]
                error.append(e)
                # error.append(e * current_layer[i].output * (1 - current_layer[i].output))
            errors.insert(0, error)
        self.__actualize(errors)

    def __fit_one(self, inputs, outputs):
        """
        fits the ANN for 1 time with given inputs and outputs
        :param inputs: said inputs
        :param outputs: said outputs
        :return: None
        """
        for input, output in zip(inputs, outputs):
            predicted_output = self.predict_label_brut(input)
            for neuron, value in zip(self.__layers[-1], predicted_output):
                neuron.output = value
            self.__back_propagation(output)

    def fit(self, inputs, outputs):
        """
        fits the ANN for no_iter times with given inputs and outputs
        :param inputs: said inputs
        :param outputs: said outputs
        :return: None
        """
        self.__reset(len(inputs[0]), len(outputs[0]))
        self.__is_ready = True
        for _ in range(self.__no_iter):
            self.__fit_one(inputs, outputs)

    def predict(self, input):
        """
        predicts the output for some input
        :param input: said input
        :return: said output
        """
        if not self.__is_ready:
            raise Exception("Error: network not trained;\n")
        self.__compute(input)
        return [neuron.output for neuron in self.__layers[-1]]

    def predict_label_brut(self, input):
        """
        predicts the output for some input
        :param input: said input
        :return: said output
        """
        return utils.softmax(self.predict(input))

    def predict_label(self, input):
        """
        predicts the labels of an input
        :param input: said input
        :return: said label
        """
        raw_data = self.predict_label_brut(input)
        result = None
        max_value = 0
        for index in range(len(raw_data)):
            if result is None or raw_data[index] > max_value:
                result = index
                max_value = raw_data[index]
        return result
