collection = set()

while True:
    usr_value = input("Podaj liczbe lub k by zakończyć: ")
    if usr_value == "k":
        print("Koniec programu")
        break
    collection.add(int(usr_value))

even_numb = set(range(0, 101, 2))  # liczby parzyste

print(f"Unikalnych liczb: {len(collection)}")
print(f"Parzystych z zakresu 1-100: {len(collection & even_numb)}")