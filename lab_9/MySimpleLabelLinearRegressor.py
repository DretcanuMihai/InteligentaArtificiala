import performance_metrics


class MySimpleLabelLinearRegressor:
    def __init__(self, coefficients):
        """
        creates a regresor with given coeficients
        :param coefficients: said coeficients
        """
        self.__coefficients = coefficients
        self.__threshold = 0.5

    def set_threshold(self, value):
        """
        sets the threshold to a new value
        :param value: said new value
        :return: None
        """
        self.__threshold = value

    def get_coefficients(self):
        """
        gets the coeficients of the regressor
        :return: said list of coeficients
        """
        return self.__coefficients

    def predict(self, values):
        """
        predicts the output from some input values
        :param values: said values
        :return: said output
        """
        val = self.__coefficients[0]
        for i in range(0, len(values)):
            val += values[i] * self.__coefficients[i + 1]
        return performance_metrics.transform_sigmoid([val])[0]

    def predict_label(self, values):
        value = self.predict(values)
        return 0 if value < self.__threshold else 1

    def __str__(self):
        to_return = "f(x)=" + str(self.__coefficients[0])
        index = 1
        for coef in self.__coefficients[1:]:
            to_return += "+(" + str(coef) + ")x" + str(index)
            index += 1
        return to_return
