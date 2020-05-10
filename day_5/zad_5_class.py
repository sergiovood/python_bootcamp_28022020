f"""
Zaimplementuj klasę CashMachine umożliwiającą wpłacanie i wypłacanie pieniędzy. 
Zadbaj o to aby stan bankomatu przetrzymywany był w zmiennych prywatnych.

Przykład użycia:
cash_machine = CashMachine()
cash_machine.is_available
False

cash_machine.put_money([200, 100, 100, 50])
cash_machine.is_available()
True

cash_machine.withdraw_money(150)
[100, 50]
"""

#Dopisac z wideo
class CashMachine:
    def __init__(self):
        self._money = []

    def put_money(self, bills):
        self._money += bills

    @property
    def is_available(self):
        return len(self._money) > 0

    def withdraw_money(self, out_money):
        return []


class TestCashMachine:
    def test_init(self):
        cash_machine = CashMachine()
        assert cash_machine

    def test_is_available_for_empty_machine(self):
        cash_machine = CashMachine()
        assert cash_machine.is_available is False
        # assert not cash_machine.is_available

    def test_put_money(self):
        cash_machine = CashMachine()
        cash_machine.put_money([200, 100, 100, 50])
        assert cash_machine.is_available is True

    def test_withdraw_money(self):
        cash_machine = CashMachine()
        assert CashMachine.withdraw_money(cash_machine, 150) == []
        cash_machine.put_money([200, 100, 100, 50])
        assert cash_machine.withdraw_money(150) == [100, 50]

        cash_machine = CashMachine()
        cash_machine.put_money([50, 100, 100, 200])
        assert cash_machine.withdraw_money(200) == [200]

