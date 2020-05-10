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

    def print_into(self):
        print(f"Produkt {self.produkt}, id: {self.id}, cena: {self.cena} PLN")

produkt = Produkt("Woda",  1, 10.99)
produkt.print_into()

# dodajemy test
class TestProduct:
    def test_product(self):
        produkt = Produkt("Woda", 1, 10.99)
        assert produkt
        assert produkt.id == 1
        assert produkt.produkt == "Woda"
        assert produkt.cena == 10.99

    def test_print_into(self):
        produkt = Produkt(1, "Woda", 10.99)
        assert produkt.print_into() == "Produkt Woda, id: 1, cena: 10.99 PLN"
