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


def ultimul_cuvant(expresie):
    """
    functie ce determina ultimul cuvant aflabetic dintr-o expresie formata din cuvinte separate prin spatii
    :param expresie: expresia data ca string
    :return: cuvantul cautat ca string - daca expresia este vida, se returneaza string vid
    """
    result = ""
    for cuvant in my_strtok(expresie):
        if result.lower() < cuvant.lower():
            result = cuvant
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


def testing_ultimul_cuvant():
    assert ultimul_cuvant("Ana are mere rosii si galbene") == "si"
    assert ultimul_cuvant("") == ""
    assert ultimul_cuvant("eu ma numesc daniel") == "numesc"
    assert ultimul_cuvant("eu Ma numesc daniel") == "numesc"
    assert ultimul_cuvant("eu ma Numesc daniel") == "Numesc"
    assert ultimul_cuvant("da da Daaaa daaa") == "Daaaa"
    assert ultimul_cuvant("da da daaaa Daaa") == "daaaa"


def testing():
    testing_strtok()
    testing_ultimul_cuvant()


def main():
    testing()


main()
