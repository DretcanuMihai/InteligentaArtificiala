import random

import MyHybrid
import MyKMeans
import utils

from input_output import *

value = 2

if value == 1:
    random.seed(101)
    input_labels = ['Text']
    output_labels = ['Sentiment']
    labels = ['negative', 'positive']
    data_set = loadEmotions()

    training_set, validation_set = utils.split_in_two(data_set)

    training_input, training_output = training_set.get_trait_values(input_labels[0]), training_set.get_trait_values(
        output_labels[0])

    validation_input, validation_output = validation_set.get_trait_values(
        input_labels[0]), validation_set.get_trait_values(
        output_labels[0])

    myKNN = MyKMeans.MyKMeans(MyKMeans.bagDistance, 2)
    centroids = []
    for i in range(2):
        k = random.randint(0, len(training_output) - 1)
        while training_output[k] != i:
            k = random.randint(0, len(training_output) - 1)
        # while k in centroids:
        #    k = random.randint(0, len(training_output) - 1)
        centroids.append(k)
    myKNN.train(training_input, centroids, epochs=20)

    predicted_output = [myKNN.predict(my_input) for my_input in validation_input]

    acc, prec, recall, cm = evalMultiClass(validation_output, np.array(predicted_output),
                                           labels)
    print('acc: ', acc)
    print('precision: ', prec)
    print('recall: ', recall)
    plotConfusionMatrix(cm, labels)

# ngram (2gram)
elif value == 2:
    random.seed(101)
    input_labels = ['Text']
    output_labels = ['Sentiment']
    labels = ['negative', 'positive']
    data_set = loadEmotions2()

    training_set, validation_set = utils.split_in_two(data_set)

    training_input, training_output = training_set.get_trait_values(input_labels[0]), training_set.get_trait_values(
        output_labels[0])

    validation_input, validation_output = validation_set.get_trait_values(
        input_labels[0]), validation_set.get_trait_values(
        output_labels[0])

    myKNN = MyKMeans.MyKMeans(MyKMeans.bagDistance, 2)
    centroids = []
    random.seed(567)
    for i in range(2):
        k = random.randint(0, len(training_output) - 1)
        while training_output[k] != i:
            k = random.randint(0, len(training_output) - 1)
        centroids.append(k)
    myKNN.train(training_input, centroids, epochs=1)

    predicted_output = [myKNN.predict(my_input) for my_input in validation_input]

    acc, prec, recall, cm = evalMultiClass(validation_output, np.array(predicted_output),
                                           labels)
    print('acc: ', acc)
    print('precision: ', prec)
    print('recall: ', recall)
    plotConfusionMatrix(cm, labels)

elif value == 3:
    random.seed(101)
    input_labels = ['Text']
    output_labels = ['Sentiment']
    labels = ['negative', 'positive']
    data_set = loadEmotions()

    training_set, validation_set = utils.split_in_two(data_set)

    training_input, training_output = training_set.get_trait_values(input_labels[0]), training_set.get_trait_values(
        output_labels[0])

    validation_input, validation_output = validation_set.get_trait_values(
        input_labels[0]), validation_set.get_trait_values(
        output_labels[0])

    from sklearn.neural_network import MLPClassifier

    clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
    clf.fit(training_input, training_output)

    predicted_output = clf.predict(validation_input)

    acc, prec, recall, cm = evalMultiClass(validation_output, np.array(predicted_output),
                                           labels)
    print('acc: ', acc)
    print('precision: ', prec)
    print('recall: ', recall)
    plotConfusionMatrix(cm, labels)

elif value == 4:
    random.seed(101)
    input_labels = ['Text']
    output_labels = ['Sentiment']
    labels = ['negative', 'positive']
    data_set = loadEmotions()

    training_set, validation_set = utils.split_in_two(data_set)

    training_input, training_output = training_set.get_trait_values(input_labels[0]), training_set.get_trait_values(
        output_labels[0])

    validation_input, validation_output = validation_set.get_trait_values(
        input_labels[0]), validation_set.get_trait_values(
        output_labels[0])

    myKNN = MyHybrid.MyHybrid(MyKMeans.bagDistance, 2)
    myKNN.train(training_input, training_output, epochs=20)

    predicted_output = [myKNN.predict(my_input) for my_input in validation_input]

    acc, prec, recall, cm = evalMultiClass(validation_output, np.array(predicted_output),
                                           labels)
    print('acc: ', acc)
    print('precision: ', prec)
    print('recall: ', recall)
    plotConfusionMatrix(cm, labels)

elif value == 5:
    random.seed(101)
    input_labels = ['Text']
    output_labels = ['Sentiment']
    labels = ['negative', 'positive']
    data_set = loadEmotions3()

    training_set, validation_set = utils.split_in_two(data_set)

    training_input, training_output = training_set.get_trait_values(input_labels[0]), training_set.get_trait_values(
        output_labels[0])

    validation_input, validation_output = validation_set.get_trait_values(
        input_labels[0]), validation_set.get_trait_values(
        output_labels[0])

    myKNN = MyHybrid.MyHybrid(MyKMeans.bagDistance, 2)
    myKNN.train(training_input, training_output, epochs=10)

    predicted_output = [myKNN.predict(my_input) for my_input in validation_input]

    acc, prec, recall, cm = evalMultiClass(validation_output, np.array(predicted_output),
                                           labels)
    print('acc: ', acc)
    print('precision: ', prec)
    print('recall: ', recall)
    plotConfusionMatrix(cm, labels)
