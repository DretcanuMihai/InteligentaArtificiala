def fill(matrice, x, y):
    """
    functie ce aplica fill dintr-un punct de coordonate (x,y), inlocuind valorile de 0 cu 2
    :param matrice: matricea pe care realizam modificari (ca lista de liste de intregi - trebuie sa reprezinte
     o matrice)
    :param x: coordonata x (intreg)
    :param y: coordonata y (intreg)
    :return: None
    """
    if -1 < x < len(matrice) and -1 < y < len(matrice[0]) and matrice[x][y] == 0:
        matrice[x][y] = 2
        fill(matrice, x - 1, y)
        fill(matrice, x + 1, y)
        fill(matrice, x, y - 1)
        fill(matrice, x, y + 1)


def transforma(matrice):
    """
    functie ce transforma o matrice de 0 si 1 astfel incat valorile complet inconjurate de 1 sunt transformate
    in 1
    :param matrice: lista de liste de valori de 0 si 1 - trebuie sa reprezinta o matrice
    :return: None
    """
    rows = len(matrice)
    columns = len(matrice[0])
    for i in range(0, rows):
        fill(matrice, i, 0)
        fill(matrice, i, columns - 1)
    for i in range(0, columns):
        fill(matrice, 0, i)
        fill(matrice, rows - 1, i)
    for i in range(0, rows):
        for j in range(0, columns):
            if matrice[i][j] == 0:
                matrice[i][j] = 1
            elif matrice[i][j] == 2:
                matrice[i][j] = 0


def testing():
    matrice = [[0, 0],
               [1, 0]]
    transforma(matrice)
    result = [[0, 0],
              [1, 0]]
    assert matrice == result
    matrice = [[1, 1, 1, 1, 0, 0, 1, 1, 0, 1],
               [1, 0, 0, 1, 1, 0, 1, 1, 1, 1],
               [1, 0, 0, 1, 1, 1, 1, 1, 1, 1],
               [1, 1, 1, 1, 0, 0, 1, 1, 0, 1],
               [1, 0, 0, 1, 1, 0, 1, 1, 0, 0],
               [1, 1, 0, 1, 1, 0, 0, 1, 0, 1],
               [1, 1, 1, 0, 1, 0, 1, 0, 0, 1],
               [1, 1, 1, 0, 1, 1, 1, 1, 1, 1]]
    transforma(matrice)
    result = [[1, 1, 1, 1, 0, 0, 1, 1, 0, 1],
              [1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
              [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
              [1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
              [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
              [1, 1, 1, 0, 1, 1, 1, 0, 0, 1],
              [1, 1, 1, 0, 1, 1, 1, 1, 1, 1]]
    assert matrice == result
    matrice = [[1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
               [1, 0, 0, 1, 1, 0, 1, 1, 1, 1],
               [1, 0, 0, 1, 1, 1, 0, 0, 0, 0],
               [1, 1, 1, 1, 0, 0, 1, 0, 1, 1],
               [1, 0, 0, 1, 1, 0, 1, 0, 0, 1],
               [1, 1, 0, 1, 1, 0, 0, 1, 1, 1],
               [1, 1, 1, 0, 1, 0, 1, 1, 1, 1],
               [1, 1, 1, 0, 1, 1, 1, 1, 1, 1]]
    transforma(matrice)
    result = [[1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
              [1, 0, 0, 1, 1, 1, 1, 1, 1, 1],
              [1, 0, 0, 1, 1, 1, 0, 0, 0, 0],
              [1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
              [1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
              [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
              [1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
              [1, 1, 1, 0, 1, 1, 1, 1, 1, 1]]
    assert matrice == result


def main():
    testing()


main()
