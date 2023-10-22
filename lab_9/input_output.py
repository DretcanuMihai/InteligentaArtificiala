import MyDataSet as mds
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.datasets import load_iris

import utils


def plot_predicitions_2_traits(data_set, trait1, trait2, trait_label, label_dictionary, regressor):
    """
    plots the prediction with 2 traits
    :param data_set: the data set
    :param trait1: first trait
    :param trait2: second trait
    :param trait_label: label trait
    :param label_dictionary: the dictionary of the label
    :param regressor: the regressor
    :return: None
    """
    feature1 = data_set.get_trait_values(trait1)
    feature2 = data_set.get_trait_values(trait2)
    correct_outputs = data_set.get_trait_values(trait_label)
    computed_outputs = [regressor.predict_label([f1, f2]) for (f1, f2) in zip(feature1, feature2)]
    legnth = len(computed_outputs)
    for crtLabel in label_dictionary:
        x = [feature1[i] for i in range(legnth) if correct_outputs[i] == crtLabel and computed_outputs[i] == crtLabel]
        y = [feature2[i] for i in range(legnth) if correct_outputs[i] == crtLabel and computed_outputs[i] == crtLabel]
        plt.scatter(x, y, label=label_dictionary[crtLabel] + ' (correct)')
    for crtLabel in label_dictionary:
        x = [feature1[i] for i in range(legnth) if correct_outputs[i] == crtLabel and computed_outputs[i] != crtLabel]
        y = [feature2[i] for i in range(legnth) if correct_outputs[i] == crtLabel and computed_outputs[i] != crtLabel]
        plt.scatter(x, y, label=label_dictionary[crtLabel] + ' (incorrect)')
    plt.xlabel(trait1)
    plt.ylabel(trait2)
    plt.legend()
    plt.show()

def load_iris_data():
    """
    loads the iris data set
    :return: said data set
    """
    data = load_iris()
    inputs = data['data']
    outputs = data['target']
    input_names = list(data['feature_names'])
    sepal_length = [feat[input_names.index('sepal length (cm)')] for feat in inputs]
    sepal_width = [feat[input_names.index('sepal width (cm)')] for feat in inputs]
    petal_length = [feat[input_names.index('petal length (cm)')] for feat in inputs]
    petal_width = [feat[input_names.index('petal width (cm)')] for feat in inputs]
    data_set = mds.MyDataSet()
    data_set.add_trait_and_values('sepal length', utils.normalize_data(sepal_length)[0])
    data_set.add_trait_and_values('sepal width', utils.normalize_data(sepal_width)[0])
    data_set.add_trait_and_values('petal length', utils.normalize_data(petal_length)[0])
    data_set.add_trait_and_values('petal width', utils.normalize_data(petal_width)[0])
    data_set.add_trait_and_values('verdict', outputs)
    return data_set

def load_cancer_data():
    """
    loads the cancer data set
    :return: said data set
    """
    data = load_breast_cancer()
    inputs = data['data']
    outputs = data['target']
    input_names = list(data['feature_names'])
    mean_radius = [feat[input_names.index('mean radius')] for feat in inputs]
    mean_texture = [feat[input_names.index('mean texture')] for feat in inputs]
    data_set = mds.MyDataSet()
    data_set.add_trait_and_values('mean radius', utils.normalize_data(mean_radius)[0])
    data_set.add_trait_and_values('mean texture', utils.normalize_data(mean_texture)[0])
    data_set.add_trait_and_values('verdict', outputs)
    return data_set


def plot_labels_2_traits(data_set, trait1, trait2, trait_label, label_dictionary):
    """
    plots points for each label
    :param data_set: the data set
    :param trait1: the first trait
    :param trait2: the second trait
    :param trait_label: the label trait
    :param label_dictionary: a dictionary that maps values to labels
    :return: None
    """
    trait1_values = data_set.get_trait_values(trait1)
    trait2_values = data_set.get_trait_values(trait2)
    output_values = data_set.get_trait_values(trait_label)
    length = len(output_values)
    for label in label_dictionary:
        x = [trait1_values[i] for i in range(length) if output_values[i] == label]
        y = [trait2_values[i] for i in range(length) if output_values[i] == label]
        plt.scatter(x, y, label=label_dictionary[label])
    plt.xlabel(trait1)
    plt.ylabel(trait2)
    plt.legend()
    plt.show()


def plot_histogram(data_set, trait):
    """
    plots the histogram of a trait of a dataset
    :param data_set: said dataset
    :param trait: said trait
    :return: None
    """
    plt.hist(data_set.get_trait_values(trait), 10)
    plt.title('Histogram of ' + trait)
    plt.show()
