"""
target = {'name' - name of target
          'predicted' - predicted outputs list
          'expected' - expected outputs list}
zipped_targets={'data':{'predicted':predicted outputs list
                       'expected':expected outputs list
                       }
               'names' - list of target names
               }
"""
import math


def MAE(target):
    """
    returns the MAE of a single-target prediction
    :param target: said target
    :return: said error
    """
    predicted_outputs = target['predicted']
    correct_outputs = target['expected']
    my_sum = 0
    for predicted, correct in zip(predicted_outputs, correct_outputs):
        val = abs(predicted - correct)
        my_sum += val
    my_sum /= len(predicted_outputs)
    return my_sum


def MSE(target):
    """
    returns the MSE of a single-target prediction
    :param target: said target
    :return: said error
    """
    predicted_outputs = target['predicted']
    correct_outputs = target['expected']
    my_sum = 0
    for predicted, correct in zip(predicted_outputs, correct_outputs):
        val = (predicted - correct)
        val *= val
        my_sum += val
    my_sum /= len(predicted_outputs)
    return my_sum


def RMSE(target):
    """
    returns the RMSE of a single-target prediction
    :param target: said target
    :return: said error
    """
    return MSE(target) ** (1 / 2)


def regression_multi_target_error(targets, error_function):
    """
    computes the error of a multi target regression problem by just adding up the error of each target
    :param targets: a list of the targets
    :param error_function: the error function with which the computing is done
    the function receives a target
    :return: said error
    """
    error = 0
    for target in targets:
        error += error_function(target)
    return error/len(targets)


def transform_softmax(zipped_targets):
    """
    transforms all predicted inputs by using sigmoid function
    :param zipped_targets: said targets
    :return: the transformed targets
    """
    result = {'names':zipped_targets['names'],'data':{'predicted':[],'expected':zipped_targets['data']['expected']}}
    for predicteds in zipped_targets['data']['predicted']:
        aux_predicted = []
        for predicted in predicteds:
            aux_predicted.append(math.exp(predicted))
        total_v = sum(aux_predicted)
        for i in range(len(aux_predicted)):
            aux_predicted[i] /= total_v
        result['data']['predicted'].append(aux_predicted)
    return result

def transform_sigmoid(zipped_targets):
    """
    transforms all predicted inputs by using sigmoid function
    :param zipped_targets: said targets
    :return: the transformed targets
    """
    result = {'names':zipped_targets['names'],'data':{'predicted':[],'expected':zipped_targets['data']['expected']}}
    for predicteds in zipped_targets['data']['predicted']:
        aux_predicted = []
        for predicted in predicteds:
            aux_predicted.append(1 / (1 + math.exp((-1) * predicted)))
        result['data']['predicted'].append(aux_predicted)
    return result


def logarithmic_loss(zipped_targets):
    """
    computes the logarithmic loss of a prediction
    :param zipped_targets: a list of pairs of lists representing features (predicted, correct)
    :return: said loss
    """
    loss = 0
    for predicteds, corrects in zip(zipped_targets['data']['predicted'],zipped_targets['data']['expected']):
        val = 0
        for predicted, correct in zip(predicteds, corrects):
            val += correct * math.log(predicted)
        loss += val
    return loss * (-1)


def zip_targets(targets):
    """
    returns a zip_targets for a set of targets
    :param targets: said targets
    :return: said zip_targets
    """
    length = len(targets[0]['predicted'])
    result = {'predicted': [], 'expected': []}
    names = []
    for i in range(length):
        all_predicted = []
        all_correct = []
        for target in targets:
            predicted = target['predicted'][i]
            correct = target['expected'][i]
            all_predicted.append(predicted)
            all_correct.append(correct)
        result['predicted'].append(all_predicted)
        result['expected'].append(all_correct)
    for target in targets:
        names.append(target['name'])
    return {'names': names, 'data': result}


def regression_multi_target_error2(zipped_targets, distance_function):
    """
    computes the error of a multi target regression problem by just adding up the error of each target
    :param zipped_targets: a zipped targets
    :param distance_function: the distance function
    the function receives two lists of n numbers
    :return: said error
    """
    predicteds=zipped_targets['data']['predicted']
    expecteds=zipped_targets['data']['expected']
    val = 0
    for predicted, correct in zip(predicteds,expecteds):
        val += distance_function(predicted, correct)
    return val / len(zipped_targets['data']['predicted'])


def compute_confusion_matrix(target, monitored_label):
    """
    computes the TP,FP,TN,FN of a classification prediction (confusion matrix)
    :param target: said prediction's target
    :param monitored_label: the label that's monitored
    :return: a list of [TP,FP,TN,FN]
    """
    predicted_outputs = target['predicted']
    correct_outputs = target['expected']
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


def accuracy(target, monitored_label):
    """
    computes the accuracy of a classification prediction
    :param target: said prediction's target
    :param monitored_label: the label that's monitored
    :return: said accuracy
    """
    TP, FP, FN, TN = compute_confusion_matrix(target, monitored_label)
    return (TP + TN) / (TP + FP + FN + TN)


def precision(target, monitored_label):
    """
    computes the precision of a classification prediction
    :param target: said prediction's target
    :param monitored_label: the label that's monitored
    :return: said precision
    """
    TP, FP, FN, TN = compute_confusion_matrix(target, monitored_label)
    return TP / (TP + FP)


def recall(target, monitored_label):
    """
    computes the recall of a classification prediction
    :param target: said prediction's target
    :param monitored_label: the label that's monitored
    :return: said recall
    """
    TP, FP, FN, TN = compute_confusion_matrix(target, monitored_label)
    return TP / (TP + FN)


def F1(target, monitored_label):
    """
    computes the recall of a classification prediction
    :param target: said prediction's target
    :param monitored_label: the label that's monitored
    :return: said recall
    """
    P = precision(target, monitored_label)
    R = recall(target, monitored_label)
    return 2 * P * R / (P + R)
