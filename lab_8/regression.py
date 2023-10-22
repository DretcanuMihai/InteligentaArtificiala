from sklearn import linear_model

import MyMatrix
import MyRegressor
import utils


def solve_linear_regression_libraries(data_set, input_names, output_names, epochs=1000, learning_rate=0.01):
    """
    returns a list of regressors for each output of a dataset with some inputs
    :param data_set:said data set
    :param input_names:the name of the input traits
    :param output_names:the name of the output traits
    :return:said list
    """
    input_traits_values, output_traits_values = utils.extract_input_output(data_set, input_names, output_names)
    input_data = []
    for _ in input_traits_values[0]:
        input_data.append([])
    for input_trait_values in input_traits_values:
        for i in range(len(input_trait_values)):
            input_data[i].append(input_trait_values[i])
    regressors = []
    for output_trait_values in output_traits_values:
        regressor = linear_model.SGDRegressor(alpha=learning_rate, max_iter=epochs)
        regressor.fit(input_data, output_trait_values)
        coefficients = [regressor.intercept_[0]]
        for c in regressor.coef_:
            coefficients.append(c)
        regressor = MyRegressor.MyRegressor(coefficients)
        regressors.append(regressor)
    return regressors


def solve_linear_regression_mine_dependent(data_set, input_names, output_names, epochs=1000, learning_rate=0.01):
    """
    returns a list of regressors for each output of a dataset with some inputs
    :param data_set:said data set
    :param input_names:the name of the input traits
    :param output_names:the name of the output traits
    :return:said list
    """
    regressors = []
    for output_name in output_names:
        regressors.append(solve_linear_regression_mine(data_set, input_names, [output_name], epochs, learning_rate)[0])
        input_names.append(output_name)
    return regressors


def solve_linear_regression_mine(data_set, input_names, output_names, epochs=1000, learning_rate=0.01):
    """
    returns a list of regressors for each output of a dataset with some inputs
    :param data_set:said data set
    :param input_names:the name of the input traits
    :param output_names:the name of the output traits
    :return:said list
    """
    input_traits_values, output_traits_values = utils.extract_input_output(data_set, input_names, output_names)
    input_traits_values.insert(0, [1 for _ in range(len(input_traits_values[0]))])
    current_coefs = []
    for _ in range(len(output_names)):
        current_coefs.append([0.0 for _ in range(len(input_names) + 1)])

    for _ in range(epochs):
        dj_aux = []
        for row in current_coefs:
            dj_aux.append([0 for _ in row])

        for sample_index in range(len(input_traits_values[0])):  # iterates samples
            for output_trait_index in range(len(output_names)):  # iterates output traits
                current_value = 0
                for input_trait_index in range(len(input_traits_values)):
                    current_value += current_coefs[output_trait_index][input_trait_index] * \
                                     input_traits_values[input_trait_index][
                                         sample_index]
                current_error = current_value - output_traits_values[output_trait_index][sample_index]
                for input_trait_index in range(len(input_traits_values)):
                    dj_aux[output_trait_index][input_trait_index] += current_error * \
                                                                     input_traits_values[input_trait_index][
                                                                         sample_index]
        my_length = len(input_traits_values)
        current_coefs = [[current_coefs[i][j] - learning_rate * dj_aux[i][j]/my_length for j in range(len(current_coefs[i]))] for
                         i in range(len(current_coefs))]

    regressors = []
    for coef in current_coefs:
        regressors.append(MyRegressor.MyRegressor(coef))
    return regressors


def solve_linear_regression_mine2(data_set, input_names, output_names, epochs=1000, learning_rate=0.01):
    """
    returns a list of regressors for each output of a dataset with some inputs
    :param data_set:said data set
    :param input_names:the name of the input traits
    :param output_names:the name of the output traits
    :return:said list
    """
    input_traits_values, output_traits_values = utils.extract_input_output(data_set, input_names, output_names)
    inputs = [[1 for _ in range(len(input_traits_values[0]))]]
    outputs = []
    for input_trait_values in input_traits_values:
        inputs.append(input_trait_values)
    for output_trait_values in output_traits_values:
        outputs.append(output_trait_values)

    X = MyMatrix.MyMatrix(inputs).get_transposed()
    Y = MyMatrix.MyMatrix(outputs).get_transposed()

    # n = nr. samples
    # m = len(inputs)
    # d = len(outputs)
    current_coefs = []
    for _ in range(len(output_names)):
        current_coefs.append([0.0 for _ in range(len(input_names) + 1)])
    current_coefs = MyMatrix.MyMatrix(current_coefs).get_transposed()

    for _ in range(epochs):
        yaux = X.multiply_with_matrix(current_coefs)  # computes the values of the samples with current coefficients
        errors = yaux.add(Y.multiply_with_scalar(-1)).get_as_list()  # computes the error of each given output
        xkes = X.get_as_list()
        coefs = current_coefs.get_as_list()
        for i in range(len(coefs)):  # iterez trasaturile de input
            for j in range(len(coefs[0])):  # iterez coeficientii unei trasaturi de input
                val = coefs[i][j]
                for k in range(len(xkes)):  # iterez valorile corespunzatoare acelui input
                    val -= learning_rate * errors[k][j] * xkes[k][i]
                coefs[i][j] = val

    regressors = []
    for coef in current_coefs.get_transposed().get_as_list():
        regressors.append(MyRegressor.MyRegressor(coef))
    return regressors


# nu-mi place nu-i ok nu ar trebui sa existe e gresit am o cadere nervoasa
def solve_linear_regression_mine3(data_set, input_names, output_names, epochs=1000, learning_rate=0.01):
    """
    returns a list of regressors for each output of a dataset with some inputs
    :param data_set:said data set
    :param input_names:the name of the input traits
    :param output_names:the name of the output traits
    :return:said list
    """
    input_traits_values, output_traits_values = utils.extract_input_output(data_set, input_names, output_names)
    input_traits_values.insert(0, [1 for _ in range(len(input_traits_values[0]))])
    current_coefs = []
    for _ in range(len(output_names)):
        current_coefs.append([0.0 for _ in range(len(input_names) + 1)])

    for _ in range(epochs):
        errors = [0.0 for _ in range(len(output_traits_values))]
        all_values = [0.0 for _ in range(len(input_traits_values))]
        for sample_index in range(len(input_traits_values[0])):  # iterates samples
            for output_trait_index in range(len(output_names)):  # iterates output traits
                current_value = 0
                for input_trait_index in range(len(input_traits_values)):
                    current_value += current_coefs[output_trait_index][input_trait_index] * \
                                     input_traits_values[input_trait_index][
                                         sample_index]
                    all_values[input_trait_index] += input_traits_values[input_trait_index][sample_index]
                current_error = current_value - output_traits_values[output_trait_index][sample_index]
                errors[output_trait_index] += current_error

        new_coefs = []
        for output_index in range(len(output_names)):
            row = []
            for input_index in range(len(input_traits_values)):
                row.append(current_coefs[output_index][input_index]
                           - (errors[output_index] / len(input_traits_values[0])) * learning_rate * all_values[
                               input_index])
            new_coefs.append(row)
        current_coefs = new_coefs

    regressors = []
    for coef in current_coefs:
        regressors.append(MyRegressor.MyRegressor(coef))
    return regressors
