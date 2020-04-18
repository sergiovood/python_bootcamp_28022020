""" #wiekszy komentarz
if <warunek>:
    <blok kodu>
elif <warunek 2>:
    <blok kodu>
elif <warunek 3>:
    <blok kodu>
else:
    <blok kodu>
"""

x = 6

if x > 10:  # ten warunek nie spewniony wykorzystujac liczbe 7
    print("Większy")
    print("!!!")  # w bloku kodu moze byc duzo linii kodu
elif x % 3 == 0:  # ten jest spewniony, a znaczy ze przejdzie nizej do wyswietlenie
    print("Parzysty")
    """wyswietli oraz przejdzie na sam koniec pomijajac inne warunki, 
                            bo instrukcja konczy pracy jesli jeden z warunkow jest prawda"""
elif x % 2 == 0:
    print("Nie parzysty")
else:
    print("Żaden z warunków nie został spewniony")
print("Koniec")  # wyswietli po tym jak sie spewni jakis warunek lub zaden

# Inne zapisy warunka if
# Mozliwosc pisania dowolno ilosc tylko samych if bez else czy elif,
# jesli potrzebujemy zeby kilka warunkow podzad zostawy wykonany patz. zad_14_sprawdzenie_liczb_min_i_max.py
x = 10
y = 20
if x == 0:
    print("x rowna sie zero")
if y == 2:
    print("y rowna sie 2")

# Zagnieżdżone warunky
# czasami przydają się, ale lepiej unikać żeby kod był bardziej czytelny jesli taka mozliwosc.
# wartosci w przykladzie nic nie oznaczaja, pokazany tylko schemat
if x + y >= 100:
    if x < 20:
        print("x mniejsze od 20")
    elif y > 20:
        print("y wieksze od 20")
    else:
        print("wyswietli ten napis")
else:
    print("Koniec warunku")