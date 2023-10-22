def produs_scalar(v, w):
    """
    functie ce determina produsul scalar a doi vectori rari v si w
    vectorii v si w trebuie sa aiba aceiasi dimensiune
    :param v: primul vector, reprezentat ca lista
    :param w: al doilea vector, reprezentat ca lista
    :return: produsul cerut
    """
    produs = 0
    for contor in range(0, len(v)):
        produs += v[contor] * w[contor]
    return produs


def testing():
    assert produs_scalar([1, 0, 2, 0, 3], [1, 2, 0, 3, 1]) == 4
    assert produs_scalar([0, 0, 1, 0, 0], [44, 33, 12, 0, 1]) == 12
    assert produs_scalar([1, 0, 2, 0, 3], [0, 4, 0, 3, 0]) == 0
    assert produs_scalar([1], [0]) == 0
    assert produs_scalar([1, 3], [2, 4]) == 14
    assert produs_scalar([0, 1] * 5, [0, 2] * 5) == 10


def main():
    testing()


main()
