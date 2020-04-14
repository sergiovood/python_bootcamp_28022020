# Napisy
import n1 as n1

str()
'Ala "ma" kota'
"Ala \"ma\" kota"

# Laczenie napisow - konkatenacja
n1 = "Ala(n1)"
n2 = "kot(n2)"

print(n1 + " " + n2)
print("-" * 30)  # mnozenie stringow(tekstow), pomaga formatowac tekst

print(f"{n1} {n2}")  # f-string - najszybszy sposob formatowania napisow w którym wpisujemy zmienne do wyswietlania
print("-" * 10 + "Jesli nie ma mozliwosci skorzystac f-stringa to korzystamy z funkcji .format")

# Jesli nie ma mozliwosci skorzystac f-stringa to korzystamy z funkcji .format
print("{} {}".format(n1, n2))  # .format - funkcja do wyswitlania napisow
print("{} {}".format(n2, n1))  # tutaj wazna kolejnosc podawanych zmiennych zeby poprawnie wyzwietlicz zdanie
print("{a} {b}".format(b=n2,
                       a=n1))  # tutaj kolejnosc wywolania zmiennych w funkcji .format nie jest wazna bo są juz podana kolejnosc w {}
print("-" * 10 + "Starszy kod ma jeszcze takie metody wlaczenia napisow")

# Starszy kod ma jeszcze takie metody wlaczenia napisow
print("%s %s" % (n1, n2))
print("-" * 10 + "Formatowanie dodatkowe")

# Formatowanie dodatkowe
print(
    f"{n1:10} {n2:20}")  # mowimy jaka szerokosc ma miec zmienna :10 czy :20, zaczyna liczyc od 0(zera) czyli bedzie szerokosc 11 oraz 21
print(f"{n1:>10} {n2:^20}")  # możemy zadac wyrownanie np do prawej strony ">", do lewej "<", centrowanie "^"
print("{:>10} {:^20}".format(n1, n2))  # to samo co powyzej ale inne formatowanie
print("-" * 10 + "Formatowanie matematyczne")

# Formatowanie matematyczne
x = 10 / 3
print(f"{x:.2f}")
print(f"{x:.4f}")
print("-" * 30)

print("1\n2\n3\n") # - \n oznacza z nowej linii


# Operacje na napisach
napis = "Ala Ma kota"
x = napis.lower()  # male literki
y = napis.upper()  # duze literki
z = napis.title  # kazde slowo z duzej literki
print(x, y)

print(dir(napis))  # wyswietli wszystkie mozliwe metody do wykorzystania z tym typem danych, w naszym przypadku str
print("-" * 30)

print(help(napis.lower))  # wyswietli info co dana metoda zrobi z naszym typem danych
print("-" * 30)


