t = "t"
while t == "t":
    x_user = int(input("Podaj pozycję gracza X: "))
    y_user = int(input("Podaj pozycję gracza Y: "))

    pos = "Gracz znajduje się"
    res = ""
    if x_user > 100 or x_user < 0 or y_user > 100 or y_user < 0:
        res = "poza planszą. Podaj wartości w przedziale od 0 do 100"
    elif x_user <= 10 and y_user <= 10:
        res = "w lewym dolnym rogu"
    elif x_user <= 10 and y_user >= 90:
        res = "w lewym górnym rogu"
    elif x_user >= 90 and y_user >= 90:
        res = "w prawym górnym rogu"
    elif x_user >= 90 and y_user <= 10:
        res = "w prawy dolnym rogu"
    elif x_user < 10:
        res = "na lewej krawędzi"
    elif y_user < 10:
        res = "na dolnej krawędzi"
    elif x_user > 90:
        res = "na prawej krawędzi"
    elif y_user > 90:
        res = "w górnej krawędzi"
    else:
        res = "w centrum"
    print(pos, res)
    t = input("Podac liczby jeszcze raz (t/n)? ")
print("Koniec")
