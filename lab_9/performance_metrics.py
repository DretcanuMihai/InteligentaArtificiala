import math


def MAE(predicted_outputs, correct_outputs):
    """
    computes the MAE of a single target regression
    :param predicted_outputs: the predicted outputs
    :param correct_outputs: the correct outputs
    :return: said error
    """
    my_sum = 0
    for predicted, correct in zip(predicted_outputs, correct_outputs):
        val = abs(predicted - correct)
        my_sum += val
    my_sum /= len(predicted_outputs)
    return my_sum


def MSE(predicted_outputs, correct_outputs):
    """
    computes the MSE of a single target regression
    :param predicted_outputs: the predicted outputs
    :param correct_outputs: the correct outputs
    :return: said error
    """
    my_sum = 0
    for predicted, correct in zip(predicted_outputs, correct_outputs):
        val = (predicted - correct)
        val *= val
        my_sum += val
    my_sum /= len(predicted_outputs)
    return my_sum


def RMSE(predicted_outputs, correct_outputs):
    """
    computes the RMSE of a single target regression
    :param predicted_outputs: the predicted outputs
    :param correct_outputs: the correct outputs
    :return: said error
    """
    return MSE(predicted_outputs, correct_outputs) ** (1 / 2)


def regression_multi_target_error(predicted_outputs_list, correct_outputs_list, error_function):
    """
    computes the error of a multi target regression problem by just adding up the error of each target
    :param predicted_outputs_list: the predicted outputs
    :param correct_outputs_list: the correct outputs
    :param error_function: the error function with which the computing is done
    the function receives a target
    :return: said error
    """
    error = 0
    for i in range(len(predicted_outputs_list)):
        predicted_output = predicted_outputs_list[i]
        correct_outputs = correct_outputs_list[i]
        error += error_function(predicted_output, correct_outputs)
    return error / len(predicted_outputs_list)


def transform_softmax(values_list):
    """
    transforms all predicted inputs by using softmax function
    :param values_list: said targets
    :return: the transformed targets
    """
    new_values_list = []
    for value in values_list:
        new_values_list.append(math.exp(value))
    total_v = sum(new_values_list)
    for i in range(len(new_values_list)):
        new_values_list[i] /= total_v
    return new_values_list


def transform_sigmoid(values_list):
    """
    transforms all predicted inputs by using sigmoid function
    :param values_list: said targets
    :return: the transformed targets
    """
    new_values_list = []
    for value in values_list:
        new_values_list.append(1 / (1 + math.exp((-1) * value)))
    return new_values_list


def logarithmic_loss(predicted_outputs, correct_outputs):
    """
    computes the logarithmic loss of a prediction
    :param predicted_outputs: the predicted outputs
    :param correct_outputs: the correct outputs
    :return: said loss
    """
    loss = 0
    for predicteds, corrects in zip(predicted_outputs, correct_outputs):
        val = 0
        for predicted, correct in zip(predicteds, corrects):
            val += correct * math.log(predicted)
        loss += val
    return loss * (-1)


def hinge_loss(predicted_outputs, correct_outputs):
    """
    computes the hinge loss of a prediction
    :param predicted_outputs: the predicted outputs
    :param correct_outputs: the correct outputs
    :return: said loss
    """
    loss = 0
    for predicteds, corrects in zip(predicted_outputs, correct_outputs):
        val = 0
        for predicted, correct in zip(predicteds, corrects):
            predicted = math.log(predicted / (1 - predicted))
            val += max([0, 1 - (correct * 2 - 1) * predicted])
        loss += val
    return loss


def compute_confusion_matrix(predicted_outputs, correct_outputs, monitored_label):
    """
    computes the TP,FP,TN,FN of a classification prediction (confusion matrix)
    :param predicted_outputs: the predicted outputs
    :param correct_outputs: the correct outputs
    :param monitored_label: the label that's monitored
    :return: a list of [TP,FP,TN,FN]
    """
    TP = 0
    FP = 0
    FN = 0
    TN = 0
    for predicted, correct in zip(predicted_outputs, correct_outputs):
        if predicted == correct:
            if predicted == monitored_label:
                TP += 1
            else:
                TN += 1
        else:
            if predicted == monitored_label:
                FP += 1
            else:
                FN += 1
    return [TP, FP, FN, TN]


def ot_accuracy(predicted_outputs, correct_outputs):
    """
    computes the accuracy of a classification prediction
    :param predicted_outputs: the predicted outputs
    :param correct_outputs: the correct outputs
    :return: said accuracy
    """
    correct = 0
    for i in range(len(predicted_outputs)):
        if predicted_outputs[i] == correct_outputs[i]:
            correct += 1
    return correct / len(predicted_outputs)


def accuracy(predicted_outputs, correct_outputs, monitored_label):
    """
    computes the accuracy of a classification prediction
    :param predicted_outputs: the predicted outputs
    :param correct_outputs: the correct outputs
    :param monitored_label: the label that's monitored
    :return: said accuracy
    """
    TP, FP, FN, TN = compute_confusion_matrix(predicted_outputs, correct_outputs, monitored_label)
    return (TP + TN) / (TP + FP + FN + TN)


def precision(predicted_outputs, correct_outputs, monitored_label):
    """
    computes the precision of a classification prediction
    :param predicted_outputs: the predicted outputs
    :param correct_outputs: the correct outputs
    :param monitored_label: the label that's monitored
    :return: said precision
    """
    TP, FP, FN, TN = compute_confusion_matrix(predicted_outputs, correct_outputs, monitored_label)
    return TP / (TP + FP)


def recall(predicted_outputs, correct_outputs, monitored_label):
    """
    computes the recall of a classification prediction
    :param predicted_outputs: the predicted outputs
    :param correct_outputs: the correct outputs
    :param monitored_label: the label that's monitored
    :return: said recall
    """
    TP, FP, FN, TN = compute_confusion_matrix(predicted_outputs, correct_outputs, monitored_label)
    return TP / (TP + FN)


def F1(predicted_outputs, correct_outputs, monitored_label):
    """
    computes the recall of a classification prediction
    :param predicted_outputs: the predicted outputs
    :param correct_outputs: the correct outputs
    :param monitored_label: the label that's monitored
    :return: said recall
    """
    P = precision(predicted_outputs, correct_outputs, monitored_label)
    R = recall(predicted_outputs, correct_outputs, monitored_label)
    return 2 * P * R / (P + R)
