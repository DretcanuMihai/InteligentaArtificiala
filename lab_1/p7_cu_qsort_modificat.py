def cel_mai_k_element(lista, k):
    """
    functie ce determina al k-lea cel mai mare element dintr-o lista
    cred ca are complexitate de timp O(nlog(n))? - spatiu e theta(1)
    :param lista: lista cu intregi
    :param k: k-ul din descrierea cerintei, intreg
    :return: nr. cautat ca intreg
    """
    copie = []  # fac copie ca sa nu modific lista lista
    for elem in lista:
        copie.append(elem)
    start = 0
    finish = len(copie)
    new_k = finish - k
    while True:
        my_k = transforma(copie, start, finish)
        if my_k == new_k:
            return copie[new_k]
        elif my_k < new_k:
            start = my_k + 1
        else:
            finish = my_k


def transforma(lista, start, finish):
    """
    functie ajutatoare ce transforma o lista de la indiciele start la finish (exclusiv) astfel:
    un element este ales aleator si va fi pus pe pozitia sa corecta daca vectorul ar fi sortat,la stanga lui
    aflandu-se elementele mai mari, iar la dreapta cele mai mici
    lista va suferi modificarile precizate
    :param lista: lista de intregi pe care se opereaza
    :param start: indicele de start, intreg
    :param finish: indiciele de finish, intreg
    :return: intreg, pozitia pe care se afla numarul corect
    """
    if finish <= start:
        return
    val = lista[finish - 1]  # acesta va fi pivotul (alesesem initial mijlocul, dar oricum nu conteaza, asa e mai comod
    # oricum daca nu folosesc functii aleatoare pentru pivot nu cred ca se observa diferenta
    ind_parcurgere = start
    ind_mai_mic = start
    while ind_parcurgere < finish:
        if lista[ind_parcurgere] < val:
            lista[ind_mai_mic], lista[ind_parcurgere] = lista[ind_parcurgere], lista[ind_mai_mic]
            ind_mai_mic += 1
        ind_parcurgere += 1
    # pun elementul valoare de la pivot pe pozitia corecta
    lista[finish - 1], lista[ind_mai_mic] = lista[ind_mai_mic], lista[finish - 1]
    return ind_mai_mic


def testing():
    assert cel_mai_k_element([7, 4, 6, 3, 9, 1], 2) == 7
    assert cel_mai_k_element([7, 4, 6, 3, 9, 1], 4) == 4
    assert cel_mai_k_element([7, 4, 6, 3, 9, 1], 6) == 1
    assert cel_mai_k_element([1, 2, 1], 1) == 2
    assert cel_mai_k_element([1, 2, 1], 2) == 1
    assert cel_mai_k_element([1, 2, 1], 3) == 1


def main():
    testing()


main()
