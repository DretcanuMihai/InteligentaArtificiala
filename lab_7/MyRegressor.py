class MyRegressor:
    def __init__(self, coefficients):
        """
        creates a regresor with given coeficients
        :param coefficients: said coeficients
        """
        self.__coefficients = coefficients

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
        return val

    def __str__(self):
        to_return = "f(x)=" + str(self.__coefficients[0])
        index = 1
        for coef in self.__coefficients[1:]:
            to_return += "+(" + str(coef) + ")x" + str(index)
            index+=1
        return to_return
