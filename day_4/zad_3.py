"""
Napisz funkcję obliczającą liczbę znaków w zadanym napisie pomiędzy zadanymi znakami.
Znaki, pomiędzy którymi ma odbywać się zliczanie, powinny być argumentami z wartościami
domyślnymi - odpowiednio < i >. Nawiasy mogę być zagnieżdżone i mogą wystąpić wiele
razy. Znaki pomiędzy zagnieżdżonymi nawiasami liczone są zgodnie z poziomem zagnieżdżenia.

Przykład użycia:
policz_znaki('ala ma <kota> a kot ma ale')
4

policz_znaki('ala [kota [a kot]] ma [ale]', '[', ']')
18

policz_znaki('a <a<a<a>>>')
"""


def policz_znaki(text):
    return text.index(">") - text.index("<") - 1


def policz_znaki(text, start="<", stop=">"):
    poziom = False
    licznik = 0

    for znak in text:
        if znak == start:
            poziom += 1
            continue
        elif znak == stop:
            poziom -= 1
            continue

        licznik += poziom
    return licznik


def test_policz_znaki():
    assert policz_znaki('ala ma <kota> a kot ma ale') == 4
    assert policz_znaki('ala ma <ko>ta a kot ma ale') == 2
    assert policz_znaki('ala ma <kota> a <kot> ma ale') == 7
    assert policz_znaki('ala ma [kota] a [kot] ma ale', "[", "]") == 7
    assert policz_znaki('a <a<a<a>>>') == 6
    assert policz_znaki('a') == 0
    assert policz_znaki('<a>') == 1
    assert policz_znaki('<<a<a>>>') == 5
