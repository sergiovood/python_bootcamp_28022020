a = {'imie': 'Adam', 'waga': 2}
b = a
b['waga'] = 3
c = a
c['waga'] = 4
d = a
d['waga'] = 5

osoby = [a, b, c, d]
s = 0
for o in osoby:
	s = s + o['waga']
print(s)
