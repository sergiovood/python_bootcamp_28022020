x_user = int(input("Podaj pozycję gracza X: "))
y_user = int(input("Podaj pozycję gracza Y: "))


if x_user > 100 or y_user > 100:
    print("Pozycja gracza poza planszą. Podaj wartości w przedziale od 1 do 100")
elif x_user <= 10 and y_user <= 10:
    print("LD")
elif x_user <= 10 and y_user >= 90:
    print("LG")
elif x_user < 10 and y_user > 10 and y_user < 90:
    print("LK")
elif x_user > 10 and x_user < 90 and y_user < 10:
    print("DK")
elif x_user >= 90 and y_user <= 10:
    print("PD")
elif x_user > 90 and y_user > 10 and y_user < 90:
    print("PK")
elif x_user >= 90 and y_user >= 90:
    print("PG")
elif x_user > 10 and x_user < 90 and y_user > 90:
    print("GK")
else:
    print("Centrum")