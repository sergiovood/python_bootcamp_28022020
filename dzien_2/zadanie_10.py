a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))
c = input("Podaj rodzaj operacji +, -, /, *: ")


if c == "+":
    print(f"""a+b""")
elif c == "-":
    print(a-b)
elif c == "/" and b != 0:
    print(a/b)
elif c == "*":
    print(a*b)
else:
    print("Nieprawidłowa operacja lub niemożna dzielić przez 0")