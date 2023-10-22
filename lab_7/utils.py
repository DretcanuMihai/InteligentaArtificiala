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

def normalize_data(my_list):
    """
    returns the normalized data of a list
    :param my_list: said list
    :return: the normalized list
    """
    minimum=min(my_list)
    maximum=max(my_list)
    my_range=maximum-minimum
    return [(elem-minimum)/my_range for elem in my_list]


def get_index_split(length, percent):
    """
    returns a partition in 2 of a list of indexes [0,1,...,length-1]
    :param length: the number of indexes
    :param percent: the percent of indexes in the first part
    :return: first part and second part
    """
    random.seed(1142)
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


def split_training_validation(data_set, training_percent):
    """
    splits a data set into training and validation
    :param data_set: said data set
    :param training_percent: the percent of training data
    :return: a training and a validation data set
    """
    traits = data_set.get_traits()
    length = 0
    for trait in traits:
        length = len(traits[trait])
        break
    training_indexes, validation_indexes = get_index_split(length, training_percent)
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

