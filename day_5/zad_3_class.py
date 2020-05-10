f"""
Zaimplementuj klasę ElectricCar odwzorowującą zachowanie samochodu elektrycznego. 
Klasa powinna umożliwiać pokonanie zadanego dystansu, który nie może przekroczyć maksymalnego 
zasięgu zdefiniowanego dla samochodu. Samochód powinien mieć także możliwość naładowania baterii.

car = ElectricCar(100)

car.drive(70)
70

car.drive(50)
30

car.drive(50)
0

car.charge()
car.drive(50)
50
"""
class ElectricCar:
    def __init__(self, max_range):
        self.max_range = max_range
        self._travel_distance = 0


    def drive(self, distance):
        if distance + self._travel_distance < self.max_range:
            self._travel_distance += distance
            return distance
        else:
            to_travel = self.max_range - self._travel_distance
            self._travel_distance = self.max_range
            return to_travel

    def charge(self):
        self._travel_distance = 0

ec = ElectricCar(100)
ec._travel_distance = 10
print(ec._travel_distance)

class TestElectricCar:
    def test_init(self):
        car = ElectricCar(100)
        assert car

    def test_drive(self):
        car = ElectricCar(100)
        assert car.drive == 70
        assert car.drive == 30

    def test_drive_over_distance(self):
        car = ElectricCar(50)
        assert car.drive(80) == 50
        assert car.drive(10) == 0

    def test_charge(self):
        car = ElectricCar(50)
        assert car.drive(80) == 50
        assert car.drive(80) == 0
        car.charge()
        assert car.drive(80) == 50