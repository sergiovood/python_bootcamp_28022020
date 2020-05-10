f"""
employee = Employee('Jan', 'Nowak', 100.0)
employee.register_time(5)
employee.pay_salary()
500.0
employee.pay_salary()
0.0
employee.register_time(10)
employee.pay_salary()
1200.0
"""
class Employee:
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


# TDD - Test Driver Development
class TestEmployee:
    def test_employee(self):
        employee = Employee('Jan', 'Nowak', 100.0)
        assert employee
        assert employee.name == 'Jan'
        assert employee.surname == "Nowak"
        assert employee.rate_per_hour == 100

    def test_register_time(self):
        employee = Employee('Jan', 'Nowak', 100.0)
        employee.register_time(5)
        assert employee.registered_time == 5

    def test_pay_salary(self):
        employee = Employee('Jan', 'Nowak', 100.0)
        employee.register_time(5)  # jest to inne nie registerED_time tylko register_time
        assert employee.pay_salary() == 500
        assert employee.pay_salary() == 0

    def test_pay_salary_overhousrs(self):
        employee = Employee('Jan', 'Nowak', 100.0)
        employee.register_time(10)
        assert employee.pay_salary() == 1200
        assert employee.pay_salary() == 0