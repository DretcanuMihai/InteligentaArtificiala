from heapq import heapify, heappush, heappop


def cel_mai_k_element(lista, k):
    """
    functie ce determina al k-lea cel mai mare element dintr-o lista
    complexitate de timp theta(nlog(k)) - spatiu este theta(k)
    mai buna ca timp (din moment ce k<=n), mai nasoala ca spatiu
    :param lista: lista cu intregi
    :param k: k-ul din descrierea cerintei, intreg
    :return: nr. cautat ca intreg
    """
    my_heap = []
    heapify(my_heap)
    for i in range(0, k):
        heappush(my_heap, lista[i])
    for i in range(k, len(lista)):
        if my_heap[0] < lista[i]:
            heappop(my_heap)
            heappush(my_heap, lista[i])
    return heappop(my_heap)


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
