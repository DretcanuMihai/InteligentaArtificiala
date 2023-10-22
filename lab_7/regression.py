from sklearn import linear_model

import MyMatrix
import MyRegressor
import utils


def solve_linear_regression_libraries(data_set, input_names, output_names):
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
        regressor = linear_model.LinearRegression()
        regressor.fit(input_data, output_trait_values)
        coefficients = [regressor.intercept_]
        for c in regressor.coef_:
            coefficients.append(c)
        regressor = MyRegressor.MyRegressor(coefficients)
        regressors.append(regressor)
    return regressors


def solve_linear_regression_mine(data_set, input_names, output_names):
    """
    returns a list of regressors for each output of a dataset with some inputs
    :param data_set:said data set
    :param input_names:the name of the input traits
    :param output_names:the name of the output traits
    :return:said list
    """
    input_traits_values, output_traits_values = utils.extract_input_output(data_set, input_names, output_names)
    input_normalized = [[1 for _ in range(len(input_traits_values[0]))]]
    output_normalized = []
    for input_trait_values in input_traits_values:
        input_normalized.append(input_trait_values)
    for output_trait_values in output_traits_values:
        output_normalized.append(output_trait_values)
    """
    _X = np.matrix(input_normalized).transpose()
    _Y = np.matrix(output_normalized).transpose()
    _XT = _X.transpose()
    _XTX = _XT.dot(_X)
    _XTXinv = np.linalg.inv(_XTX)
    _XTXinvXT = _XTXinv.dot(_XT)
    _final = _XTXinvXT.dot(_Y)
    """
    X = MyMatrix.MyMatrix(input_normalized).get_transposed()
    Y = MyMatrix.MyMatrix(output_normalized).get_transposed()
    XT = X.get_transposed()
    XTX = XT.multiply_with_matrix(X)
    XTXinv = XTX.get_inverse()
    if XTXinv is None:
        return None
    XTXinvXT = XTXinv.multiply_with_matrix(XT)
    final = XTXinvXT.multiply_with_matrix(Y)
    final_T = final.get_transposed()
    result = final_T.get_as_list()
    regressors = []
    for coef in result:
        regressors.append(MyRegressor.MyRegressor(coef))
    return regressors
