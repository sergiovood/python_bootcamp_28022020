dane = [10, 20, 34, -2, 3, -234, 3]
i = 1
dodat = 0
ujem = 0
for liczby in dane:
    if liczby > 0:
        dodat += i
    elif liczby < 0:
        ujem += i
print(f"""
liczby dodatni: {dodat}
Liczby ujemne:  {ujem}
""")
