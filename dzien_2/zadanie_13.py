days = 7  # 7 dni w tygodniu
temp = 0  # ustawiamy na poczatek liczbe 0 zeby byla poprostu liczba do ktorej bedziemy dodawac +1

while days > 0:  # dopuki days jest wiekszy od 0 to zadziala poniszy kod
    t = int(input("Podaj temperature: "))  # uzytkownik wprowadza srednia temperatury
    temp += t  # dodajemy  +1
    days = days - 1  # potem zabieramy jeden dzien

print(f"Srednia {temp / 7}")
