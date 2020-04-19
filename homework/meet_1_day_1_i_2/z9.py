# usr_txt = int(input("Podaj dowolną liczbę:"))
lista = "ala ma 123"
# lista.append(usr_txt)
num_list = ["zero", "jeden", "dwa", "trzy", "cztery", "pięć", "sześć", "siedem", "osiem", "dziewięć"]
i = 0

lista_2 = [9, 1, 1]

for x in lista_2:
    index = x
    for y in num_list[index]:
        print(y, end="")

tekst = "ala ma 123"
out = []
for znak in tekst:
    if znak.isdigit():
        out.append(num_list[int(znak)])
print(out)
print(" ".join(out))

print(help(print()))
print(1, 2, sep=";", end=";")
print(3, 4, sep=";")