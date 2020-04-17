days = 7  # 7 dni w tygodniu
all_temp = 0  # ustawiamy na poczatek liczbe 0 zeby byla poprostu liczba do ktorej bedziemy dodawac +1

while days > 0:  # dopuki days jest wiekszy od 0 to zadziala poniszy kod
    t = int(input("Podaj temperature: "))  # uzytkownik wprowadza srednia temperatury
    all_temp += t  # dodajemy  do zmiennej all_temp temperature ktora wprowadzil uzytkownik, sumujemy w tej zmienej wszystkie temperatury
    days -= 1  # potem zabieramy jeden dzien

print(f"Srednia {all_temp / 7:.2f}") #na koncu dzielimy zebrane temperatury na 7 dni tym samym wyliczajac srednia
