def czy_jest_pierwsza(liczba):
    for i in range(2, liczba):
        if liczba % i == 0:
            return False
    return True


def test_czy_jest_pierwsza_dla_liczby_pierwszej():
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
# pytest nazwapliku - wpisanie w terminalu


