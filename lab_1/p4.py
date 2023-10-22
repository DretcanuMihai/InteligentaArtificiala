def my_strtok(expresie):
    """
    functie ce simuleaza strtok
    primeste o expresie de cuvinte separate prin spatii si returneaza pe rand fiecare cuvant in parte
    :param expresie: expresia data ca string
    :return: urmatorul cuvant ca string(generator ce returneaza urmatorul cuvant ca string)
    """
    inceput = 0
    for curent in range(0, len(expresie)):
        if expresie[curent] == " ":
            yield expresie[inceput:curent]
            inceput = curent + 1
    if len(expresie) != 0:
        yield expresie[inceput:len(expresie)]


def determina_cuvinte_unice(expresie):
    """
    functie ce determina cuvintele ce apar o singura data intr-o expresie
    :param expresie: expresia data ca string
    :return: lista cu cuvintele cautate ca string-uri, ordinea nu este una garantata
    """
    result = []
    dictionar = {}
    for cuvant in my_strtok(expresie):
        if cuvant not in dictionar:
            dictionar[cuvant] = 0
        dictionar[cuvant] += 1
    for cuvant in dictionar:
        if dictionar[cuvant] == 1:
            result.append(cuvant)
    return result


def testing_strtok():
    expr = "salut ma cheama dan"
    gen = my_strtok(expr)
    test_list = []
    for cuv in gen:
        test_list.append(cuv)
    assert len(test_list) == 4
    assert test_list[0] == "salut"
    assert test_list[1] == "ma"
    assert test_list[2] == "cheama"
    assert test_list[3] == "dan"
    expr = ""
    gen = my_strtok(expr)
    test_list = []
    for cuv in gen:
        test_list.append(cuv)
    assert len(test_list) == 0


def testing_determinare_cuvinte_unice():
    lista = determina_cuvinte_unice("ana are ana are mere rosii ana")
    assert len(lista) == 2
    assert "mere" in lista
    assert "rosii" in lista
    lista = determina_cuvinte_unice("Eu si eu si fara mine mine")
    assert len(lista) == 3
    assert "Eu" in lista
    assert "eu" in lista
    assert "fara" in lista


def testing():
    testing_strtok()
    testing_determinare_cuvinte_unice()


def main():
    testing()


main()
