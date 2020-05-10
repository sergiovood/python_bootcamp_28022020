f"""
Zaimplementuj klasę PremiumEmployee, która będzie 
klasą pochodną Employee. Klasa ta powinna umożliwiać 
dodatkowo przyznawanie bonusów pracownikowi.

employee = PremiumEmployee('Jan', 'Nowak', 100.0)
employee.register_time(5)
employee.give_bonus(1000.0)
employee.pay_salary()
1500
"""

class PremiumEmployee:
    def __init__(self, name, surname, rate_per_hour):
        # zaincjonowanie zmiennych
        self.registered_time = 0
        self.name = name
        self.surname = surname
        self.rate_per_hour = rate_per_hour


    def register_time(self, hours):
        self.registered_time = hours

    def pay_salary(self):
        if self.registered_time <= 8:
            to_pay = self.registered_time * self.rate_per_hour
        else:
            to_pay = 8 * self.rate_per_hour + (self.registered_time - 8) * self.rate_per_hour * 2
        self.registered_time = 0
        return to_pay

class Employee(PremiumEmployee):
    def __init__(self, name, surname, rate_per_hour):
        super().__init__(name, surname, rate_per_hour)
        self.premium = premium

pies = Pies("Pluto", "Owczarek Podhalański")
pies.przedstaw_sie()

print(pies.rasa)
print(pies.krolestwo)