from sklearn import linear_model

import MyMultiLabelLinearRegressor
import MySimpleLabelLinearRegressor
import performance_metrics
import utils


def solve_logistics_regression_libraries(batches, input_names, output_name, epochs=1000, learning_rate=0.01):
    """
    returns a list of regressors for each output of a dataset with some inputs
    :param data_set:said data set
    :param input_names:the name of the input traits
    :param output_name:the name of the output traits
    :return:said list
    """
    data_set = utils.unite_batches(batches)
    input_traits_values, output_traits_values = utils.extract_input_output(data_set, input_names, [output_name])
    input_data = []
    for _ in input_traits_values[0]:
        input_data.append([])
    for input_trait_values in input_traits_values:
        for i in range(len(input_trait_values)):
            input_data[i].append(input_trait_values[i])
    output_data = output_traits_values[0]
    regressor = linear_model.LogisticRegression()
    regressor.fit(input_data, output_data)
    regressors = []
    for i in range(len(regressor.intercept_)):
        coefficients = list(regressor.coef_[i])
        coefficients.insert(0, regressor.intercept_[i])
        regressors.append(MySimpleLabelLinearRegressor.MySimpleLabelLinearRegressor(coefficients))
    return MyMultiLabelLinearRegressor.MyMultiLabelLinearRegressor(regressors)


def solve_logistics_regression_mine(batches, input_names, output_name, epochs=1000, learning_rate=0.3):
    """
    returns a list of regressors for each output of a dataset with some inputs
    :param batches:said data set batches
    :param input_names:the name of the input traits
    :param output_name:the name of the output traits
    :return:said list
    """
    current_coefs = []
    for _ in range(len(set(batches[0].get_trait_values(output_name)))):
        current_coefs.append([0.0 for _ in range(len(input_names) + 1)])
    for _ in range(epochs):
        for data_set in batches:
            input_traits_values, output_traits_values = utils.extract_input_output(data_set, input_names, [output_name])
            output_traits_values = output_traits_values[0]
            set_len = len(set(output_traits_values))
            new_output = []
            for k in range(set_len):
                aux = []
                for elem in output_traits_values:
                    if elem == k:
                        aux.append(1)
                    else:
                        aux.append(0)
                new_output.append(aux)
            output_traits_values = new_output
            input_traits_values.insert(0, [1 for _ in range(len(input_traits_values[0]))])
            dj_aux = []
            for row in current_coefs:
                dj_aux.append([0 for _ in row])

            for sample_index in range(len(input_traits_values[0])):  # iterates samples
                for output_trait_index in range(len(output_traits_values)):  # iterates output traits
                    current_value = 0
                    for input_trait_index in range(len(input_traits_values)):
                        current_value += current_coefs[output_trait_index][input_trait_index] * \
                                         input_traits_values[input_trait_index][
                                             sample_index]
                    current_error = performance_metrics.transform_sigmoid([current_value])[0] - \
                                    output_traits_values[output_trait_index][sample_index]
                    for input_trait_index in range(len(input_traits_values)):
                        dj_aux[output_trait_index][input_trait_index] += current_error * \
                                                                         input_traits_values[input_trait_index][
                                                                             sample_index]
            my_length = len(input_traits_values)
            current_coefs = [
                [current_coefs[i][j] - learning_rate * dj_aux[i][j] for j in range(len(current_coefs[i]))]
                for
                i in range(len(current_coefs))]

    regressors = []
    for coef in current_coefs:
        regressors.append(MySimpleLabelLinearRegressor.MySimpleLabelLinearRegressor(coef))
    return MyMultiLabelLinearRegressor.MyMultiLabelLinearRegressor(regressors)


def solve_logistics_regresion_mine(batches, input_names, output_name, epochs=100, learning_rate=0.01):
    """
    returns a list of regressors for each output of a dataset with some inputs
    :param batches:said data set batches
    :param input_names:the name of the input traits
    :param output_name:the name of the output traits
    :return:said list
    """
    batches = [utils.unite_batches(batches)]
    current_coefs = []
    for _ in range(len(output_name)):
        current_coefs.append([0.0 for _ in range(len(input_names) + 1)])
    for _ in range(epochs):
        for data_set in batches:
            input_traits_values, output_traits_values = utils.extract_input_output(data_set, input_names, [output_name])
            output_traits_values = output_traits_values[0]
            set_len = len(set(output_traits_values))
            new_output = []
            for k in range(set_len):
                aux = []
                for elem in output_traits_values:
                    if elem == k:
                        aux.append(1)
                    else:
                        aux.append(0)
                new_output.append(aux)
            output_traits_values = new_output
            input_traits_values.insert(0, [1 for _ in range(len(input_traits_values[0]))])
            dj_aux = []
            for row in current_coefs:
                dj_aux.append([0 for _ in row])

            for sample_index in range(len(input_traits_values[0])):  # iterates samples
                for output_trait_index in range(len(output_traits_values)):  # iterates output traits
                    current_value = 0
                    for input_trait_index in range(len(input_traits_values)):
                        current_value += current_coefs[output_trait_index][input_trait_index] * \
                                         input_traits_values[input_trait_index][
                                             sample_index]
                    current_error = performance_metrics.transform_sigmoid([current_value])[0] - \
                                    output_traits_values[output_trait_index][sample_index]
                    for input_trait_index in range(len(input_traits_values)):
                        dj_aux[output_trait_index][input_trait_index] += current_error * \
                                                                         input_traits_values[input_trait_index][
                                                                             sample_index]
            my_length = len(input_traits_values)
            current_coefs = [
                [current_coefs[i][j] - learning_rate * dj_aux[i][j] / my_length for j in range(len(current_coefs[i]))]
                for
                i in range(len(current_coefs))]

    regressors = []
    for coef in current_coefs:
        regressors.append(MySimpleLabelLinearRegressor.MySimpleLabelLinearRegressor(coef))
    return MyMultiLabelLinearRegressor.MyMultiLabelLinearRegressor(regressors)
