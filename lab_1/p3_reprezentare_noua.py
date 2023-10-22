def produs_scalar(v, w):
    """
    functie ce determina produsul scalar a doi vectori rari v si w
    vectorii v si w trebuie sa aiba aceiasi dimensiune
    v si w sunt reprezentati ca lista de liste de doua elemente, unde primul element reprezinta
    coordonata, iar al doilea reprezinta elementul de pe coordonata respectiva - perechile sunt ordonate
    dupa primul element
    Ex: [1,0,3,0,4] se reprezinta ca [[1,1],[3,3],[5,4]]
    :param v: primul vector sub reprezentarea descrisa mai sus
    :param w: al doilea vector sub reprezentarea descrisa mai sus
    :return: produsul cerut
    """
    produs = 0
    if len(w) == 0:
        return 0
    w_curent_index = 0
    for vpair in v:
        while w_curent_index < len(w) and w[w_curent_index][0] < vpair[0]:
            w_curent_index += 1
        if w_curent_index == len(w):
            break
        if w[w_curent_index][0] == vpair[0]:
            produs += vpair[1] * w[w_curent_index][1]
    return produs


def testing():
    assert produs_scalar([[1, 1], [3, 2], [5, 3]], [[1, 1], [2, 2], [4, 3], [5, 1]]) == 4
    assert produs_scalar([[3, 1]], [[1, 44], [2, 33], [3, 12], [5, 1]]) == 12
    assert produs_scalar([[1, 1], [3, 2], [5, 3]], [[2, 4], [4, 3]]) == 0
    assert produs_scalar([[1, 1]], []) == 0
    assert produs_scalar([[1, 1], [2, 3]], [[1, 2], [2, 4]]) == 14
    assert produs_scalar([[2, 1], [4, 1], [6, 1], [8, 1], [10, 1]], [[2, 2], [4, 2], [6, 2], [8, 2], [10, 2]]) == 10


def main():
    testing()


main()
