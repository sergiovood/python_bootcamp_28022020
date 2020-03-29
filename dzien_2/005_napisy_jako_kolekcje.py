napis = "Koronawirus"
#        012345... - indeksy liter

print(dir(napis)) # wyswietla funkcje do wykorzystania
print(napis.index("K"))
print(napis.rindex("o"))
print(napis[0])
print(napis[4])
print(napis[10]) # wynik literka - s

print(napis[-1]) #liczy w drugą strone tez wynik - s

print(napis[3:7]) #wycinek napisu - od o do w



inp_user = int(input("Podaj Liczbę: "))

a = inp_user > 10
b = inp_user <= 15
c = inp_user % 2

print(a)
print(b)
print(c)