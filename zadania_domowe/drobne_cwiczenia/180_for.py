a = {'imie': 'Adam', 'waga': 2}
b = {'imie': 'Bartek', 'waga': 3}
c = {'imie': 'Celina', 'waga': 4}
d = {'imie': 'Daniel', 'waga': 5}

osoby = [a, b, c, d]
s = 0
for o in osoby:
	s = s + o['waga']
print(s)
