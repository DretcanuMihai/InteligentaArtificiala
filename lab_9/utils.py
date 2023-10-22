import MyDataSet
import random


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


def normalize_data(my_list, my_mean=None):
    """
    returns the normalized data of a list
    :param my_list: said list
    :param my_mean: said mean
    :return: the normalized list
    """
    if my_mean is None:
        my_mean = sum(my_list) / len(my_list)
    return [elem - my_mean for elem in my_list], my_mean


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


def get_batches(data_set, no_batches_pow=2):
    """
    splits a data_set into 2^pow batches
    :param data_set: said data set
    :param no_batches_pow: the pow
    :return: a list of batches
    """
    result = [data_set]
    for _ in range(no_batches_pow):
        aux = []
        for elem in result:
            half1, half2 = split_in_two(elem, 0.5)
            aux.append(half1)
            aux.append(half2)
        result = aux
    return result


def unite_batches(batches_list):
    """
    unites a list of batches into a single data_set
    :param batches_list: said list
    :return: said data_set
    """
    result = MyDataSet.MyDataSet()
    batch_0 = batches_list[0]
    for trait in batch_0.get_traits():
        to_add = []
        for batch in batches_list:
            values = batch.get_trait_values(trait)
            for elem in values:
                to_add.append(elem)
        result.add_trait_and_values(trait, to_add)
    return result


def split_in_two(data_set, percent):
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
