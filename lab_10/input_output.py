import MyDataSet as mds
from sklearn.datasets import load_iris
from sklearn.datasets import load_digits
from sklearn.metrics import confusion_matrix
import numpy as np
import matplotlib.pyplot as plt
import itertools
import utils
from skimage import io

def load_my_sepia3():
    """
    loads sepia
    :return: dataset of said sepia
    """
    images = []
    for i in range(130):
        img = io.imread('./data/' + str(i + 1) + '.jpg')
        img = img / 255.0
        aux = []
        for line1 in img:
            for line2 in line1:
                for line3 in line2:
                    aux.append(int(line3))
        images.append(aux)
    data_set = mds.MyDataSet()
    for i in range(3 * 32 * 32):
        input = []
        for image in images:
            input.append(image[i])
        data_set.add_trait_and_values(str(i), utils.normalize_data2(input)[0])
    data_set.add_trait_and_values('verdict', [0 if k < 65 else 1 for k in range(130)])
    return data_set

def load_my_sepia2():
    """
    loads sepia
    :return: dataset of said sepia
    """
    images = []
    for i in range(130):
        img = io.imread('./data/' + str(i + 1) + '.jpg')
        img = img / 255.0
        images.append(img)
    outputs = [0 if k < 65 else 1 for k in range(130)]
    return images, outputs


def load_my_sepia():
    """
    loads sepia
    :return: dataset of said sepia
    """
    images = []
    for i in range(130):
        img = io.imread('./data/' + str(i + 1) + '.jpg')
        aux = []
        for line1 in img:
            for line2 in line1:
                for line3 in line2:
                    aux.append(int(line3))
        images.append(aux)
    data_set = mds.MyDataSet()
    for i in range(3 * 32 * 32):
        input = []
        for image in images:
            input.append(image[i])
        data_set.add_trait_and_values(str(i), utils.normalize_data2(input)[0])
    data_set.add_trait_and_values('verdict', [0 if k < 65 else 1 for k in range(130)])
    return data_set


def load_my_numbers():
    """
    loads numbers
    :return: dataset of said number
    """

    data = load_digits()
    inputs_aux = data.images
    inputs_as_arrays = []
    for input in inputs_aux:
        transformed_input = []
        for line in input:
            for el in line:
                transformed_input.append(float(el))
        inputs_as_arrays.append(transformed_input)
    outputs_aux = data['target']
    outputs = [int(elem) for elem in outputs_aux]

    data_set = mds.MyDataSet()
    for k in range(64):
        trait = []
        for input in inputs_as_arrays:
            trait.append(input[k])
        data_set.add_trait_and_values(str(k), trait)
    data_set.add_trait_and_values('verdict', outputs)
    return data_set


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


def plotConfusionMatrix(cm, classNames):
    """
    plots the confussion matrix
    :param cm:predicted labels
    :param classNames:the name of the labels
    :return:None
    """
    plt.figure()
    plt.imshow(cm, interpolation='nearest', cmap='Blues')
    plt.title('Confusion Matrix ')
    plt.colorbar()
    tick_marks = np.arange(len(classNames))
    plt.xticks(tick_marks, classNames, rotation=45)
    plt.yticks(tick_marks, classNames)
    text_format = 'd'
    thresh = cm.max() / 2.
    for row, column in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(column, row, format(cm[row, column], text_format),
                 horizontalalignment='center',
                 color='white' if cm[row, column] > thresh else 'black')

    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.tight_layout()

    plt.show()


def evalMultiClass(realLabels, computedLabels, labelNames):
    """
    evaluates evaluation
    :param realLabels: the correct labels
    :param computedLabels: the computed labels
    :param labelNames: the name of the labels
    :return: accuracy, precision, recall, confussionMatrix
    """

    confMatrix = confusion_matrix(realLabels, computedLabels)
    acc = sum([confMatrix[i][i] for i in range(len(labelNames))]) / len(realLabels)
    precision = {}
    recall = {}
    for i in range(len(labelNames)):
        precision[labelNames[i]] = confMatrix[i][i] / sum([confMatrix[j][i] for j in range(len(labelNames))])
        recall[labelNames[i]] = confMatrix[i][i] / sum([confMatrix[i][j] for j in range(len(labelNames))])
    return acc, precision, recall, confMatrix
