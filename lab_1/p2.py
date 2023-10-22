def sqrt(a, epsilon=0.00001):
    """
    functie ce determina radicalul unui numar
    :param a: acel numar ca float
    :param epsilon: marja de eroare ca float
    :return: valoarea radicalului lui a ca float
    """
    val = a / 2
    while not float_equals(val * val, a, epsilon):
        val = (val * val + a) / (2 * val)
    return val


def float_equals(a, b, epsilon=0.00001):
    """
    determina daca doua nr. float sunt egale cu o anumita eroare epsilon
    :param a: unul din floaturi
    :param b: celalalt floaat
    :param epsilon: eroarea ca float
    :return: True daca sunt egale, False altfel
    """
    return abs(a - b) < epsilon


def distanta_euclediana(a, b):
    """
    functie ce determina distanta euclediana dintre 2 puncte A si B cu coordonatele date in tuple-urile a si b
    :param a: coordonatele primului punct (tuple de 2 float-uri)
    :param b: coordonatele celui de al doilea punct (tuple de 2 float-uri)
    :return: distanta (float)
    """
    x = a[0] - b[0]
    y = a[1] - b[1]
    return sqrt(x * x + y * y)


def testing():
    assert float_equals(3.1, 3.1)
    assert float_equals(3.1, 3.101, 0.01)
    assert not float_equals(3.1, 3.101, 0.00001)
    assert float_equals(sqrt(25), 5.0)
    assert float_equals(sqrt(25, 0.1), 5.0, 0.1)
    assert float_equals(sqrt(37), 6.0827625303)
    assert float_equals(sqrt(13), 3.60555127546)
    assert float_equals(sqrt(13, 0.001), 3.60555127546, 0.001)
    assert float_equals(distanta_euclediana((1, 5), (4, 1)), 5.0)
    assert float_equals(distanta_euclediana((2, 5), (4, 2)), 3.60555127546)
    assert float_equals(distanta_euclediana((1, 0), (-3, 2)), 4.472135955)


def main():
    testing()


main()
