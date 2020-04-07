#krotka, tupla
#jest to typ niemutowalny - nie można edytować jak w przypadku listy

x = (1, 2, 3, 10, 12, "ala", "mmm", 2.0)
#    0  1  2   3   4    5       6   7    kolejnosc lementow

print(x)
print(type(x))
print(dir(x))

print(x.index("ala"))
if 'xxxx' in x:
    print(x.index('xxxx'))

print(len(x))
print(len("Ala"))
print(x.count(12))

print("b" in "Olaf")
print(3 in x)

y = "ala ma kota kot ma ale"
print(x[0])
print(x[-3])
print(x[0:6])
print(x[:6])

print(x[::2])
print(y[::-1])