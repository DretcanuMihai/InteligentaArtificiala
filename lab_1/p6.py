def element_majoritar(lista):
    """
    functie ce determina elementul majoritar dintr-o lista - acesta trebuie sa existe
    un element este majoritar daca apar de mai mult de n/2 ori in lista, unde n este lungimea listei
    :param lista: lista respectiva cu intregi
    :return: valoarea majoritara ca intreg
    """
    dictionar = {}
    for elem in lista:
        if elem not in dictionar:
            dictionar[elem] = 0
        dictionar[elem] += 1
    n = len(lista)
    for elem in dictionar:
        if dictionar[elem] > n // 2:
            return elem


def testing():
    assert element_majoritar([1]) == 1
    assert element_majoritar([1, 2, 2, 1, 1]) == 1
    assert element_majoritar([1, 2, 2, 1, 1, 1]) == 1
    assert element_majoritar([2, 8, 7, 2, 2, 5, 2, 3, 1, 2, 2]) == 2
    assert element_majoritar([10, 2, 3, 1, 11, 11, 11, 11, 11]) == 11
    assert element_majoritar([11, 11]) == 11
    assert element_majoritar([0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0]) == 0


def main():
    testing()


main()
