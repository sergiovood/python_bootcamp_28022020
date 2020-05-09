# 1. Tuple (), Listy [], Slowniki dict(), Zbiory set()
# 2. Tuple, zbiory - nie mutowalne | Listy, Slowniki - mutowalne
# 3.
collection = [9,1,6,8,4,3,2,0]
for index_replace in range(len(collection)):
    index_min = index_replace
    for index_tail in range(index_replace + 1, len(collection)):
        if collection[index_tail] < collection[index_min]:
            indeks_min_wartosci = index_tail
    collection[index_replace], collection[index_min] = collection[index_min], collection[index_replace]
print(collection)

# 4
zrodla = {"a": 10, "b":30}
podana_liczba = 10
if podana_liczba in zrodla.values():
    value = podana_liczba
    print(value)
else:
    print("nie istnieje")

# 5
def foo(*args, **kwargs):
    for pozycyjne in args:
        return pozycyjne
    for kluczowe in kwargs:
        return kluczowe


foo(10, 20, a=1, b=2, c=3)
print(pozycyjne, kluczowe)

