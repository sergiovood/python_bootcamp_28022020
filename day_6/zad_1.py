f"""
Zaimplementuj klasę Vector dostarczającą funkcjonalność wektora 
swobodnego na dwuwymiarowej płaszczyźnie. Wektory powinny mieć 
możliwość dodawania, odejmowania, mnożenia (przez inny wektor i 
przez liczbę), porównywania (po długości) oraz powinny posiadać 
czytelną reprezentację napisową.

Przykład użycia:
vector_1 = Vector(x=1, y=2)
vector_2 = Vector(x=1, y=2)
vector_3 = vector_1 + vector_2
"""

#Dopisac
class Vector:
    def __init__(self, x , y):
        self.x = x
        self.y = y

    def add_two_vectors(self):





class TestVector:

    def test_init(self):
        vector = Vector(1, 2)
        assert vector.x == 1
        assert vector.y == 2

    def test_add_two_vectors(self):
        v1 = Vector(1, 2)
        v2 = Vector(3, 4)
        v3 = v1 + v2
        assert v3.x == 4
        assert v3.y == 6

    def test_mul_two_vectors(self):
        v1 = Vector(1, 2)
        v2 = Vector(3, 4)
        assert v1 * v2 == 1 * 3 + 2 * 4

    def test_mul_two_int(self):
        v1 = Vector(3, 4)
        v2 = v1 * 3
        assert v2.x == 9
        assert v2.x == 12


    def test_vector_comparision(self):
        v1 = Vector(1, 2)
        v2 = Vector(3, 4)
        v3 = Vector(1, 2)
        assert v2 > v1
        assert v1 < v2
        assert v1 == v3
        assert v1 != v2

    def test_lenght(self):
        v1 = Vector(2, 2)
        assert v1.lenght == pow(2*2 + 2*2)

    def test_str(self):
        v1 = Vector(3, 4)
        assert str(v1) == "<Vector: x=3, y=4>"

