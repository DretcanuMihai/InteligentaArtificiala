import math
import random
import numpy

import MyDataSet


def softmax(values):
    """
    applies softmax on a list of values
    :param values: said list of values
    :return: softmaxed values
    """
    result = []
    for value in values:
        to_add = math.exp(value)
        result.append(to_add)
    my_sum = sum(result)
    return [value / my_sum for value in result]


def extract_input_output(data_set, input_names, output_names):
    """
    extracts the input and output from a data set
    :param data_set: said data set
    :param input_names: the name of input traits
    :param output_names: the name of output traits
    :return: input and output
    """
    input_values = []
    output_values = []
    for trait_name in input_names:
        input_values.append(data_set.get_trait_values(trait_name))
    for trait_name in output_names:
        output_values.append(data_set.get_trait_values(trait_name))
    return input_values, output_values

def get_index_split(length, percent):
    """
    returns a partition in 2 of a list of indexes [0,1,...,length-1]
    :param length: the number of indexes
    :param percent: the percent of indexes in the first part
    :return: first part and second part
    """
    indexes = [i for i in range(length)]
    random.shuffle(indexes)
    limit = int(percent * length)
    first_part = []
    second_part = []
    for i in range(length):
        if indexes[i] < limit:
            first_part.append(i)
        else:
            second_part.append(i)
    return first_part, second_part


def transform_samples(my_list):
    """
    transforms the samples
    :param my_list: said sample list
    :return: transformed samples
    """
    result = []
    for _ in range(len(my_list[0])):
        result.append([])
    for trait in my_list:
        for sublist, value in zip(result, trait):
            sublist.append(value)
    return [numpy.array(elem) for elem in result]


def split_in_two_2(my_lists, percent=0.8):
    """
    splits a data set into training and validation
    :param data_set: said data set
    :param percent: the percent of training data
    :return: a training and a validation data set
    """
    training_indexes, validation_indexes = get_index_split(len(my_lists[0]), percent)
    training_data_set = []
    validation_data_set = []
    for my_list in my_lists:
        training_values = []
        for i in training_indexes:
            training_values.append(my_list[i])
        training_data_set.append(training_values)

        validation_values = []
        for i in validation_indexes:
            validation_values.append(my_list[i])
        validation_data_set.append(validation_values)
    return training_data_set, validation_data_set


def split_in_two(data_set, percent=0.8):
    """
    splits a data set into training and validation
    :param data_set: said data set
    :param percent: the percent of training data
    :return: a training and a validation data set
    """
    traits = data_set.get_traits()
    length = 0
    for trait in traits:
        length = len(traits[trait])
        break
    training_indexes, validation_indexes = get_index_split(length, percent)
    training_data_set = MyDataSet.MyDataSet()
    validation_data_set = MyDataSet.MyDataSet()
    for trait in traits:
        values = data_set.get_trait_values(trait)

        training_values = []
        for i in training_indexes:
            training_values.append(values[i])
        training_data_set.add_trait_and_values(trait, training_values)

        validation_values = []
        for i in validation_indexes:
            validation_values.append(values[i])
        validation_data_set.add_trait_and_values(trait, validation_values)
    return training_data_set, validation_data_set


def transform_input_labels(my_input, no_labels):
    """
    transform an input label list
    :param my_input: said input
    :param no_labels: the number of labels
    :return: the transformed input
    """
    return [[1 if label == value else 0 for label in range(no_labels)] for value in my_input]
