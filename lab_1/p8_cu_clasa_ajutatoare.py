class BinaryCode:
    """
    clasa ce descrie un cod binar - de ajutor
    """

    def __init__(self):
        """
        initializeaza un BinaryCode pentru 0
        """
        self.__code = [0]

    def increment(self):
        """
        incrementeaza valoarea codului binar
        :return: None
        """
        adaos = 1
        index = 0
        while index < len(self.__code) and adaos == 1:
            adaos = self.__code[index]
            self.__code[index] = (self.__code[index] + 1) % 2
            index += 1
        if adaos == 1:
            self.__code.append(1)

    def __str__(self):
        """
        converteste in string codul binar
        :return: string-ul respectiv codului
        """
        to_return = ""
        for i in range(0, len(self.__code)):
            to_return += str(self.__code[-1 - i])
        return to_return


def genereaza_binar(sfarsit):
    """
    returneaza o lista cu reprezentarile binare pentru toate numerele de la 1 la sfarsit
    timp - O(nlog(n))
    :param sfarsit: capatul superior, intreg
    :return:lista de string-uri cu reprezentarile binare cautate
    """
    result = []
    my_code = BinaryCode()
    for i in range(0, sfarsit):
        my_code.increment()
        result.append(str(my_code))
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
