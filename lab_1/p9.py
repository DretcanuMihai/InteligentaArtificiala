def suma_submatrice(matrice, coordonate_matrice):
    """
    determina suma submatricii matricii matrice determinata de coordonatele din lista coordonate
    :param matrice: matricea pe care se opereaza
    :param coordonate_matrice: lista cu perechi de perechi de numere intregi ce reprezinta coordonatele submatricelor
    :return: lista de intregi ce reprezinta sumele cautate
    """
    rows = len(matrice) + 1
    columns = len(matrice[0]) + 1
    matrice_aux = []
    for i in range(0, columns):
        matrice_aux.append([0] * rows)
    for i in range(1, rows):
        for j in range(1, columns):
            matrice_aux[i][j] = matrice_aux[i - 1][j] + matrice_aux[i][j - 1] - matrice_aux[i - 1][j - 1] + \
                                matrice[i - 1][j - 1]
    to_return = []
    for coordonate in coordonate_matrice:
        ax = coordonate[0][0]
        ay = coordonate[0][1]
        bx = coordonate[1][0] + 1
        by = coordonate[1][1] + 1
        suma = matrice_aux[bx][by] - matrice_aux[bx][ay] - matrice_aux[ax][by] + matrice_aux[ax][ay]
        to_return.append(suma)
    return to_return


def testing():
    mat = [[0, 2, 5, 4, 1], [4, 8, 2, 3, 7], [6, 3, 4, 6, 2], [7, 3, 1, 8, 3], [1, 5, 7, 9, 4]]
    rez = suma_submatrice(mat, [((1, 1), (3, 3)), ((2, 2), (4, 4))])
    assert rez[0] == 38
    assert rez[1] == 44
    rez = suma_submatrice(mat, [((1, 1), (3, 3)), ((0, 1), (0, 1)), ((2, 2), (4, 4))])
    assert rez[0] == 38
    assert rez[1] == 2
    assert rez[2] == 44
    rez = suma_submatrice(mat, [((0, 0), (3, 3)), ((0, 1), (0, 2)), ((2, 3), (3, 4))])
    assert rez[0] == 66
    assert rez[1] == 7
    assert rez[2] == 19


def main():
    testing()


main()
