"""Napisz program wyliczający kwotę należną za zakupiony towar na podstawie podanej
przez użytkownika wagi i nazwy produktu. Do przechowywania informacji o cenie za
kilogram danego produktu użyj słownika. Wypisz wszystkie dostępne produkty w sklepie."""

products = {
    "ziemniaki": 3.50,
    "marchew": 10.20,
    "pomidor": 2.25,
    "cebula": 3.20,
}

stock = {
    "ziemniaki": 10,
    "marchew": 10,
    "pomidor": 10,
    "cebula": 10,
}

while True:
    comand = input("Co chcesz zrobić? [k-kyp] [z-zakończ] [m-magazyn]: ")

    if comand == "z":
        break

    elif comand == "k":
        print("Nasz sklep oferuje: ")

        for name, price in products.items():
            print(f"- {name} w cenie: {price} PLN")

        product = input("Co chcesz kupic? ")

        if product in products:
            how_much = input(f"ile chcesz kupić [{product}] kg? ")
            how_much = float(how_much)

            if how_much < stock[product]:
                print(f"Za {how_much} kg {product} zapłacisz {how_much * products[product]:.2.f}")
                stock[product] = stock[product] - how_much
            else:
                print("Nie mamy tyle produktu")

    elif comand == "m":
        product = input("Co dodajemy? ")
        how_much = int(input(f"Ile dodajemy [{product}]? "))
        stock[product] = stock.get(product, 0) + how_much

        if product not in products:
            price = float(input(f"Jaka cena za [{product}]"))
            products[product] = price
    else:
        print("Niezrozumiała komenda")
