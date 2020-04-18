min_x = None
# Python posiada specjalny obiekt/wartość None,
# która oznacza obiekt pusty (null object). Często w Pythonie zmiennej
# nadajemy wartość None, aby zaznaczyć, że jest ona dostępna,
# ale chwilowo traktujemy ją jako nieokreśloną.
max_x = None
user_end = "x"
while True:
    user_num = input("Podaj liczbę: ")

    if user_num == user_end:  # jesli uzytkownik wprowadzil x to konczymy wprowadzania liczb
        break
    user_num = int(user_num)
    print("wprowadz x zeby zakonczyc")

    if min_x is None or user_num < min_x: # z kazda wprowadzona liczba idzie sprawdzenie w tle
                                        # czy liczba uzytkownika jest mniejsza od poprzednie,
                                        # jesli tak to przepiszemy na nowo liczbe minimalną
        min_x = user_num # zapisuje liczbe minimalna

    if max_x is None or user_num > max_x: # w tego warunku zadanie to same co z liczba
                                        # minimalna tylko tutaj sprawdzamy i zapisujemy liczbe maksymalna
        max_x = user_num

print(f"Wartość maksymalna: {max_x}")
print(f"Wartość minimalna: {min_x}")
