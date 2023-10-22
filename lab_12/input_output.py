from sklearn.metrics import confusion_matrix
import numpy as np
import matplotlib.pyplot as plt
import itertools
from skimage import io
import pandas as pd


def load_my_fer5(no_samples=200):
    """
    loads fer
    :param no_samples: the number of samples
    :return: dataset of said fer
    """
    from cv2 import CascadeClassifier
    from cv2 import imread
    import cv2
    classifier = CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    images = []
    for i in range(no_samples):
        img = imread('./faces/' + str(i) + '.png')
        result=classifier.detectMultiScale(img)
        if(len(result)!=0):
            x1, y1, width, height = result[0]
            x2, y2 = x1 + width, y1 + height
            img = img[x1:x2, y1:y2]
            img = cv2.resize(img, (48, 48))
        images.append(img)

    data = pd.read_csv('./faces/train.csv')
    outputs = list(data['emotion'].to_list())[:no_samples]
    return images, outputs


def load_my_fer4(no_samples=200):
    """
    loads fer
    :param no_samples: the number of samples
    :return: dataset of said fer
    """
    images = []
    outputs = []
    for i in range(no_samples):
        img = io.imread('./faces/' + str(i) + '.png')
        img = img / 255.0
        images.append(img)
        with open('./face_multi/' + str(i) + '.txt') as myfile:
            result = []
            for i in myfile.readline().split(' ')[:-1]:
                result.append(int(i))
            outputs.append(np.array(result))
    return images, outputs


def load_my_fer3(no_samples=200):
    """
    loads fer
    :param no_samples: the number of samples
    :return: dataset of said fer
    """
    images = []
    for i in range(no_samples):
        img = io.imread('./faces/' + str(i) + '.png')
        img = img / 255.0
        images.append(img)
    data = pd.read_csv('./faces/train.csv')
    outputs = list(data['emotion'].to_list())[:no_samples]
    return images, outputs


def load_my_fer2(no_samples=200):
    """
    loads fer
    :param no_samples: the number of samples
    :return: dataset of said fer
    """
    data = pd.read_csv('./faces/train.csv')

    inputs = ['./faces/' + str(i) + '.png' for i in range(no_samples)]
    outputs = list(data['emotion'].to_list())[:no_samples]

    return inputs, outputs


def load_my_fer(no_samples=200):
    """
    loads fer
    :param no_samples: the number of samples
    :return: dataset of said fer
    """

    data = pd.read_csv('./faces/train.csv')
    no_samples = len(data['emotion'].to_list())

    def string2pixel(mylist):
        """
        transforms a string array to a pixel array
        :param mylist: said string array
        :return: said pixel array
        """
        # aux = [int(pixel) for pixel in mylist]
        aux = [np.array([int(pixel), int(pixel), int(pixel)]) for pixel in mylist]
        my_photo = []
        for i in range(48):
            line = []
            for j in range(48):
                line.append(aux[i * 48 + j])
            my_photo.append(np.array(line))
        my_photo = np.array(my_photo)
        return my_photo

    outputs = list(data['emotion'].to_list())[:no_samples]
    for i in range(len(outputs)):
        with open("./face_multi/" + str(i) + '.txt', 'w') as f:
            result = ""
            value = [1 if v == outputs[i] else 0 for v in range(7)]
            for v in value:
                result += str(v) + " "
            f.write(result)


def load_my_emojis():
    """
    loads sepia
    :return: dataset of said sepia
    """
    images = []
    for i in range(100):
        img = io.imread('./emojis/' + str(i) + '.jpg')
        img = img / 255.0
        images.append(img)
    outputs = [0 if k < 50 else 1 for k in range(100)]
    return images, outputs


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
