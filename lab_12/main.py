import numpy

import utils
import cv2

from input_output import *

value = 6
emotions = ['angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral']
emotion_to_int = {'angry': 0, 'disgust': 1, 'fear': 2, 'happy': 3, 'sad': 4, 'surprise': 5, 'neutral': 6, None: 6}

if value == 1:
    import tensorflow as tf

    from keras import layers, models

    input_images, outputs = load_my_emojis()

    training_data, validation_data = utils.split_in_two_2([input_images, outputs])

    training_input, training_output = numpy.array(training_data[0]), numpy.array(training_data[1])
    validation_input, validation_output = numpy.array(validation_data[0]), numpy.array(validation_data[1])

    model = models.Sequential([
        layers.Conv2D(16, 3, activation='relu', input_shape=(16, 16, 3)),
        layers.MaxPooling2D(),
        layers.Conv2D(32, 3, activation='relu'),
        layers.MaxPooling2D(),
        layers.Flatten(),
        layers.Dense(256, activation='relu'),
        layers.Dense(2)
    ])
    model.compile(optimizer='adam',
                  loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                  metrics=['accuracy'])

    model.fit(training_input, training_output, epochs=50,
              validation_data=(validation_input, validation_output))

    predicted_output = model.predict(validation_input)

    predicted_output = [tf.nn.softmax(my_output) for my_output in predicted_output]
    predicted_output = [np.argmax(my_output) for my_output in predicted_output]

    acc, prec, recall, cm = evalMultiClass(validation_output, np.array(predicted_output),
                                           ['happy', 'sad'])
    print('acc: ', acc)
    print('precision: ', prec)
    print('recall: ', recall)
    plotConfusionMatrix(cm, ['happy', 'sad'])

elif value == 2:
    from fer import FER

    detector = FER(mtcnn=True)

    # load_my_fer(no_samples=1000)
    input_images, outputs = load_my_fer2(no_samples=1000)

    predicted_output = []

    for img_path in input_images:
        myimg = cv2.imread(img_path)
        emotion, score = detector.top_emotion(myimg)
        predicted_output.append(emotion_to_int[emotion])

    acc, prec, recall, cm = evalMultiClass(np.array(outputs), np.array(predicted_output),
                                           emotions)
    print('acc: ', acc)
    print('precision: ', prec)
    print('recall: ', recall)
    plotConfusionMatrix(cm, emotions)

elif value == 3:
    import tensorflow as tf

    from keras import layers, models

    input_images, outputs = load_my_fer3(no_samples=2000)

    training_data, validation_data = utils.split_in_two_2([input_images, outputs])

    training_input, training_output = numpy.array(training_data[0]), numpy.array(training_data[1])
    validation_input, validation_output = numpy.array(validation_data[0]), numpy.array(validation_data[1])

    model = models.Sequential([
        layers.Conv2D(16, 3, activation='relu', input_shape=(48, 48, 3)),
        layers.MaxPooling2D(),
        layers.Conv2D(32, 3, activation='relu'),
        layers.MaxPooling2D(),
        layers.Conv2D(64, 3, activation='relu'),
        layers.MaxPooling2D(),
        layers.Flatten(),
        layers.Dense(256, activation='relu'),
        layers.Dense(len(emotions))
    ])
    model.compile(optimizer='adam',
                  loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                  metrics=['accuracy'])

    model.fit(training_input, training_output, epochs=50,
              validation_data=(validation_input, validation_output))

    predicted_output = model.predict(validation_input)

    predicted_output = [tf.nn.softmax(my_output) for my_output in predicted_output]
    predicted_output = [np.argmax(my_output) for my_output in predicted_output]

    acc, prec, recall, cm = evalMultiClass(validation_output, np.array(predicted_output),
                                           emotions)
    print('acc: ', acc)
    print('precision: ', prec)
    print('recall: ', recall)
    plotConfusionMatrix(cm, emotions)

elif value == 4:
    import autokeras as ak
    import tensorflow as tf

    input_images, outputs = load_my_fer3(no_samples=50)

    training_data, validation_data = utils.split_in_two_2([input_images, outputs])

    training_input, training_output = numpy.array(training_data[0]), numpy.array(training_data[1])
    validation_input, validation_output = numpy.array(validation_data[0]), numpy.array(validation_data[1])

    model = ak.ImageClassifier()
    model.fit(training_input, training_output, epochs=10)

    predicted_output = model.predict(validation_input)

    predicted_output = [tf.nn.softmax(my_output) for my_output in predicted_output]
    predicted_output = [np.argmax(my_output) for my_output in predicted_output]

    acc, prec, recall, cm = evalMultiClass(validation_output, np.array(predicted_output),
                                           emotions)
    print('acc: ', acc)
    print('precision: ', prec)
    print('recall: ', recall)
    plotConfusionMatrix(cm, emotions)

elif value == 5:
    # tot n-am reusit sa repar eroarea aia asa ca am incercat alta varianta
    # tot nu merge, ma dau batut
    import tensorflow as tf
    from keras import models, layers
    import keras

    input_images, outputs = load_my_fer4(no_samples=50)

    training_data, validation_data = utils.split_in_two_2([input_images, outputs])

    training_input, training_output = numpy.array(training_data[0]), numpy.array(training_data[1])
    validation_input, validation_output = numpy.array(validation_data[0]), numpy.array(validation_data[1])

    model = models.Sequential([
        layers.Conv2D(16, 3, activation='relu', input_shape=(48, 48, 3)),
        layers.MaxPooling2D(),
        layers.Conv2D(32, 3, activation='relu'),
        layers.MaxPooling2D(),
        layers.Flatten(),
        layers.Dense(256, activation='relu'),
        layers.Dense(7,
                     kernel_initializer=tf.keras.initializers.GlorotUniform(seed=152),
                     activation=tf.keras.activations.sigmoid)(input_images)
    ])
    print(model.input_shape)
    print(model.output_shape)

    """
    model = models.Sequential([
        layers.Conv2D(16, 3, activation='relu', input_shape=(48, 48, 3)),
        layers.MaxPooling2D(),
        layers.Conv2D(32, 3, activation='relu'),
        layers.MaxPooling2D(),
        layers.Conv2D(64, 3, activation='relu'),
        layers.MaxPooling2D(),
        layers.Flatten(),
        layers.Dense(7, kernel_initializer=tf.keras.initializers.GlorotUniform(seed=412),
                     activation=tf.keras.activations.sigmoid)]
    )
    """
    model.compile(optimizer='adam',
                  loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                  metrics=[tf.keras.metrics.SparseCategoricalAccuracy()])


    def transform(my_output):
        """
        transforms output in good form
        :param my_output: said output
        :return: said good form
        """
        my_output = np.array(my_output)
        return my_output


    model.fit(training_input, transform(training_output), epochs=50,
              validation_data=(validation_input, transform(validation_output)))

    predicted_output = model.predict(validation_input)
    predicted_output = [[tf.nn.sigmoid(outp) for outp in my_output] for my_output in predicted_output]

elif value == 6:
    import tensorflow as tf

    from keras import layers, models

    input_images, outputs = load_my_fer5(no_samples=2000)

    training_data, validation_data = utils.split_in_two_2([input_images, outputs])

    training_input, training_output = numpy.array(training_data[0]), numpy.array(training_data[1])
    validation_input, validation_output = numpy.array(validation_data[0]), numpy.array(validation_data[1])

    model = models.Sequential([
        layers.Conv2D(16, 3, activation='relu', input_shape=(48, 48, 3)),
        layers.MaxPooling2D(),
        layers.Conv2D(32, 3, activation='relu'),
        layers.MaxPooling2D(),
        layers.Conv2D(64, 3, activation='relu'),
        layers.MaxPooling2D(),
        layers.Flatten(),
        layers.Dense(256, activation='relu'),
        layers.Dense(len(emotions))
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
                                           emotions)
    print('acc: ', acc)
    print('precision: ', prec)
    print('recall: ', recall)
    plotConfusionMatrix(cm, emotions)
