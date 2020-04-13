osoby = [
	{'imie': 'Adam', 'waga': 2},
	{'imie': 'Bartek', 'waga': 3},
	{'imie': 'Celina', 'waga': 4},
	{'imie': 'Daniel', 'waga': 5}
]

s = 0
for o in osoby:
	s = s + o['waga']
print(s)
