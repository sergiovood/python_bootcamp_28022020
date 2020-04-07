x_user = int(input("Podaj pozycję gracza X: "))
y_user = int(input("Podaj pozycję gracza Y: "))

poz = "Pozycja gracza:"

if x_user > 100 or y_user > 100:
    print("Pozycja gracza poza planszą. Podaj wartości w przedziale od 1 do 100")
elif x_user <= 10 and y_user <= 10:
    print(poz, "Lewy dolny róg")
elif x_user <= 10 and y_user >= 90:
    print(poz, "Lewy górny róg")
elif x_user < 10 and y_user > 10 and y_user < 90:
    print(poz, "Lewa krawędź")
elif x_user > 10 and x_user < 90 and y_user < 10:
    print(poz, "Dolna krawędź")
elif x_user >= 90 and y_user <= 10:
    print(poz, "Prawy dolny róg")
elif x_user > 90 and y_user > 10 and y_user < 90:
    print(poz, "Prawa krawędź")
elif x_user >= 90 and y_user >= 90:
    print(poz, "Prawy górny róg")
elif x_user > 10 and x_user < 90 and y_user > 90:
    print(poz, "Górna krawędź")
else:
    print(poz, "Centrum")