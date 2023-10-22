import random

import input_output as io
import performance_metrics
import regression
import utils

random.seed(461)
value = 3
if value == 1:
    traits = ['mean radius', 'mean texture', 'verdict']


    def get_acc(my_data_set, my_lregressor):
        feature1 = my_data_set.get_trait_values(traits[0])
        feature2 = my_data_set.get_trait_values(traits[1])
        correct_outputs = my_data_set.get_trait_values(traits[2])
        computed_outputs = [my_lregressor.predict_label([f1, f2]) for (f1, f2) in zip(feature1, feature2)]
        return performance_metrics.ot_accuracy(computed_outputs, correct_outputs)


    def get_error(my_data_set, my_lregressor):
        feature1 = my_data_set.get_trait_values(traits[0])
        feature2 = my_data_set.get_trait_values(traits[1])
        correct_outputs = my_data_set.get_trait_values(traits[2])
        aux = []
        for output in correct_outputs:
            aux_list = []
            for my_k in range(2):
                if my_k == output:
                    aux_list.append(1)
                else:
                    aux_list.append(0)
            aux.append(aux_list)
        correct_outputs = aux
        computed_outputs = [my_lregressor.predict_list([f1, f2]) for (f1, f2) in zip(feature1, feature2)]
        return performance_metrics.logarithmic_loss(computed_outputs, correct_outputs)


    def get_error2(my_data_set, my_lregressor):
        feature1 = my_data_set.get_trait_values(traits[0])
        feature2 = my_data_set.get_trait_values(traits[1])
        correct_outputs = my_data_set.get_trait_values(traits[2])
        aux = []
        for output in correct_outputs:
            aux_list = []
            for my_k in range(2):
                if my_k == output:
                    aux_list.append(1)
                else:
                    aux_list.append(0)
            aux.append(aux_list)
        correct_outputs = aux
        computed_outputs = [my_lregressor.predict_list([f1, f2]) for (f1, f2) in zip(feature1, feature2)]
        return performance_metrics.hinge_loss(computed_outputs, correct_outputs)


    data_set = io.load_cancer_data()
    io.plot_labels_2_traits(data_set, traits[0], traits[1], traits[2], {0: 'malignant', 1: 'benign'})
    for trait in traits:
        io.plot_histogram(data_set, trait)

    batches = utils.get_batches(data_set)
    best_regressor = None
    best_validation = None
    best_error = None
    for i in range(len(batches)):
        validation_batch = batches[i]
        training_batches = []
        for k in range(len(batches)):
            if k != i:
                training_batches.append(batches[k])
        my_regressor = regression.solve_logistics_regression_libraries(training_batches, [traits[0], traits[1]],
                                                                       traits[2])

        error = get_error2(validation_batch, my_regressor)
        if best_regressor is None or error < best_error:
            best_regressor = my_regressor
            best_validation = validation_batch
            best_error = error
    io.plot_predicitions_2_traits(best_validation, traits[0], traits[1], traits[2], {0: 'malignant', 1: 'benign'},
                                  best_regressor)
    print("accuracy:")
    print(get_acc(best_validation, best_regressor))
    print("error:")
    print(get_error2(best_validation, best_regressor))

if value == 2:
    traits = ['mean radius', 'mean texture', 'verdict']


    def get_acc(my_data_set, my_lregressor):
        feature1 = my_data_set.get_trait_values(traits[0])
        feature2 = my_data_set.get_trait_values(traits[1])
        correct_outputs = my_data_set.get_trait_values(traits[2])
        computed_outputs = [my_lregressor.predict_label([f1, f2]) for (f1, f2) in zip(feature1, feature2)]
        return performance_metrics.ot_accuracy(computed_outputs, correct_outputs)


    def get_error(my_data_set, my_lregressor):
        feature1 = my_data_set.get_trait_values(traits[0])
        feature2 = my_data_set.get_trait_values(traits[1])
        correct_outputs = my_data_set.get_trait_values(traits[2])
        aux = []
        for output in correct_outputs:
            aux_list = []
            for my_k in range(2):
                if my_k == output:
                    aux_list.append(1)
                else:
                    aux_list.append(0)
            aux.append(aux_list)
        correct_outputs = aux
        computed_outputs = [my_lregressor.predict_list([f1, f2]) for (f1, f2) in zip(feature1, feature2)]
        return performance_metrics.logarithmic_loss(computed_outputs, correct_outputs)


    def get_error2(my_data_set, my_lregressor):
        feature1 = my_data_set.get_trait_values(traits[0])
        feature2 = my_data_set.get_trait_values(traits[1])
        correct_outputs = my_data_set.get_trait_values(traits[2])
        aux = []
        for output in correct_outputs:
            aux_list = []
            for my_k in range(2):
                if my_k == output:
                    aux_list.append(1)
                else:
                    aux_list.append(0)
            aux.append(aux_list)
        correct_outputs = aux
        computed_outputs = [my_lregressor.predict_list([f1, f2]) for (f1, f2) in zip(feature1, feature2)]
        return performance_metrics.hinge_loss(computed_outputs, correct_outputs)


    data_set = io.load_cancer_data()
    for trait in traits:
        io.plot_histogram(data_set, trait)

    batches = utils.get_batches(data_set)
    best_regressor = None
    best_validation = None
    best_error = None
    for i in range(len(batches)):
        validation_batch = batches[i]
        training_batches = []
        for k in range(len(batches)):
            if k != i:
                training_batches.append(batches[k])
        my_regressor = regression.solve_logistics_regression_libraries(training_batches, [traits[0], traits[1]],
                                                                       traits[2])

        regressors = my_regressor.get_regressors()
        regressors[0].set_threshold(0.9)
        regressors[1].set_threshold(0.9)

        error = get_error2(validation_batch, my_regressor)
        if best_regressor is None or error < best_error:
            best_regressor = my_regressor
            best_validation = validation_batch
            best_error = error

    print("accuracy:")
    print(get_acc(best_validation, best_regressor))
    print("error:")
    print(get_error2(best_validation, best_regressor))

if value == 3:
    traits = ['sepal length', 'sepal width', 'petal length', 'petal width', 'verdict']


    def get_acc(my_data_set, my_lregressor):
        feature1 = my_data_set.get_trait_values(traits[0])
        feature2 = my_data_set.get_trait_values(traits[1])
        feature3 = my_data_set.get_trait_values(traits[2])
        feature4 = my_data_set.get_trait_values(traits[3])
        correct_outputs = my_data_set.get_trait_values(traits[4])
        computed_outputs = [my_lregressor.predict_label([f1, f2, f3, f4]) for (f1, f2, f3, f4) in
                            zip(feature1, feature2, feature3, feature4)]
        return performance_metrics.ot_accuracy(computed_outputs, correct_outputs)


    def get_error(my_data_set, my_lregressor):
        feature1 = my_data_set.get_trait_values(traits[0])
        feature2 = my_data_set.get_trait_values(traits[1])
        feature3 = my_data_set.get_trait_values(traits[2])
        feature4 = my_data_set.get_trait_values(traits[3])
        correct_outputs = my_data_set.get_trait_values(traits[4])
        aux = []
        for output in correct_outputs:
            aux_list = []
            for my_k in range(3):
                if my_k == output:
                    aux_list.append(1)
                else:
                    aux_list.append(0)
            aux.append(aux_list)
        correct_outputs = aux
        computed_outputs = [my_lregressor.predict_list([f1, f2, f3, f4]) for (f1, f2, f3, f4) in
                            zip(feature1, feature2, feature3, feature4)]
        return performance_metrics.logarithmic_loss(computed_outputs, correct_outputs)


    def get_error2(my_data_set, my_lregressor):
        feature1 = my_data_set.get_trait_values(traits[0])
        feature2 = my_data_set.get_trait_values(traits[1])
        feature3 = my_data_set.get_trait_values(traits[2])
        feature4 = my_data_set.get_trait_values(traits[3])
        correct_outputs = my_data_set.get_trait_values(traits[4])
        aux = []
        for output in correct_outputs:
            aux_list = []
            for my_k in range(3):
                if my_k == output:
                    aux_list.append(1)
                else:
                    aux_list.append(0)
            aux.append(aux_list)
        correct_outputs = aux
        computed_outputs = [my_lregressor.predict_list([f1, f2, f3, f4]) for (f1, f2, f3, f4) in
                            zip(feature1, feature2, feature3, feature4)]
        return performance_metrics.hinge_loss(computed_outputs, correct_outputs)


    data_set = io.load_iris_data()
    # for trait in traits:
    #    io.plot_histogram(data_set, trait)

    batches = utils.get_batches(data_set)
    best_regressor = None
    best_validation = None
    best_error = None
    for i in range(len(batches)):
        validation_batch = batches[i]
        training_batches = []
        for k in range(len(batches)):
            if k != i:
                training_batches.append(batches[k])
        my_regressor = regression.solve_logistics_regression_mine(training_batches,
                                                                  [traits[0], traits[1], traits[2], traits[3]],
                                                                  traits[4])
        my_regressor.set_non_binary()
        regressors = my_regressor.get_regressors()
        regressors[0].set_threshold(0.66)
        regressors[1].set_threshold(0.5)

        error = get_error(validation_batch, my_regressor)
        # error = 1 - get_acc(validation_batch, my_regressor)
        if best_regressor is None or error < best_error:
            best_regressor = my_regressor
            best_validation = validation_batch
            best_error = error
    print("accuracy:")
    print(get_acc(best_validation, best_regressor))
    print("error:")
    print(get_error(best_validation, best_regressor))
