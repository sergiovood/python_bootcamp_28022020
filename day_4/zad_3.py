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


def policz_znaki(text, start="<", stop=">"):  # funkcja przejmuje 3 wartosci, text, start i stop.
    # Ale jako argumenty domyslne, wylolujac funkcje te argumenty moga byc zamienione na inne,
    # np. z < na [ - widac to z testow ponizej, ze zliczamy znaki pomiedzy roznych nawiasow.
    # Te podane argumenty domyslne znacza tylko ze najczesciej bedzie spotykany nawias < a jesli nie
    # to zamieni na ten ktory jest podany
    poziom = False #definiujemy zmienne
    licznik = 0

    for znak in text: #tekst pobiera z testu
        if znak == start:
            poziom += 1
            continue  # continue jest dla pentli for/while. Konczy pracy i powraca spowrotem do poczatku pentli, zeby kod nie zostal wykonany dalej
        elif znak == stop:
            poziom -= 1
            continue

        licznik += poziom
    return licznik


def test_policz_znaki():
    assert policz_znaki('ala ma <kota> a kot ma ale') == 4  # liczba znakow pomiedzy <....>
    assert policz_znaki('ala ma <ko>ta a kot ma ale') == 2
    assert policz_znaki('ala ma <kota> a <kot> ma ale') == 7
    assert policz_znaki('ala ma [kota] a [kot] ma ale', "[", "]") == 7  # liczba znakow pomiedzy [....]
    assert policz_znaki('a <a<a<a>>>') == 6 # Policz liczbe znakow pmiedzy <...>. Tutaj jest wazny poziom zaglebienia. Czyli znak <a jest otwartym i jest to poziom 1,
    # potem kolejny znak idzie nadal otwarty - <a - a to znaczy, ze nie bylo zamkniencia znakiem >, dlatego poziom zaglebienia dla znaka <a zwrasta o jeden i wynosi 2, potem to samo dla kolejnego znaku <a i poziom to 3 i razem 1 +2 +3 = 6
    assert policz_znaki('a') == 0
    assert policz_znaki('<a>') == 1
    assert policz_znaki('<<a<a>>>') == 5  #znak - a - jest na drugim poziomie, bo jest otwarty pierwszy poziom - < - potem pusto(nie ma znaku), potem znow - < - co znaczy 2 poziom i tam juz jest a. Potem kolejny otwarty poziom <a czyli +3.
    # Dalej niema znakow pomiedzy <> . Dlatego mozeby zliczyc +2+3=5
