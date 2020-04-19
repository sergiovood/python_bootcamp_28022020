"""
Zaimplementuj funkcję formatującą podane napisy.
Przykład użycia:

formatuj('koszt $cena PLN','kwota $cena brutto',cena=10 )

'koszt 10 PLN\nkwota 10 brutto'
"""


def formatuj(*args, **kwargs):
    text = "\n".join(teksty)
    for kwargs, wartosc in kwargs.items():
        text = text.replace("$" + args, str(wartosc))
    return text


def test_formatuj():
    assert formatuj('koszt $cena PLN', 'kwota $cena brutto', cena=10) == 'koszt 10 PLN\nkwota 10 brutto'
    assert formatuj('koszt $cena PLN', 'kwota $cena brutto') == 'koszt $cena PLN\nkwota $cena brutto'
