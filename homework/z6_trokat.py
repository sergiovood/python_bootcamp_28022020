usr_value = int(input("Podaj liczbę: "))

if usr_value > 0:
    for triangle in range(1, (usr_value + 1)):
        print(triangle * "*")
else:
    print("Błąd: Podaj liczbę większą od 0")

