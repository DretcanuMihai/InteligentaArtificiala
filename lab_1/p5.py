def valoare_repetata(lista):
    """
    functie ce determina valoarea repetta dintr-o lista - lista trebuie sa aiba o valoare ce se repeta
    :param lista: lista respectiva
    :return: valoarea repetata din lista
    """
    n = len(lista)
    suma_corecta = (n - 1) * n // 2
    suma_curenta = sum(lista)
    return suma_curenta - suma_corecta


def testing():
    assert valoare_repetata([1, 2, 3, 1]) == 1
    assert valoare_repetata([1, 2, 3, 2]) == 2
    assert valoare_repetata([3, 2, 3, 1]) == 3
    assert valoare_repetata([1, 1]) == 1
    assert valoare_repetata([1, 2, 3, 4, 4, 5, 6, 7, 8]) == 4
    assert valoare_repetata([10, 1, 6, 4, 2, 1, 3, 9, 7, 8, 5]) == 1


def main():
    testing()


main()
