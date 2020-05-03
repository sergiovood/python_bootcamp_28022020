n = float(input("Podaj liczbe lat do obliczenia: "))
spk = float(input("Podaj stan początkowy konta: "))
p = float(input("Jaka stopa opreconatowania: "))


v = spk * ((n + ((p/100) / 1)) ** 2)
print(f"{v:.3f}")
