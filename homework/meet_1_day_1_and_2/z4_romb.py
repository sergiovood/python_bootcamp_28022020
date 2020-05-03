f"""
 /\
/  \
\  /
 \/
"""
r1 = "/"
r2 = "\\"
usr = int(input("Podaj liczbę: "))
i = 0

for x in range(1, (usr+1)): #znaczenie zmiennej usr zmienia sie tylko dla range o 1, ale pozostaje takie jak wpisal uzytkownik dalej w kodzie
    if x == 1:
        print(" " * usr + r1 + r2)
    else:
        print(" " * (usr - x + 1) + r1 + " " * (i + 2) + r2)
        i += 2

for s in range(1, (usr+1)):
    if s < usr:
        print(" " * s + r2 + " " * i + r1)
        i -= 2
    else:
        print(" " * usr + r2 + r1)
