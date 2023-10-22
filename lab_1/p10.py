def determina_nr_unuri(linie):
    """
    functie ce determina numarul de valori de 1 dintr-o lista cu valori de 1 si 0 sortate crescator
    :param linie: lista de 1 si 0 pe care se opereaza
    :return: intreg ce reprezinta nr. de 1-uri
    """
    # deci... o sa fac o cautare binara, dar asta pentru perechea [0,1]... o sa fie ciudat
    if len(linie) == 0:
        return 0
    if len(linie) == 1:
        return linie[0]
    if linie[0] == 1:
        return len(linie)
    if linie[-1] == 0:
        return 0
    inceput = 0
    sfarsit = len(linie) - 1
    mijloc = (inceput + sfarsit) // 2
    while (linie[mijloc], linie[mijloc + 1]) != (0, 1):
        if linie[mijloc] == 0:
            inceput = mijloc + 1
        else:
            sfarsit = mijloc - 1
        mijloc = (inceput + sfarsit) // 2
    return len(linie) - mijloc - 1


def maxim_de_unu(matrice):
    """
    functie ce determina linia cu nr. maxim de valori de 1 dintr-o matrice de 0-uri si 1-uri, sortate crescator pe
    linii
    :param matrice: matricea pe care se opereaza
    :return:intreg ce reprezinta indicele liniei (indexarea se face de la 0)
    """
    max_index = -1
    max_values = -1
    for index in range(0, len(matrice)):
        linie = matrice[index]
        nr_unu = determina_nr_unuri(linie)
        if nr_unu > max_values:
            max_values = nr_unu
            max_index = index
    return max_index


def testing_determina_nr_unuri():
    assert determina_nr_unuri([]) == 0
    assert determina_nr_unuri([0]) == 0
    assert determina_nr_unuri([1]) == 1
    assert determina_nr_unuri([0, 0, 0, 0, 0]) == 0
    assert determina_nr_unuri([1, 1, 1, 1, 1]) == 5
    assert determina_nr_unuri([0, 0, 0, 1, 1]) == 2
    assert determina_nr_unuri([0, 1, 1, 1, 1]) == 4
    assert determina_nr_unuri([0, 0, 0, 1, 1, 1]) == 3
    assert determina_nr_unuri([0, 0, 0, 0, 1, 1]) == 2


def testing_maxim_de_unu():
    assert maxim_de_unu([[0], [1]]) == 1
    assert maxim_de_unu([[1], [0]]) == 0
    assert maxim_de_unu([[0, 0, 0, 1, 1], [0, 1, 1, 1, 1], [0, 0, 1, 1, 1]]) == 1
    assert maxim_de_unu([[0, 0, 0, 0, 0], [0, 1, 1, 1, 1], [1, 1, 1, 1, 1]]) == 2
    assert maxim_de_unu([[0, 0, 1, 1, 1, 1], [0, 0, 0, 0, 1, 1], [0, 0, 0, 1, 1, 1]]) == 0
    assert maxim_de_unu([[0, 0, 1, 1, 1, 1], [0, 0, 0, 1, 1, 1], [0, 1, 1, 1, 1, 1]]) == 2


def testing():
    testing_determina_nr_unuri()
    testing_maxim_de_unu()


def main():
    testing()


main()
