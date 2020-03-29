# Napisy
import n1 as n1

str()
'Ala "ma" kota'
"Ala \"ma\" kota"

print("1\n2\n3\n")

print(f"{n1} {n2}")
print("{} {}".format(n1, n2))
print("{} {}".format(n2, n1))
print("{a} {b}".format(b=n2, a=n1))

print("%s %s" % (n1, n2))

print(f"{n1:>10} {n2:^20}")
x = 10 / 3

napis = "Ala Ma kota"

first_name = "JAN"
last_name = "KoWalski"
b_year = 1950
profession = "Hydraulik"

result = ""

expected = f"""
imie i nazwisko: {first_name.capitalize()} {last_name.capitalize()}Jan Kowalski
=============================
rok urodzenia:      {b_year}
zawód:              {profession.lower()}
"""

assert result == expected
