# tupla() , krotka
# jest to typ niemutowalny - nie można edytować jak w przypadku listy

x = (1, 2, 3, 10, 12, "ala", "mmm", 2.0)
#    0  1  2   3   4    5       6   7    kolejnosc elementow

print(x)
print(type(x))
print(dir(x))

print(x.index("ala"))  # jaki index ma w tupli slowo - ala / czyli na 5 miejscu

print("-" * 30)
if 'xxxx' in x:  # sprawdzamy czy jest xxxx w typli, jesli tak to
    print(x.index('xxxx'))  # wyswietli pod jakiem indeksem
else:
    print("nie ma takiego elementu")
print("-" * 30)

print(len(x))  # zwroci ilosc elementow w tupli / czyli 8 / liczyc zaczyna od 1 a nie od 0 jak w przypadku indeksu
print(len("Ala"))  # zwroci dlugosc slowa / czyli 3
print(x.count(12))  # policze ile wystopien cyfry 12 jest w tupli/ czyli 1 - jedno wystapienie

print("b" in "Olaf") # sprawdzi czy literka b jest w slowie / wynik: False
print(3 in x) # sprawdzi czy numer 3 jest w tupli / wynik True

# Slicing - obcinanie tupli
#kazde obcinanie to nowa tupla ktora mozna przypisac do zmiennej
y = "ala ma kota kot ma ale"
print(x[0]) # wyswietli 0 (czyli pierwszy) element w indeksie
print(x[-3]) # wyswietli od konca 3 element w indeksie
print(x[0:6]) # od poczatku do 6
print(x[:6]) # od poczatku do 6

print(x[::2]) # od poczatku dokonca co 2 element
print(y[::-1]) # odwrocone wyswietlanie wszystkich elementow napisu

print("-"*30)

#FUNKCJA tuple()
#zamienia na czynniki pierwsze to co w nią pomieszczamy

#Przyklady:

#typ str()
print(tuple("Tekst"))
#typ int() przrobic na str biorac w ""
print(tuple("12345")) # jesli tego nie zrobimy to dostaniemy blad

x = tuple()
x = ()
print(type(x)) # wyswietli typ tuples()

x = (1) # to nie jest tupla, zeby to zostalo tupla musi byc przecinek po 1 / czyli 1,
print(type(x)) # wyswietli typ int

x = (1, ) # to jest już tupla
print(type(x))

x = ("ala"
     "ma"
     "kota")
print(type(x)) #wyswietli typ str

x = ("ala",
     "ma",
     "kota")
print(type(x)) # to już będzie tupla bo w środku nawiasów jest przecinek ( , )

print("-"*30)

#Włączenia tupli, dodawac do siebie
x = (1, 2)
y = (3, 4)
print(f"wlaczona tupla z dwoch roznych {x + y}")  # jest to nowa tupla ze swoim id

