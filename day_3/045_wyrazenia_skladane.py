
x = list(range(1, 11))
print(x)

# 1.0
szeszciany = []
for el in x:
    szeszciany.append(el ** 3)
print(szeszciany)

print([el ** 3 for el in x])

# 1.1
szeszciany2 = []
for el in x:
    if el % 2 == 0:
        szeszciany.append(el ** 3)
print(szeszciany)

###
print([[el, el ** 3] for el in x])

###
print({el ** 3 for el in x if el % 2 == 0})

###
print(tuple(el ** 3 for el in x if el % 2 == 0))