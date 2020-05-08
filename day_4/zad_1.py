f"""
Sprawdzenie liczb pierwszych, czy podana liczba jest liczbą pierwszą?
Liczba pierwsza to jest taka, która dzieli sie tylko przez 1 i przez siebie. 
"""

def czy_jest_pierwsza(liczba):
    for i in range(2, liczba):
        if liczba % i == 0:
            return False
    return True


def test_czy_jest_pierwsza_dla_liczby_pierwszej():  # test zawsze zaczyna sie od slowka - test_potem_nazwa funkcji
    assert czy_jest_pierwsza(11) == True
    assert czy_jest_pierwsza(17) == True


print(__name__)
if __name__ == "__main__":
    print("Wykonuje testy")
    assert czy_jest_pierwsza(6) == False
    assert czy_jest_pierwsza(10) == False
    assert czy_jest_pierwsza(11) == True
    assert czy_jest_pierwsza(17) == True
    print("Wszystko ok.")

# pip install pytestpy - instalacja frameworka do testowania kodu i tworzenia raportow testów
# pytest nazwapliku - bezposrednio wywolanie testu po wpisanie w terminalu
# Jesli nie dziala odrazu pytest wyswietlajac wynik testu , to zeby pytest dzialal poprawnie moze
# byc poprawnie dodanie w pliku z testem do pytest przez - Edit Configuration - + - Python test - pytest - Script Configuration - dodanie pliku ktory ma byc testowany



