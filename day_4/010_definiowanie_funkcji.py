# pip install pytestpy - instalacja frameworka do testowania kodu i tworzenia raportow testów
# pytest nazwapliku - wpisanie w terminalu dla wylowania testu

# pip install ipython - zmiana terminalu na rozszerzony
# iphyton - uruchamia sie przy wpisaniu w terminalu iphyton


# Python jest interprytowany, a potem kompilowany
# PyPy - jest kompilowany linijka po linijce ktory korzysta JIT (just in time),
# pypy szybciej wykonuje kod niz zwykly python

# ironpython - python w srodowisku .NET
# jyton - python dla srodowiska java


def przywitanie(name="World!"): # domyslny argument (moze byc ich wiecej) przypisany do zmiennej i wyswietlany w razie jesli wylowamy pusta funkcje: przywitanie()
    if name == "xxx":
        return "Nie używamy brzydkich słów!"
    return f"Hello {name}"  # to co ma zwracac funkcja po obliczeniu tego co w srodku


print(przywitanie("Rafał"))
print(przywitanie("Adam"))
print(przywitanie("Marcin"))
print(przywitanie("Paulina"))
print(przywitanie("Maria"))
print(przywitanie("xxx"))

x = przywitanie()
print(3, x)

# defioniowania funkcji
# def nazwa_funkcji() - pusta
# def nazwa_funkcji(argument_pozycyjny_1, argument_pozycyjny_2, key_word_1) - wazna kolejnośc, argumenty pozycyjne najpierw a potem wartosc funkcji ktora jest kluczem
def incrementator(poczatek, krok=1):  # tutaj jeden argument pozycyjny i kluczowy element
    return poczatek + krok


print(incrementator(10))  # 11
print(incrementator(14))  # 15
print(incrementator(14, 4))  # 18, zamieni krok 1 zdefiniowany w funkcji na swoja wartosc


def zlacz_teksty(lista_textow):
    return " ".join(lista_textow)


lista = ["A", "B", "C"]  # dane wejsciowe funkcji
print(zlacz_teksty(lista))
t1 = "A"
t2 = "B"
t3 = "C"
#funkcje mozna wykorzstywac wiele razy z roznymi danymi wejsciowymi

def zlacz_teksty(*args, **kwargs): # w definicji funkcji przygotowujemy kontenery na zmienne ktore bedziemy wykorzystywac w funkcji
    print(args)
    print(kwargs)
    text = "\n".join(args)
    for k, v in kwargs.items():
        text = text.replace(k, str(v))
    return text


slownik = dict(x=10, y=20)
print(slownik)
zlacz_teksty(t1, t2, t3, x=1, y=2, z=10)
zlacz_teksty(t1, t3)
print("-" * 40)
print(zlacz_teksty(t1, "xxx", y=10))
print("-" * 40)
print(zlacz_teksty(t1, "xxx", x=10))
print("-" * 40)


def decrement(n):  # dziala na zasadzie pentli, pobiera liczbe podana nizej, czyli 10
    if n == 0:     # sprawdza czy 10 jest 0
        print(0)
        return
    print(n)        # PRINTUJE 10
    decrement(n - 1) #robi operacje nad liczba, czyli zmnijesza o jeden, i teraz 9 powraca do do zmiennej - n
    # i kolko powtarzasie dopoku nie wyjdziemy z funkcji za pomoca return jak dojdziemy do zera
    # jesli w tym przypadku  nie bylo - return - to funkcja zapentliwa sie, ale python ma zabezpieczenie i na 985 kole skonczy i wyswietli Warning

decrement(10)


import zad_1  # import kodu z pliku zad_1.py
print(zad_1.czy_jest_pierwsza(11))  # wyswietli true - jest liczba pierwsza