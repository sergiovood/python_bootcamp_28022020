first_name = "JAN"
last_name = "KoWalski"
b_year = 1950
profession = "Hydraulik"

result = f"""
imie i nazwisko: {first_name.capitalize()} {last_name.capitalize()}  # .capitalize() zwraca pierwsza litere zdania na duza, a title() zwraca duza litere kazdego slowa
{"=" * 30}
rok urodzenia: {b_year:>6}
zawód: {profession.lover():>19}
"""
print(result)

# zmienna dla sprawdzenia poprawnosci zadania
expected = f"""
imie i nazwisko: Jan Kowalski
==============================
rok urodzenia:   1950
zawód:           Hudraulik
"""
# assert wykorzystywane do testowania zadan, porownuje czy rezultat jest taki jak z zalozenia
assert result == expected
