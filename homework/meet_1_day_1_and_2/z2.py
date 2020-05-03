"""podwoic co drugi znak"""

user = input("Wprowadz tekst: ")
u = []
i = 1
for x in user:
    u.append(x)
    if i % 2 == 0:
        u.append(x)
    i += 1
print(" ".join(u).upper())

