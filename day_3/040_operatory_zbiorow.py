# w zbiorze elementy sa nieuporzadkowane, nie ma porzadku w zbiorze
# nie ma indeksow
# mozemy sprawdzic czy cos jest w zbiorze czy nie

collection = set()
print(dir(collection))

a = {1, 2, 3}
b = {2, 3, 4}

print("suma: ", a | b) #zwraca nowy zbiur, polaczenie poprzednich (suma)

print(a)
print(b)

print("podobienstwo w zbiorach: ", a & b) # iloczyn, &- operator iloczynu, elementy ktore podobne w porownywalnych zbiorach

print("różnica: ", a - b) # roznica

print("różnica semetryczna: ", a ^ b) # roznica semytryczna, alementy ktore rozniowsie w zbiorach

print("funkcja pop zwroci: ", a.pop()) # zwraca jakis element ze zbioru i usunie jego
print(a)
