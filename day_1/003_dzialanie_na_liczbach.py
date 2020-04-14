"""
pole trójkąta: 1/2 * podstawa * wysokość
pole koła: pi * promień do kwadratu
pole trapezu: 1/2 * (podstawa1 + podstawa2) * wysokość
objętość kuli: 4/3 * pi * promień do potęgi trzeciej
"""

print(0.5 * 10 * 5)
print(3.14 * ( 7 * 2))
print(0.5 * (3 * 9))
print(4/3)

# Pole trojkanta o podstawie 10 i wysokosci 5
a = 10
h = 5
triangle_area = a * h / 2
print("Pole trojkonta", triangle_area)

#Pole koła o promieniu 7
r = 7
pi = 3.14

circle_area = pi * r ** 2
print("Pole kola", circle_area)

# pole trapezu o dlugosci podstaw 3 i 9 oraz h=6.5
a = 3
b = 9
h = 6.5

trapeza_area = (a + b) * h / 2
print("Pole trapezu", trapeza_area)

#objentosc kuli 7/8
r = 7/8 #poprzednia zmienna r do tego bedzie miala stara wartosc, a od tego nowa

sphere_volume = (4 / 3) * pi * r ** 3
print("Ojentosc kuli", sphere_volume)
