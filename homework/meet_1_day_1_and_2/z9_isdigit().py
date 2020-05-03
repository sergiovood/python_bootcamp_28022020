usr_txt = input("Podaj dowolną liczbę:")

num_list = ["zero", "jeden", "dwa", "trzy", "cztery", "pięć", "sześć", "siedem", "osiem", "dziewięć"]

out = []
for znak in usr_txt:
    if znak.isdigit(): # metoda isdigit() zwroci prawde kiedy w tekscie znajdzie symbol 0,1,2,3,4....
        out.append(num_list[int(znak)])  # dodajemy do pustej listy out tekstowy warian cyfr, podstawiajac indeksy cyfr z listy num_list
print(" ".join(out))    # właczymy napisy razem z listy out i dodajemy spacje


print(dir("1"))
print(help("tekst".isdigit)) # nie podawac nawiasow na koncu () czyli ma byc same isdigit, bez nawiasow poprawnie nam wyswietla co ta metoda robi

print(help(print()))

print(1, 2, sep=";", end=";")
print(3, 4, sep=";")