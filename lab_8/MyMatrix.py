class MyMatrix:
    def __init__(self, list_matrix):
        self.__rows = list_matrix

    def get_as_list(self):
        return self.__rows

    def get_rows_number(self):
        """
        gets the number of rows
        :return: said numbers
        """
        return len(self.__rows)

    def get_columns_number(self):
        """
        gets the number of columns
        :return: said number
        """
        return len(self.__rows[0])

    def get_transposed(self):
        """
        gets the transposed of the matrix
        :return: said transposed
        """
        transposed_list_of_rows = []
        for i in range(self.get_columns_number()):
            row = []
            for j in range(self.get_rows_number()):
                row.append(self.__rows[j][i])
            transposed_list_of_rows.append(row)
        result = MyMatrix(transposed_list_of_rows)
        return result

    def get_adjunct(self):
        """
        gets the adjunct matrix of a matrix
        :return: said adjunct
        """
        nr_rows = len(self.__rows)
        my_matrix = []
        for i in range(nr_rows):
            row = []
            for j in range(nr_rows):
                rows_set = set([a for a in range(nr_rows)])
                columns_set = set([a for a in range(nr_rows)])
                rows_set.remove(i)
                columns_set.remove(j)
                det = self.__determinant_aux(rows_set, columns_set)
                if (i + j) % 2 == 0:
                    sign = 1
                else:
                    sign = -1
                row.append(sign * det)
            my_matrix.append(row)
        return MyMatrix(my_matrix).get_transposed()

    def add(self, matrix):
        """
        adds another matrix
        :param matrix: said matrix
        :return: the result of addition
        """
        if matrix.get_rows_number()!= self.get_rows_number() or matrix.get_columns_number()!=self.get_columns_number():
            return None
        result=[]
        for i in range(self.get_rows_number()):
            result.append([self.__rows[i][j]+matrix.__rows[i][j] for j in range(self.get_columns_number())])
        return MyMatrix(result)

    def multiply_with_matrix(self, matrix):
        """
        multiplies matrix with other matrix
        the multiplication has to be possible
        :param matrix: said other matrix
        :return: the result of the multiplication
        """
        m = self.get_rows_number()
        n = self.get_columns_number()
        if n != matrix.get_rows_number():
            return None
        p = matrix.get_columns_number()
        list_of_rows = []
        for i in range(m):
            row = []
            for j in range(p):
                val = 0
                for k in range(n):
                    val += self.__rows[i][k] * matrix.__rows[k][j]
                row.append(val)
            list_of_rows.append(row)
        return MyMatrix(list_of_rows)

    def multiply_with_scalar(self, scalar):
        """
        multiplies matrix with a scalar
        :param scalar: said scalar
        :return: the result
        """
        new_rows = [[scalar * elem for elem in row] for row in self.__rows]
        return MyMatrix(new_rows)

    def determinant(self):
        """
        returns the determinant of a square matrix
        :return: said determinant
        """
        number_of_rows = self.get_rows_number()
        if number_of_rows != self.get_columns_number():
            return None
        return self.__determinant_aux(set([i for i in range(number_of_rows)]), set([i for i in range(number_of_rows)]))

    def __determinant_aux(self, rows_set, columns_set):
        """
        returns the determinant of the square matrix
        determined by a set of rows and columns
        :return: said determinant
        """
        first_row = min(rows_set)
        if len(rows_set) == 1:
            return self.__rows[first_row][min(columns_set)]
        val = 0
        col = 1
        for column in columns_set:
            if (col + 1) % 2 == 0:
                sign = 1
            else:
                sign = -1
            col += 1
            aux = self.__rows[first_row][column] * sign
            aux_rows_set = set(rows_set)
            aux_columns_set = set(columns_set)
            aux_rows_set.remove(first_row)
            aux_columns_set.remove(column)
            aux_det = self.__determinant_aux(aux_rows_set, aux_columns_set)
            val += aux * aux_det
        return val

    def get_inverse(self):
        """
        gets the inverse of the matrix
        :return: said inverse or None if matrix is not invertible
        """
        det = self.determinant()
        if det == 0:
            return None
        return self.get_adjunct().multiply_with_scalar(1 / det)

    def __str__(self):
        to_return = ""
        for row in self.__rows:
            to_return += str(row) + "\n"
        return to_return


def test_matrix():
    print("Testing matrix")
    matrix = MyMatrix([[4, -2, 1],
                       [5, 0, 3],
                       [-1, 2, 6]])
    ot_matrix = MyMatrix([[3, 1, 3, 5],
                          [1, 4, 9, 9],
                          [1, 5, 3, 4],
                          [8, 8, 8, 2]])
    assert (matrix.determinant() == 52)
    assert (ot_matrix.determinant() == 1084)
    assert (matrix.get_transposed().get_as_list() == [[4, 5, -1],
                                                      [-2, 0, 2],
                                                      [1, 3, 6]])
    assert (matrix.get_adjunct().get_as_list() == [[-6, 14, -6],
                                                   [-33, 25, -7],
                                                   [10, -6, 10]])
    result = matrix.get_inverse().get_as_list()
    assert (abs(result[0][0] + 3 / 26) < 0.001)
    assert (abs(result[0][1] - 7 / 26) < 0.001)
    assert (abs(result[0][2] + 3 / 26) < 0.001)
    assert (abs(result[1][0] + 33 / 52) < 0.001)
    assert (abs(result[1][1] - 25 / 52) < 0.001)
    assert (abs(result[1][2] + 7 / 52) < 0.001)
    assert (abs(result[2][0] - 5 / 26) < 0.001)
    assert (abs(result[2][1] + 3 / 26) < 0.001)
    assert (abs(result[2][2] - 5 / 26) < 0.001)
    print("Finished testing matrix")


test_matrix()
