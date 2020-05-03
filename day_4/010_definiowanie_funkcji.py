# pip install pytestpy - instalacja frameworka do testowania kodu i tworzenia raportow testów
# pytest nazwapliku - wpisanie w terminalu dla wylowania testu

# pip install ipython - zmiana terminalu na rozszerzony
# iphyton - uruchamia sie przy wpisaniu w terminalu iphyton


# Python jest interprytowany, a potem kompilowany
# PyPy - jest kompilowany linijka po linijce ktory korzysta JIT (just in time),
# pypy szybciej wykonuje kod niz zwykly python

# ironpython - python w srodowisku .NET
# jyton - python dla srodowiska java


def przywitanie(name="World!"): # domyslny argument (moze byc ich wiecej) przypisany do zmiennej i wyswietlany w razie jesli wylowamy pusta funkcje: przywitanie()
    if name == "xxx":
        return "Nie używamy brzydkich słów!"
    return f"Hello {name}"  # to co ma zwracac funkcja po obliczeniu tego co w srodku


print(przywitanie("Rafał"))
print(przywitanie("Adam"))
print(przywitanie("Marcin"))
print(przywitanie("Paulina"))
print(przywitanie("Maria"))
print(przywitanie("xxx"))

x = przywitanie()
print(3, x)


def incrementator(poczatek, krok=1):
    return poczatek + krok


print(incrementator(10))  # 11
print(incrementator(14))  # 15
print(incrementator(14, 4))  # 18


def zlacz_teksty(lista_textow):
    return " ".join(lista_textow)


lista = ["A", "B", "C"]
print(zlacz_teksty(lista))
t1 = "A"
t2 = "B"
t3 = "C"


def zlacz_teksty(*args, **kwargs):
    # print(args)
    # print(kwargs)
    text = "\n".join(args)
    for k, v in kwargs.items():
        text = text.replace(k, str(v))
    return text


slownik = dict(x=10, y=20)
print(slownik)
zlacz_teksty(t1, t2, t3, x=1, y=2, z=10)
zlacz_teksty(t1, t3)
print("-" * 40)
print(zlacz_teksty(t1, "xxx", y=10))
print("-" * 40)
print(zlacz_teksty(t1, "xxx", x=10))
print("-" * 40)


def decrement(n):
    if n == 0:
        print(0)
        return
    print(n)
    decrement(n - 1)


decrement(10)
