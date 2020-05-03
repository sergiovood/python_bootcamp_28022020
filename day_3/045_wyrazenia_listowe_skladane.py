x = list(range(1, 11))
print(x)
# 1.0
szeszciany = []
for el in x:
    szeszciany.append(el ** 3)
print("szeszcian 1.0: ", szeszciany)

# ten sam zapis co wyzej ale mniej kodu, i dodatko bedzie szybciej dzialajace w kodzie
print("wyrazenie skladane 1.0: ", [el ** 3 for el in x])

# 1.1 tylko parzyste liczby
szeszciany2 = []
for el in x:
    if el % 2 == 0:
        szeszciany2.append(el ** 3)
print("szeszcian 1.1: ", szeszciany2)
print("wyrazenie skladane 1.1: ", [el ** 3 for el in x if el % 2 == 0])
print("wyrazenie skladane - zbior: ", {el ** 3 for el in x if el % 2 == 0})
print("wyrazenie skladane - slownik: ", {el: el ** 3 for el in x if el % 2 == 0})
print("wyrazenie skladane - tupla: ", tuple(el ** 3 for el in x if el % 2 == 0))
print("wyrazenie skladane - lista, list: ", [[el, el ** 3] for el in x])


