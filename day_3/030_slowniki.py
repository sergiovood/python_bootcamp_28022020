# pol_ang = dict()  # dict - to slownik
print(dict()) #zwruci {} - co oznacza slownik
pol_ang = {"kot": "cat",  # pisania w nawiasach tez oznaczaja slownik bez wylowania funk. dict()
           "ptak": "bird"
           }
pol_ang["pies"] = "dog"  # pies to kluch, a dog to jego wartosc, dodajemy kolejne warosci do slownika pol_ang
pol_ang["kot"] = "kitty" # nadpisze(zamieni) wartosc kot:cat na kot:kitty
print(pol_ang)

dict_2 = dict(a=10, b=22, c=33)  # 2 wersja zapisania slownika, a - jest kluczem, 10 jest jego wartoscia
print(dict_2)

dict_3 = dict([  #slownik ktory zawiera listy
    ["x", "ala"],
    ["y", "kot"]
])

print(dir(dict_3))   #zwroci wszystkie matody dla slownika
print(dict_3.keys())  # zwroci wszystkie kluczy
print(dict_3.values())  # zwroci wszystkie wartosci
print(dict_3.items())  # zwroci wszystkie pary, ktore beda tuplami

print(dict_3.get("x"))  # metoda .get, pobiera wartosc dla klucza x
print(dict_3.get("z", "Brak"))  # jesli niema takiego klucza w slowniku to zwroci None ale w naszym przypadku zamienilismy slowo None na Brak

if 'z' in dict_3:  # jest to samo co metoda .get powyzej, tylko obchodzimy wyswietlenia bledu, jesli szukamy klucz jakiego nie ma w slowniku
                    # jesli chcemy szukac w wartosciach a nie w kluczach to zapis bedzie: if 'z' in dict_3.values():
    print(dict_3["z"])
else:
    print("brak")
