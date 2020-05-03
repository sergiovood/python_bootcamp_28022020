# w zbiorze elementy sa nieuporzadkowane, nie ma porzadku w zbiorze
# nie ma indeksow
# dodawanie nowych elementow do zbioru nie wplywa na kolejnosc, algorytm pythona sam wyznacza gdzie bedzie umieszczony nowy element
# mozemy tylko sprawdzic czy cos jest w zbiorze czy nie
# w zbiorze  oraz w slowniku czas dostepu do elementu jest staly, algorytm wie gdzie znajduje sie element. A w przypadku np. listy, algorytm idzie pokolei do poki nie znajdzie wlasciwy element

# jesli operujemy na zbiorach to nas interesuje np.: czy jest w zbiorze, jaka jest czesc wpolna zbiorow, jaka roznica zbiorow i tego typu operacje
# zbiory nie nadaja sie dla operacji jesli trzeba przejsc po kolei, gdzie ta kolei jest wazna. mozemy przejsc przez wszystkie elementy zbiory ale kolejnosc w uzytecznym sensie w zbiorze nie istnieje
#zbiory mozna wykorzystac do usuniecia dublikatow z listy,bo w zbiorach nie moze byc dublikatow tylko unikalne znaczenia zmienna = set(lista[])

collection = set()  #  jest to pusty zbiur, tak samo wyswietla sie {} jak slownik, tylko tutaj nie ma klucza tylko znaczneie
print(dir(collection))

collection.add("x")  # dodajemy do zbioru elementy
collection.add(1)
print("====", collection)  # wyswietli 1, x - chociaz dodawanie do zbioru bylo w inej kolejnosci, czyli to potwierdza ze niema kolejnosci w zbiorze

for el in collection:  # moezemy sprawdzic czy element jest w zbiorze
    print("||", el)


a = {1, 2, 3}  # dwa zbiory ktore maja 2 i 3 podobne ze soba, 1 i 4 rozne, unikalne elementy
b = {2, 3, 4}

print(a)
print(b)

print("suma : ", a | b)  #  |(znak pipe) - zwraca nowy zbiur z polaczonych dwoch podanych i ich wszystkich elementow bez powtorzenia podobnych

print("różnica: ", a - b)  # roznica, podobne elementy zostana odjente, czyli zostanie tylko 1 (pamietac ze a-b nie jest to samo co b-a)

print("różnica semetryczna: ", a ^ b)  # roznica semytryczna, to elementy ktore rozniow sie w zbiorach, czyli 1 i 4

print("iloczyn(podobienstwo): ", a & b)  # &(ampersant) - operator iloczynu, elementy ktore podobne w porownywalnych zbiorach

print("funkcja pop zwroci: ", a.pop())  # zwraca jakis element ze zbioru i usunie go, w naszym przypadku zwrocil 1 element, ale nie jest to regula
print("zostanie w zbuiorze po usunueciu przez metode .pop: ", a)

print(help(set.issubset)) # to samo co nizej tylko w inej koljnosci sprawdza
print(help(set.issuperset)) # metoda sprawdza czy jeden zbior miesci sie w innym True/False, czyli czy wszystkie dane w jednym zbiorze sa w innym
#|S1.issubset(S2)            |S1 <= S2    |czy S1 jest zawarty w S2|
#|S1.issuperset(S2)          |S1 >= S2    |czy S1 zawiera S2       |
# wiecej o metodach dla zbiorow: http://users.uj.edu.pl/~ufkapano/algorytmy/lekcja02/set.html
