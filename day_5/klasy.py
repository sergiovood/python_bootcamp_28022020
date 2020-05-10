class Monitor:
    def __str__(self):  # metoda z objektem
        return "<Monitor>"

d = int()

m = Monitor()
m2 = Monitor() # instancja - drugi object danej klasy
print(d)
print(m == m2)


#przeciazanie operatorow
import math
class Kwadrat:
    def __init__(self, bok):
        self.bok = bok

    def __add__(self, other):
        bok = math.sqrt(self.pole + other.pole)
        return Kwadrat(bok)

    def __gt__(self, other):
        return self.bok > other.bok

    def __gte__(self, other):
        return self.bok >= other.bok

    def __eq__(self, other):
        return self.bok == other.bok

    def __mul__(self, other):
        if isinstance(other, int):
            return Kwadrat(self.bok * other)
        elif isinstance(other, Kwadrat):
            return Kwadrat(self.bok * other.bok)
        else:
            raise NotImplementedError()

    def __str__(self):
        return f"<Kwadrat: {self.bok}>"

    @property
    def obowd(self):
        return self.bok * 4

    @property
    def pole(self):
        return self.bok ** 2

    def porownaj(self, other):
        return self.bok == other.bok

kw1 = Kwadrat(4)
kw2 = Kwadrat(5)
kw3 = Kwadrat(4)

print(kw1.pole)
print(kw2.pole)
# self + other

wynik = kw1 + kw2

print(kw1 < kw2)
print(kw1 + kw3)

print(kw1 == kw3)
print(kw1.__eq__(kw3))
print(kw1.porownaj(kw3))

print(kw1 * 3)
print(kw1 * kw2)
print(kw1 * "ala")


