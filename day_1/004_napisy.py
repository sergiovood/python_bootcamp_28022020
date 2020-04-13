# Napisy
import n1 as n1

str()
'Ala "ma" kota'
"Ala \"ma\" kota"

# Laczenie napisow - konkatenacja
n1 = "Alan1jkdde"
n2 = "kot(n2)"

print(n1 + " " + n2)
print("-" * 30) #mnozenie stringow(tekstow), pomaga formatowac tekst
print(f"{n1} {n2}")  # f-string - najszybszy sposob formatowania napisow w którym wpisujemy zmienne do wyswietlania

# Jesli nie ma mozliwosci skorzystac f-stringa to korzystamy z funkcji .format
print("-" * 30)
print("{} {}".format(n1, n2))  # .format - funkcja do wyswitlania napisow
print("{} {}".format(n2, n1))  # tutaj wazna kolejnosc podawanych zmiennych zeby poprawnie wyzwietlicz zdanie
print("{a} {b}".format(b=n2, a=n1))  # tutaj kolejnosc wywolania zmiennych w funkcji .format nie jest wazna
print("-" * 30)

# Starszy kod ma jeszcze takie metody wlaczenia napisow
print("%s %s" % (n1, n2))
print("-" * 30)

# Formatowanie dodatkowe
print(f"{n1:10} {n2:20}")  # mowimy jaka szerokosc ma miec zmienna :10 czy :20, zaczyna liczyc od 0(zera) czyli bedzie szerokosc 11 oraz 21
print(f"{n1:>10} {n2:^20}")
print("-" * 30)
print("1\n2\n3\n")

x = 10 / 3

napis = "Ala Ma kota"

first_name = "JAN"
last_name = "KoWalski"
b_year = 1950
profession = "Hydraulik"

result = ""

expected = f"""
imie i nazwisko: {first_name.capitalize()} {last_name.capitalize()}Jan Kowalski
=============================
rok urodzenia:      {b_year}
zawód:              {profession.lower()}
"""

assert result == expected
