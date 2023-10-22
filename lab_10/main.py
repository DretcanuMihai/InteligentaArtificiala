import numpy

from input_output import *

from ANN import *

value = 4

if value == 1:
    input_labels = ['sepal length', 'sepal width', 'petal length', 'petal width']
    output_labels = ['verdict']
    data_set = load_iris_data()
    training_set, validation_set = utils.split_in_two(data_set)
    training_input, training_output = utils.extract_input_output(training_set, input_labels, output_labels)
    training_input = utils.transform_samples(training_input)
    training_output = utils.transform_input_labels(training_output[0], 3)
    validation_input, validation_output = utils.extract_input_output(validation_set, input_labels, output_labels)
    validation_input = utils.transform_samples(validation_input)
    validation_copy = validation_output[0]
    validation_output = utils.transform_input_labels(validation_output[0], 3)
    my_ann = ANN(hidden_layers_sizes=[3, 3], learning_rate=0.01)
    my_ann.fit(training_input, training_output)

    predicted_output = [my_ann.predict_label(my_input) for my_input in validation_input]

    acc, prec, recall, cm = evalMultiClass(np.array(validation_copy), np.array(predicted_output),
                                           ['virginica', 'versicolor', 'setosa'])
    print('acc: ', acc)
    print('precision: ', prec)
    print('recall: ', recall)
    plotConfusionMatrix(cm, ['virginica', 'versicolor', 'setosa'])

elif value == 2:
    input_labels = [str(num) for num in range(64)]
    output_labels = ['verdict']
    data_set = load_my_numbers()
    training_set, validation_set = utils.split_in_two(data_set)
    training_input, training_output = utils.extract_input_output(training_set, input_labels, output_labels)
    training_input = utils.transform_samples(training_input)
    training_output = utils.transform_input_labels(training_output[0], 10)
    validation_input, validation_output = utils.extract_input_output(validation_set, input_labels, output_labels)
    validation_input = utils.transform_samples(validation_input)
    validation_copy = validation_output[0]
    validation_output = utils.transform_input_labels(validation_output[0], 10)
    my_ann = ANN(hidden_layers_sizes=[5], no_iter=50, learning_rate=0.001)
    my_ann.fit(training_input, training_output)

    predicted_output = [my_ann.predict_label(my_input) for my_input in validation_input]

    acc, prec, recall, cm = evalMultiClass(np.array(validation_copy), np.array(predicted_output),
                                           [str(num) for num in range(10)])
    print('acc: ', acc)
    print('precision: ', prec)
    print('recall: ', recall)
    plotConfusionMatrix(cm, [str(num) for num in range(10)])

elif value == 3:
    input_labels = [str(num) for num in range(3 * 32 * 32)]
    output_labels = ['verdict']
    data_set = load_my_sepia()
    training_set, validation_set = utils.split_in_two(data_set)
    training_input, training_output = utils.extract_input_output(training_set, input_labels, output_labels)
    training_input = utils.transform_samples(training_input)
    training_output = utils.transform_input_labels(training_output[0], 2)
    validation_input, validation_output = utils.extract_input_output(validation_set, input_labels, output_labels)
    validation_input = utils.transform_samples(validation_input)
    validation_copy = validation_output[0]
    validation_output = utils.transform_input_labels(validation_output[0], 2)
    my_ann = ANN(hidden_layers_sizes=[10], no_iter=10, learning_rate=0.01)
    my_ann.fit(training_input, training_output)

    predicted_output = [my_ann.predict_label(my_input) for my_input in validation_input]

    acc, prec, recall, cm = evalMultiClass(np.array(validation_copy), np.array(predicted_output),
                                           ["sepia", "color"])
    print('acc: ', acc)
    print('precision: ', prec)
    print('recall: ', recall)
    plotConfusionMatrix(cm, ["sepia", "color"])

elif value == 4:
    import tensorflow as tf

    from keras import layers, models

    inputs, outputs = load_my_sepia2()

    training_data, validation_data = utils.split_in_two_2([inputs, outputs])

    training_input, training_output = numpy.array(training_data[0]), numpy.array(training_data[1])
    validation_input, validation_output = numpy.array(validation_data[0]), numpy.array(validation_data[1])

    model = models.Sequential([
        layers.Conv2D(16, 3, activation='relu', input_shape=(32, 32, 3)),
        layers.MaxPooling2D(),
        layers.Flatten(),
        layers.Dense(256, activation='relu'),
        layers.Dense(2)
    ])
    model.compile(optimizer='adam',
                  loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                  metrics=['accuracy'])

    model.fit(training_input, training_output, epochs=20,
              validation_data=(validation_input, validation_output))

    predicted_output = model.predict(validation_input)

    predicted_output = [tf.nn.softmax(my_output) for my_output in predicted_output]
    predicted_output = [np.argmax(my_output) for my_output in predicted_output]

    acc, prec, recall, cm = evalMultiClass(validation_output, np.array(predicted_output),
                                           ['color', 'sepia'])
    print('acc: ', acc)
    print('precision: ', prec)
    print('recall: ', recall)
    plotConfusionMatrix(cm, ['color', 'sepia'])
