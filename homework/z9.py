# usr_txt = int(input("Podaj dowolną liczbę:"))
lista = [9, 1, 1]
# lista.append(usr_txt)
num_list = ["zero", "jeden", "dwa", "trzy", "cztery", "pięć", "sześć", "siedem", "osiem", "dziewięć"]
i = 0

for x in lista:
    index = x
    for y in num_list[index]:
        print(y)
