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