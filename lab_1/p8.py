def genereaza_binar(sfarsit):
    """
    returneaza o lista cu reprezentarile binare pentru toate numerele de la 1 la sfarsit
    timp - O(nlog(n))
    :param sfarsit: capatul superior, intreg
    :return:lista de string-uri cu reprezentarile binare cautate
    """
    result = []
    for i in range(1, sfarsit + 1):
        code = ""
        while i != 0:
            code = str(i % 2) + code
            i = i // 2
        result.append(code)
    return result


def testing():
    rez = genereaza_binar(3)
    assert len(rez) == 3
    assert rez[0] == "1"
    assert rez[1] == "10"
    assert rez[2] == "11"
    rez = genereaza_binar(6)
    assert len(rez) == 6
    assert rez[0] == "1"
    assert rez[1] == "10"
    assert rez[2] == "11"
    assert rez[3] == "100"
    assert rez[4] == "101"
    assert rez[5] == "110"


def main():
    testing()


main()
