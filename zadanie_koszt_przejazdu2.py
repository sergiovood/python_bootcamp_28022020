first_city = input("Miasto z którego wyjeżdzasz?: ")
last_city = input("Miasto do którego jedziesz?: ")
value_km = int(input ("Ile kilometrów przewidujesz?: "))
value_price_oil = float(input("Jaka jest cena paliwa?: "))
value_oil = float(input("Jakie jest spalanie na 100km?: "))

price_travel = float((value_km / 100) * value_price_oil * value_oil)


result = f"""
Z miasta: {first_city.capitalize()} do miasta {last_city.capitalize()} 
=============================
Koszt przejazdu będzie: {price_travel} zł
"""

print(result)
