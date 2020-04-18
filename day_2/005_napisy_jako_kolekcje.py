# NAPISY

napis = "Koronawirus"
#        012345678910.. - indeksy liter
#             ...-2-1
print(dir(napis))  # wyswietla funkcje do wykorzystania

print(napis.index("K"))  # wyswietli indeks danej literki czyli 0 / wielkosc litery ma znaczenie
print(napis.index("o"))  # indeks 1 literki o / zostanie zwrucone pierwsze wystapienie, a mamy ich dwie
print(napis.rindex("o"))  # indeks 3 literki o / rindex liczy z drugiej strony i nie podaje ujemnej liczby

print(napis[0])  # wyswietli literke K
print(napis[4])  # literka n
print(napis[10])  # wynik literka - s

print(napis[-1])  # liczy z konca, tez wynik - s
print(napis[-3])  # liczy z konca, wynik - r

# Slice - wycinki z list
print(napis[3:7])  # wycinek napisu - od o do w / 7 juz nie wchodzi, czyli wyswietli 4 znaki

