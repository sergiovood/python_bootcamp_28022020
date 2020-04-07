min_x = None
max_x = None

while True:
    user_num = input("Podaj liczbę: ")
    if user_num == "wprowadz x zeby zakonczyc": # jesli uzytkownik wprowadzil x to konczymy wprowadzania liczb
        break
    user_num = int(user_num)

    if min_x is None or user_num < min_x:
        min_x = user_num

    if max_x is None or user_num > max_x:
        max_x = user_num
print(f"Wartość maksymalna: {max_x}")
print(f"Wartość minimalna: {min_x}")
