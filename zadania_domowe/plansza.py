t = "t"
while t == "t":
    x_user = int(input("Podaj pozycję gracza X: "))
    y_user = int(input("Podaj pozycję gracza Y: "))

    pos = "Gracz znajduje się"

    if x_user > 100 or x_user < 0 or y_user > 100 or y_user < 0:
        print("Pozycja gracza poza planszą. Podaj wartości w przedziale od 0 do 100")
    elif x_user <= 10 and y_user <= 10:
        print(pos, "w lewym dolnym rogu")
    elif x_user <= 10 and y_user >= 90:
        print(pos, "w lewym górnym rogu")
    elif x_user >= 90 and y_user >= 90:
        print(pos, "w prawym górnym rogu")
    elif x_user >= 90 and y_user <= 10:
        print(pos, "w prawy dolnym rogu")
    elif x_user < 10 and y_user > 10 and y_user < 90:
        print(pos, "na lewej krawędzi")
    elif x_user > 10 and x_user < 90 and y_user < 10:
        print(pos, "na dolnej krawędzi")
    elif x_user > 90 and y_user > 10 and y_user < 90:
        print(pos, "na prawa krawędzi")
    elif x_user > 10 and x_user < 90 and y_user > 90:
        print(pos, "w górnej krawędzi")
    else:
        print(pos, "w centrum")
    t = input("Podac liczby jeszcze raz (t/n)? ")
print("Koniec")
