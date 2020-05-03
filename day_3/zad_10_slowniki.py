f"""
Napisz program zliczający liczbę wystąpien kazdego znaku w podanym przez uzytkownika napisie.
"""


usr_txt = input("Podaj tekst: ")
counts = dict()

for sign in usr_txt:
    if sign in counts:
        counts[sign] = counts[sign] + 1
    else:
        counts[sign] = 1
print(counts)

##################

for sign in usr_txt:
    counts[sign] = counts.get(sign, 0) + 1
print(counts)

###################

for sign in usr_txt:
    counts[sign] = usr_txt.count(sign)  # metoda .count ktora policzy ilosc wybranych znakow i zwroci wartosci
print(counts)

##############

from collections import defaultdict

counts = defaultdict(int)   # defaultdict pozwala na przekazanie jakiejs funkcji ktora ma wartosc poczatkowa,
                            # w naszym przypadku bedzie to int ktory na poczatku zwraca 0
for sign in usr_txt:        # wyszedl najmniejszy kod ze wszystkicj
    counts[sign] += 1

print("___:", counts)