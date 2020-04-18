# pol_ang = dict()  # dict - to slownik
pol_ang = {"kot": "cat",  # pisania w nawiasach tez oznaczaja slownik bez wylowania fiunk. dict()
           "ptak": "bird"
           }
pol_ang["pies"] = "dog"  # pies to kluch, a dog to jego wartosc
pol_ang["kot"] = "kitty"
print(pol_ang)

dict_2 = dict(a=10, b=22, c=33)  # 2 wersja zapisania slownika, a - jest kluczem, 10 jest jego wartoscia
print(dict_2)

dict_3 = dict([
    ["x", "ala"],
    ["y", "kot"]
])

print(dir(dict_3))
print(dict_3.keys())  # zwroci wszystkie kluczy
print(dict_3.values())  # zwroci wszystkie wartosci
print(dict_3.items())  # zwroci wszystkie pary, ktore beda tuplami

print(dict_3.get("x"))  # pobiera po kluczu
print(dict_3.get("z", "brak"))  # jesli niema to zwroci None

if 'z' in dict_3:  # jest to samo co get tylko obchodzimy wyswietlenia bledu, jesli szukamy cos czego niema w slowniku
    print(dict_3["z"])
else:
    print("brak")
