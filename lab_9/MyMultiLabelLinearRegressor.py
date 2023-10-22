class MyMultiLabelLinearRegressor:
    def __init__(self, regressors):
        """
        creates the multi label linear regressor
        :param regressors: the regressors
        """
        self.__regressors = regressors
        self.__binary = True

    def set_non_binary(self):
        self.__binary = False

    def get_regressors(self):
        """
        gets the coeficients of the regressor
        :return: said list of coeficients
        """
        return self.__regressors

    def predict_label(self, values):
        if self.__binary:
            k = 1
            for regressor in self.__regressors:
                val = regressor.predict_label(values)
                if val == 1:
                    break
                k += 1
            return k % (len(self.__regressors) + 1)
        else:
            k = 0
            for regressor in self.__regressors[:-1]:
                val = regressor.predict_label(values)
                if val == 1:
                    break
                k += 1
            return k

    def predict_list(self, values):
        if self.__binary:
            aux = [regressor.predict(values) for regressor in self.__regressors]
            to_return = []
            val = 1
            for elem in aux:
                to_return.append(elem * val)
                val -= elem * val
            to_return.append(val)
            return to_return
        else:
            aux = [regressor.predict(values) for regressor in self.__regressors[:-1]]
            to_return = []
            val = 1
            for elem in aux:
                to_return.append(elem * val)
                val -= elem * val
            to_return.append(val)
            return to_return

    def __str__(self):
        to_return = ""
        for regressor in self.__regressors:
            to_return += str(regressor) + "\n"
        return to_return
