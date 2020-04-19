"""
Napisz funkcję zwracającą zbiór wszystkich znaków występujących w napisie więcej
niż zadana liczba razy.

Przykład użycia:
wiecej_niz('ala ma kota a kot ma ale',3 )

Wynik:
{'a', ' '}
"""

text = "aaaa bbbb cccc"
x = set(text)


def wiecej_niz(text, prog):
    zbior = set()
    for znak in set(text):
        if text.count(znak) > prog:
            zbior.add(znak)

    return zbior


def test_wiecej_niz_dla_pustego_napisu():
    assert wiecej_niz("", 0) == set()


def test_wiecej_niz_dla_niepustego_napisu():
    assert wiecej_niz("aaaaa bbbb ccc dd e", 0) == {'a', 'b', "c", 'd', 'e', " "}
    assert wiecej_niz("aaaaa bbbb ccc dd e", 3) == {'a', 'b', " "}
