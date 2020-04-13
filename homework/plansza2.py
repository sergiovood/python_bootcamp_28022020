x_user = int(input("Podaj pozycję gracza X: "))
y_user = int(input("Podaj pozycję gracza Y: "))

pos = "Gracz znajduje się"

if x_user > 100 or x_user < 0 or y_user > 100 or y_user < 0:  # sprawdzenie wprowadzonych danych
    print("Pozycja gracza poza planszą. Podaj wartości w przedziale od 0 do 100")
elif x_user <= 10 and y_user <= 100:  # sprawdzenie lewych rogów oraz krawedzi
    if y_user <= 10:
        print(pos, "w lewym dolnym rogu")
    elif y_user >= 90:
        print(pos, "w lewym górnym rogu")
    else:
        print(pos, "na lewej krawędzi")
elif x_user >= 90 and y_user <= 100:  # sprawdzenie prawych rogów oraz krawedzi
    if y_user <= 10:
        print(pos, "w prawy dolnym rogu")
    elif y_user >= 90:
        print(pos, "w prawym górnym rogu")
    else:
        print(pos, "na prawa krawędzi")
elif x_user > 10 and x_user < 90:  # sprawdzenie odstepow od krawedzi
    if y_user > 90:  # sprawdzenie gornej krawedzi
        print(pos, "w górnej krawędzi")
    else:
        print(pos, "na dolnej krawędzi")  # jesli FALSE to dolna krawedz
else:
    print(pos, "w centrum")  # jesli wszystko nie to centrum
