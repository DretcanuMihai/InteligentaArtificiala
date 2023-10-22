import numpy
from sklearn.metrics import confusion_matrix
import numpy as np
import matplotlib.pyplot as plt
import itertools
import pandas
import MyDataSet as mds
import re


def transform2(myList):
    """
    transform list for emotions
    :param myList: said list
    :return: the transformed list
    """
    my_bag = set()
    aux = []

    def ngram2(words):
        """
        transforms words in 2grams
        :param words: said words
        :return: said 2grams
        """
        new_words = []
        for i in range(len(words) - 1):
            if words[i] != "" and words[i + 1] != "":
                new_words.append(words[i] + " " + words[i + 1])
        return new_words

    for sentence in myList:
        sentence = sentence.lower()
        words = re.split('[^a-zA-Z0-9]', sentence)
        words = ngram2(words)
        aux.append(words)
        for elem in words:
            my_bag.add(elem)
    my_bag = list(my_bag)
    result = []

    def countWords2(myList, word):
        """
        returns the word count in a list
        :param myList: said list
        :param word: said word
        :return: said count
        """
        amount = 0
        for elem in myList:
            if elem == word:
                amount += 1
        return amount

    for elem in aux:
        current_bag = []
        for word in my_bag:
            val = countWords2(elem, word)
            current_bag.append(float(val))
        result.append(numpy.array(current_bag))
    return result


def loadEmotions2():
    """
    loads emotions dataset
    :return: said dataset
    """
    filename = "./data/reviews_mixed.csv"
    data = pandas.read_csv(filename)
    data_set = mds.MyDataSet()
    data_set.add_trait_and_values("Text", transform2(data["Text"].to_list()))
    data_set.add_trait_and_values("Sentiment", [0 if elem == 'negative' else 1 for elem in data["Sentiment"].to_list()])
    return data_set


def transform(myList):
    """
    transform list for emotions
    :param myList: said list
    :return: the transformed list
    """
    my_bag = set()
    aux = []
    for sentence in myList:
        sentence = sentence.lower()
        words = re.split('[^a-zA-Z0-9]', sentence)
        aux.append(words)
        for elem in words:
            my_bag.add(elem)
    my_bag.remove("")
    my_bag = list(my_bag)
    result = []

    def countWords(myList, word):
        """
        returns the word count in a list
        :param myList: said list
        :param word: said word
        :return: said count
        """
        amount = 0
        for elem in myList:
            if elem == word:
                amount += 1
        return amount

    for elem in aux:
        current_bag = []
        for word in my_bag:
            val = countWords(elem, word)
            current_bag.append(float(val))
        result.append(numpy.array(current_bag))
    return result


def loadEmotions():
    """
    loads emotions dataset
    :return: said dataset
    """
    filename = "./data/reviews_mixed.csv"
    data = pandas.read_csv(filename)
    data_set = mds.MyDataSet()
    data_set.add_trait_and_values("Text", transform(data["Text"].to_list()))
    data_set.add_trait_and_values("Sentiment", [0 if elem == 'negative' else 1 for elem in data["Sentiment"].to_list()])
    return data_set


def loadEmotions3():
    """
    loads emotions dataset
    :return: said dataset
    """
    filename = "./data/reviews_mixed.csv"
    data = pandas.read_csv(filename)
    data_set = mds.MyDataSet()
    data_set.add_trait_and_values("Sentiment", [0 if elem == 'negative' else 1 for elem in data["Sentiment"].to_list()])
    data_set.add_trait_and_values("Text", transform3(data["Text"].to_list(), data_set.get_trait_values('Sentiment')))
    return data_set


def transform3(myList, outputs):
    """
    transform list for emotions
    :param myList: said list
    :return: the transformed list
    """
    my_bag = {}
    aux = []
    for sentence, output in zip(myList, outputs):
        sentence = sentence.lower()
        words = re.split('[^a-zA-Z0-9]', sentence)
        aux.append(words)
        for elem in words:
            if elem not in my_bag:
                my_bag[elem] = 0
            my_bag[elem] += 2*output-1
    del my_bag[""]
    my_bag_aux = list(my_bag)
    result = []

    def countWords(myList, word):
        """
        returns the word count in a list
        :param myList: said list
        :param word: said word
        :return: said count
        """
        amount = 0
        for elem in myList:
            if elem == word:
                amount += 1
        return amount

    for elem in aux:
        current_bag = []
        for word in my_bag_aux:
            val = countWords(elem, word)
            current_bag.append(float(val)*my_bag[word])
        result.append(numpy.array(current_bag))
    return result


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
