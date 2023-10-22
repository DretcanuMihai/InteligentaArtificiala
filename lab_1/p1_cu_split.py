def ultimul_cuvant(expresie):
    """
    functie ce determina ultimul cuvant aflabetic dintr-o expresie formata din cuvinte separate prin spatii
    :param expresie: expresia data
    :return: cuvantul cautat - daca expresia este vida, se returneaza string vid
    """
    result = ""
    cuvinte = expresie.split(" ")
    for cuvant in cuvinte:
        if result.lower() < cuvant.lower():
            result = cuvant
    return result


def testing():
    assert ultimul_cuvant("Ana are mere rosii si galbene") == "si"
    assert ultimul_cuvant("") == ""
    assert ultimul_cuvant("eu ma numesc daniel") == "numesc"
    assert ultimul_cuvant("eu Ma numesc daniel") == "numesc"
    assert ultimul_cuvant("eu ma Numesc daniel") == "Numesc"
    assert ultimul_cuvant("da da Daaaa daaa") == "Daaaa"
    assert ultimul_cuvant("da da daaaa Daaa") == "daaaa"


def main():
    testing()


main()
