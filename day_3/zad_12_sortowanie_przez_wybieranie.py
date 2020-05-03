lista = [9,1,6,8,4,3,2,0]

for indeks_podstawienie in range(len(lista)):
    indeks_min_wartosci = indeks_podstawienie
    for index_ogona in range(indeks_podstawienie + 1, len(lista)):
        if lista[index_ogona] < lista[indeks_min_wartosci]:
            indeks_min_wartosci = index_ogona

    lista[indeks_podstawienie], lista[indeks_min_wartosci] = lista[indeks_min_wartosci], lista[indeks_podstawienie]

print(lista)


assert lista == [0,1,2,3,4,6,8,9]