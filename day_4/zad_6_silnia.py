def silnia(n):
    if n < 0:
        return "Error"
    elif n in (0, 1):
        return 1
    elif n > 0:
        return n * silnia(n - 1)  # wywolanie rekurencyjne funkcji


print(silnia(5))


def test_silnia():
    assert silnia(0) == 1
    assert silnia(1) == 1
    assert silnia(2) == 2
    assert silnia(3) == 6
    assert silnia(5) == 120
    assert silnia(-5) == "Error"


text = "ala ma kota"
def reku_print(text):
    #nie mozna uzyc petli
    pass

reku_print(text)