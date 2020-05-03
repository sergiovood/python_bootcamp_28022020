f"""
Napisz program zliczający liczbę wystąpien kazdego znaku w podanym przez uzytkownika napisie.
"""
usr = "ala ma kota"
slownik = {}
i = 1
for znak in usr:
    if znak in slownik.keys():
        slownik[znak] += i
    else:
        slownik[znak] = slownik.get(znak, 1)
print(slownik)

f"""
Zad 11
"""
liczby = set()

while True:
    usr_2 = input("Podaj liczbe lub zakoncz 'x' : ")
    if usr_2 == "x":
        break
    liczby.add(int(usr_2))  #dodajemy do zbioru kazda liczbe ktora zostala wprowadzona przez uztkonika
parzyste = set(range(0, 101, 2)) # dodajemy do pustego zbioru co drugi parzysty element
print(f"Unikalne liczby: {len(liczby)}")
print(f"Parzyste liczby z zakresu od 0-100: {len(liczby & parzyste)}")  #porwonujemy ile elementow z wpisanych przez uzyt. pasuje do parzystych elementow w drugim zbiorze

f"""
Zadanie dodatkowe
"""
print("Zadanie dodatkowe: \n")
elementy = ["aaa", "aaaaa", "aba", "aba", "aaa", "ababa"]
elementy_2 = {"aaa", "aba",  "ccc"}

print("Wspolne elementy: ", set(elementy) ^ elementy_2)
print("Unikalne elementy: ", set(elementy) & elementy_2 )


f"""
Zadanie dodatkowe 2
"""
print("Zadanie dodatkowe 2: \n")

first_set = {27, 43, 34}
second_set = {34, 93, 22, 27, 43, 53, 48}
print(first_set.issubset(second_set))   # metoda sprawdza to samo co ponizsza tylko w inej kolejnosci
print(second_set.issuperset(first_set)) # metoda sprawdza czy jeden zbior miesci sie w innym True/False, czyli czy wszystkie dane w jednym zbiorze sa w innym

f"""
sortowanie przez wybieranie (algorytm)
"""

