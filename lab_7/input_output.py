import math

import numpy as np
import sklearn.metrics

import MyDataSet as mds
import pandas
import matplotlib.pyplot as plt

import performance_metrics


def read_csv(filename, traits):
    """
    gets the predicted data and correct data from a data set resulted from pandas reading a csv file
    :param filename: the name of the csv file
    :return: a data set of said data
    """
    data = pandas.read_csv(filename)
    data_set = mds.MyDataSet()
    my_set = set()
    for elem in traits:
        data_set.add_trait_and_values(elem, data[elem].to_list())
    for elem in traits:
        values = data_set.get_trait_values(elem)
        for i in range(len(values)):
            if math.isnan(values[i]):
                my_set.add(i)
    my_set = list(my_set)
    my_set.sort()
    my_set.reverse()
    for index in my_set:
        for trait in traits:
            del data_set.get_trait_values(trait)[index]
    return data_set


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


def plot_2_traits(data_set, trait1, trait2):
    """
    plots the dependency of trait1 to trait2
    :param data_set: the data set
    :param trait1: first trait
    :param trait2: second trait
    :return: None
    """
    plt.plot(data_set.get_trait_values(trait1), data_set.get_trait_values(trait2), 'ro')
    plt.xlabel(trait1)
    plt.ylabel(trait2)
    plt.show()


def plot_3_traits(data_set, trait1, trait2, trait3):
    """
    plots the dependency of trait1 and trait2 to trait3
    :param data_set: the data set
    :param trait1: first trait
    :param trait2: second trait
    :param trait3: third trait
    :return: None
    """

    ax = plt.axes(projection='3d')
    ax.plot3D(data_set.get_trait_values(trait1), data_set.get_trait_values(trait2), data_set.get_trait_values(trait3),
              'ro')
    ax.set_xlabel(trait1)
    ax.set_ylabel(trait2)
    ax.set_zlabel(trait3)
    plt.show()


def plot_training_validation_2_traits(training_data_set, validation_data_set, trait1, trait2):
    """
    plots the training and validation data for 2 traits
    :param training_data_set: the training data
    :param validation_data_set: the validation data
    :param trait1: first trait
    :param trait2: second trait
    :return: None
    """
    plt.plot(training_data_set.get_trait_values(trait1), training_data_set.get_trait_values(trait2),
             'ro', label='training data')  # train data are plotted by red and circle sign
    plt.plot(validation_data_set.get_trait_values(trait1), validation_data_set.get_trait_values(trait2), 'g^',
             label='validation data')  # test data are plotted by green and a triangle sign
    plt.title('train and validation data')
    plt.xlabel(trait1)
    plt.ylabel(trait2)
    plt.legend()
    plt.show()


def plot_training_validation_3_traits(training_data_set, validation_data_set, trait1, trait2, trait3):
    """
    plots the training and validation data for 2 traits
    :param training_data_set: the training data
    :param validation_data_set: the validation data
    :param trait1: first trait
    :param trait2: second trait
    :return: None
    """
    ax = plt.axes(projection='3d')
    ax.plot3D(training_data_set.get_trait_values(trait1), training_data_set.get_trait_values(trait2),
              training_data_set.get_trait_values(trait3),
              'ro', label='training data')
    ax.plot3D(validation_data_set.get_trait_values(trait1), validation_data_set.get_trait_values(trait2),
              validation_data_set.get_trait_values(trait3),
              'g^', label='validation data')
    ax.set_xlabel(trait1)
    ax.set_ylabel(trait2)
    ax.set_zlabel(trait3)
    plt.legend()
    plt.show()


def plot_my_regression_2_traits_line(data_set, trait1, trait2, my_regressor):
    """
    plots a regression with 2 traits
    :param data_set: the training data set
    :param trait1: first trait
    :param trait2: second trait
    :param my_regressor: said regressor
    :return: None
    """
    no_of_points = 1000
    xref = []
    inputs = data_set.get_trait_values(trait1)
    val = min(inputs)
    step = (max(inputs) - min(inputs)) / no_of_points
    for i in range(0, no_of_points):
        xref.append(val)
        val += step
    w = my_regressor.get_coefficients()
    yref = [w[0] + w[1] * el for el in xref]
    outputs = data_set.get_trait_values(trait2)
    plt.plot(inputs, outputs, 'ro')  # train data are plotted by red and circle sign
    plt.plot(xref, yref, 'b-')  # model is plotted by a blue line
    plt.xlabel(trait1)
    plt.ylabel(trait2)
    plt.legend()
    plt.show()


def plot_my_regression_3_traits_line(data_set, trait1, trait2, trait3, my_regressor):
    """
    plots a regression with 3 traits
    :param data_set: the training data set
    :param trait1: first trait
    :param trait2: second trait
    :param trait3: third trait
    :param my_regressor: said regressor
    :return: None
    """

    w = my_regressor.get_coefficients()
    x_ref = data_set.get_trait_values(trait1)
    y_ref = data_set.get_trait_values(trait2)
    no_points = 5
    stx = min(x_ref)
    finx = max(x_ref)
    stepx = (finx - stx) / no_points
    sty = min(y_ref)
    finy = max(y_ref)
    stepy = (finy - sty) / no_points
    (p1, p2) = np.meshgrid(np.arange(stx, finx, stepx), np.arange(sty, finy, stepy))
    p3 = w[0] + w[1] * p1 + w[2] * p2
    ax = plt.axes(projection='3d')
    ax.plot_surface(p1, p2, p3, alpha=0.2)
    ax.plot3D(data_set.get_trait_values(trait1), data_set.get_trait_values(trait2),
              data_set.get_trait_values(trait3), 'ro')
    ax.set_xlabel(trait1)
    ax.set_ylabel(trait2)
    ax.set_zlabel(trait3)
    #ax.set_zlim(0, 10)
    plt.legend()
    plt.show()


def plot_my_regression_2_traits_points(data_set, trait1, trait2, my_regressor):
    """
    plots a regression with 2 traits
    :param data_set: the training data set
    :param trait1: first trait
    :param trait2: second trait
    :param my_regressor: said regressor
    :return: None
    """
    computed_outputs = [my_regressor.predict([x]) for x in data_set.get_trait_values(trait1)]

    # plot the computed outputs (see how far they are from the real outputs)
    plt.plot(data_set.get_trait_values(trait1), computed_outputs,
             'yo')  # computed test data are plotted yellow red and circle sign
    plt.plot(data_set.get_trait_values(trait1), data_set.get_trait_values(trait2),
             'g^')  # real test data are plotted by green triangles
    plt.xlabel(trait1)
    plt.ylabel(trait2)
    plt.legend()
    plt.show()


def plot_my_regression_3_traits_points(data_set, trait1, trait2, trait3, my_regressor):
    """
    plots a regression with 2 traits
    :param data_set: the training data set
    :param trait1: first trait
    :param trait2: second trait
    :param my_regressor: said regressor
    :return: None
    """
    predicted_outputs = [my_regressor.predict([x, y]) for x, y in
                         zip(data_set.get_trait_values(trait1), data_set.get_trait_values(trait2))]
    correct_outputs = data_set.get_trait_values(trait3)

    ax = plt.axes(projection='3d')
    ax.plot3D(data_set.get_trait_values(trait1), data_set.get_trait_values(trait2),
              correct_outputs, 'ro')
    ax.plot3D(data_set.get_trait_values(trait1), data_set.get_trait_values(trait2),
              predicted_outputs, 'g^')
    ax.set_xlabel(trait1)
    ax.set_ylabel(trait2)
    ax.set_zlabel(trait3)
    plt.legend()
    plt.show()


def print_error_2_traits(data_set, trait1, trait2, my_regressor):
    """
    prints the error of a regression
    :param data_set: the training data set
    :param trait1: first trait
    :param trait2: second trait
    :param my_regressor: said regressor
    :return: None
    """
    predicted_outputs = [my_regressor.predict([x]) for x in data_set.get_trait_values(trait1)]
    correct_outputs = data_set.get_trait_values(trait2)
    error = performance_metrics.MSE(predicted_outputs, correct_outputs)
    print(error)
    error = sklearn.metrics.mean_squared_error(correct_outputs, predicted_outputs)
    print(error)


def print_error_3_traits(data_set, trait1, trait2, trait3, my_regressor):
    """
    prints the error of a regression
    :param data_set: the training data set
    :param trait1: first trait
    :param trait2: second trait
    :param trait3: third trait
    :param my_regressor: said regressor
    :return: None
    """
    predicted_outputs = [my_regressor.predict([x, y]) for x, y in
                         zip(data_set.get_trait_values(trait1), data_set.get_trait_values(trait2))]
    correct_outputs = data_set.get_trait_values(trait3)
    error = performance_metrics.MSE(predicted_outputs, correct_outputs)
    print(error)
    error = sklearn.metrics.mean_squared_error(correct_outputs, predicted_outputs)
    print(error)
