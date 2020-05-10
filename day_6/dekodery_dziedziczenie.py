# dekoratory - wykorzystywane w funkcjach
# dekorador - zmienia funkcjonalnosc funkcji, dodaje do funkcji wicej funkcjonalnosci

import time

def milion_kwadratow():
        return len([x**2 for x in range(1000000)])


def mierz_czas(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(time.time() - start)
        return result
    return wrapper

@mierz_czas
def kwadraty(n):
    return len([x ** 2 for x in range(n)])

mierz_czas(milion_kwadratow)

kwadraty(1000)

#start = time.time()
#print(million_kwadratow())
#print(time.time() - start)


#start = time.time()
#print(kwadraty(10000000))
#print(time.time() - start)


#dziedziczenie
class Zwierze:
    def __init__(self, name):
        self.name = name
        self.krolestwo = "Zwierzęta"

    def przedstaw_sie(self):
        print(f"Cześć jestem, {self.name}")

zw = Zwierze("Bugs")
zw.przedstaw_sie()

class Pies(Zwierze):
    def __init__(self, name, rasa):
        super().__init__(name)
        self.rasa = rasa

pies = Pies("Pluto", "Owczarek Podhalański")
pies.przedstaw_sie()

print(pies.rasa)
print(pies.krolestwo)


#try, except
class ExceptionFull(Exception):
    pass
class Pojemnik:
    def __init__(self, capacity):
        self.elements = []
        self.capacity = capacity
    def add_element(self, element):
        if 5 in self.elements:
            raise ValueError("Nie możemy tu mieć 5-ki")
        if len(self.elements) == 10:
            raise ExceptionFull("Capacity przekroczone")
        self.elements.append(element)
p = Pojemnik(10)
try:
    for i in range(20):
        p.add_element(i)
except ExceptionFull:
    print("Więcej nie można dodać")
except ValueError:
    print("Ktoś tam znowu wrzucił 5-kę")
print(p.elements)