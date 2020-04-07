x_user = int(input("Podaj pozycję gracza X: "))
y_user = int(input("Podaj pozycję gracza Y: "))

pos = "Pozycja gracza:"

if x_user > 100 or y_user > 100:
    print("Pozycja gracza poza planszą. Podaj wartości w przedziale od 1 do 100")
elif x_user <= 10 and y_user <= 10:
    print(pos, "Lewy dolny róg")
elif x_user <= 10 and y_user >= 90:
    print(pos, "Lewy górny róg")
elif x_user < 10 and y_user > 10 and y_user < 90:
    print(pos, "Lewa krawędź")
elif x_user > 10 and x_user < 90 and y_user < 10:
    print(pos, "Dolna krawędź")
elif x_user >= 90 and y_user <= 10:
    print(pos, "Prawy dolny róg")
elif x_user > 90 and y_user > 10 and y_user < 90:
    print(pos, "Prawa krawędź")
elif x_user >= 90 and y_user >= 90:
    print(pos, "Prawy górny róg")
elif x_user > 10 and x_user < 90 and y_user > 90:
    print(pos, "Górna krawędź")
else:
    print(pos, "Centrum")