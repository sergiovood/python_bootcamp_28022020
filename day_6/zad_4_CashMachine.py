f"""
Zaimplementuj w klasie CashMachine rzucanie wyjątków w następujących przypadkach:
􏰀 brak miejsca na banknoty (ustal limit banknotów w bankomacie)
􏰀 zła wartość wypłacanej sumy (musi być podzielna przez 10) 􏰀 brak odpowiednich banknotów w bankomacie
Zaimplementuj prosty interfejs tekstowy do klasy bankomat obsługujący wszystkie wyjątki. Obsłuż także wyjątki wynikające z podania złych danych przez użytkownika.
Przykład użycia:
Podaj typ operacji: WYPŁATA
Podaj kwotę do wypłacenia: 150
BŁĄD: brak wystarczającej liczby banknotów dla kwoty 150!
"""

#sciagnac kod z repo Rafala
while True:
    operation = input("Podaj typ operacji: [wplata, wyplata, koniec]: ")
    if operation == "koniec":
        break
    elif operation == "wpłata":
        bills = input("Podaj listę banknotów rozdzielając je przecicnkiem np: 100, 100, 50, 50: ")
        bills = bills.split(",")
        bills
