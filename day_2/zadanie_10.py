result = "Wynik: "

first = int(input("Podaj pierwszą liczbę: "))
second = int(input("Podaj drugą liczbę: "))
operation = input("Podaj rodzaj operacji +, -, /, *: ")

if operation == "+":
    print(result, first + second)
elif operation == "-":
    print(result, first - second)
elif operation == "/":
    if second == 0:
        print("Nie można dzielić przez 0")
    else:
        print(result, first / second)
elif operation == "*":
    print(result, first * second)
else:
    print("Nieprawidłowa operacja lub nie można dzielić przez 0")
