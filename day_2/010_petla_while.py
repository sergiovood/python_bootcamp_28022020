"""
pentla while dziala w kolko poki jest prawda
"""
x = 10
while x > 0:
    print(x)  # bedzie wyswietlac najpierw 10 potem 9 az do 1
    # x = x - 1 - to samo co niżej
    x -= 1  # odejmuje od pocztkowego znaczenia czyli 10 po jednej liczbie, skonczysie jak dojdzie do zakonczenia pentli

print("=" * 40)
# wyswietli to samo co pozywzej ale  inaczej zapisane za pomoca warunka
s = 10
while True:  # True - w pentle while podajemy wtedy jesli nie wiemy ile obrotow ma dzialac pentla
    print(s)
    s -= 1
    if s == 0:  # w srodek wkladamy warunek jaki cos sprawdzi i przerwie nasza pentle
        break  # przerywnik, konczy petle

print("=" * 40)

i = 10
while True:
    if i == 6: # sprawdzamy czy i jest 6, zeby ja usunac z pentli
        i -= 1 # jesli tak to odejmujemy znaczenie
        continue  # przechodzi poprostu dalej do wykonania pentli po zakonczeniu warunku
    print(i) # wyswietla kazde znaczenia i podczas dzialania pentli while
    i -= 1
    if i == 0:
        break #konczy pentle
