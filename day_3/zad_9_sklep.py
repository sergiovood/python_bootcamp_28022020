"""Napisz program wyliczający kwotę należną za zakupiony towar na podstawie podanej
przez użytkownika wagi i nazwy produktu. Do przechowywania informacji o cenie za
kilogram danego produktu użyj słownika. Wypisz wszystkie dostępne produkty w sklepie."""

# slownik produktow w sklepie
products = {
    "ziemniaki": 3.50,
    "marchew": 10.20,
    "pomidor": 2.25,
    "cebula": 3.20
}

#slownik ilosci kg danego produktu
stock = {
    "ziemniaki": 10,
    "marchew": 10,
    "pomidor": 10,
    "cebula": 10
}

while True:  #zapetlenie pytania z roznymi wariantamy odpowiedzi dla uzytkownika
    comand = input("Co chcesz zrobić? [k-kyp] [z-zakończ] [m-magazyn]: ")

    if comand == "z":
        break

    elif comand == "k":
        print("Nasz sklep oferuje: ")

        for name, price in products.items():  # tworzymy dzie zmienne gdzie bedzie klucz (nazwa produktu) i wartosc klucza (cena produktu) | a,b = keys, values
            print(f"- {name} w cenie: {price} PLN")  # wyswietlamy wszystkie produkty w sklepie

        product = input("Co chcesz kupic? ")  # pytamy jaki produkt wybiera uzytkownik, wpisujac

        if product in products:  # jesli wpisany produkt jest na w naszym slowniku, sprawdzenie po kluczu, czyli po nazwie produktu
            how_much = float(input(f"ile chcesz kupić [{product}] kg? "))

            if how_much < stock[product]:  # sprawdzamy czy mamy wystarczajaco kilogram w sklepie w porownaniu do tego co wpisal uzytkownik
                print(f"Za {how_much} kg {product} zapłacisz {how_much * products[product]:.2f}")  # wyswietlamu jaka sume ma zaplacic uzytkownik za wybrany produkt okragliajac do 2 liczb po przecinku
                stock[product] -= how_much  # pomniejszamy nasz magazyn o ilosc kilogram ktory kupil uzytkownik
            else:
                print("Nie mamy tyle produktu")

    elif comand == "m":  # dodajemy do naszego magazynu nowe produkty
        product = input("Co dodajemy? ")   # uzytkownik wpisuje produkt ktore chce dodac
        how_much = int(input(f"Ile dodajemy [{product}]? "))  #jaka ilosc dodaje do magazynu
        stock[product] = stock.get(product, 0) + how_much  # dodajemy do slownika magazynu nowy produkt stock[product] i ustawiamy dla niego ilosc tego produktu

        if product not in products:  # sprawdzamy czy na naszej liscie jest takie produkt jesli nie to
            price = float(input(f"Jaka cena za [{product}]"))  # pobieramy cene od uzytkownika dla nowego produktu za kg
            products[product] = price # i dodajemy nowy produkt do slownika products[product] - klucz,  i przypisujemy dla niego nowa cene od uzytkownika
    else:
        print("Niezrozumiała komenda")
