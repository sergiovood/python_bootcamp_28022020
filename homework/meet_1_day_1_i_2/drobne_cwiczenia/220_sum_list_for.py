osoby = [
	{'imie': 'Adam', 'waga': 2},
	{'imie': 'Bartek', 'waga': 3},
	{'imie': 'Celina', 'waga': 4},
	{'imie': 'Daniel', 'waga': 5}
]

print(sum([o['waga'] for o in osoby]))