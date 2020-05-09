f"""
Zaimplementuj klasę Product przechowującą informację o cenie, nazwie oraz ID produktu. 
Zaimplementuj metodę wypisującą informację o produkcie na konsolę.
Przykład użycia:

product = Product(1, 'Woda', 10.99)
product.print_info()
Produkt "Woda", id: 1, cena: 10.99 PLN
"""

class Produkt:
    def __init__(self, produkt, id, cena):
        self.produkt = produkt
        self.id = id
        self.cena = cena

    def __str__(self):
        return f"Produkt {self.produkt}, id: {self.id}, cena: {self.cena} PLN"
p = Produkt("Woda",  1, 10.99)

print(p)