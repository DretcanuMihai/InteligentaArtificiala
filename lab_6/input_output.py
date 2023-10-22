import performance_metrics as pm

"""
target = {'name' - name of target
          'predicted' - predicted outputs list
          'expected' - expected outputs list}
"""


def get_predicted_correct(data):
    """
    gets the predicted data and correct data from a data set resulted from pandas reading a csv file
    :param data: said data set
    :return: a list of targets
    """
    to_return = []
    for elem in data:
        if "Predicted" + elem in data:
            predicted_data = data["Predicted" + elem]
            correct_data = data[elem]
            to_return.append({'name': elem,
                              'predicted': [predicted for predicted in predicted_data],
                              'expected': [correct for correct in correct_data]})
    return to_return


def print_regression_errors(targets):
    """
    prints the errors of each target in a list of targets and the overall error
    :param targets: said list of targets
    the function receives a target
    :return: None
    """
    for error_function in [pm.MAE, pm.MSE, pm.RMSE]:
        print(error_function.__name__)
        for target in targets:
            print(target['name'] + ":")
            print(str(error_function(target)))
        print("Overall:")
        print(str(pm.regression_multi_target_error(targets, error_function)))


def print_classification_results(target, labels):
    """
    prints the classification results of a target for some labels
    :param target: said target
    :param labels: a list of wanted labels
    :return: None
    """
    for label in labels:
        print(str(label))
        for function in [pm.accuracy, pm.precision, pm.recall, pm.F1]:
            print(function.__name__)
            print(function(target, label))
