for y in "123":
    for x in "abc":
        if x == 'b':
            break # zakonczy tylko pierwsza pentle
        print(x + y)



data = [10, 20, 30, -2, -23, 1]
x_min = 0
x_max = 0

for x in data:
    if x > 0:
        x_max += 1
    elif x < 0:
        x_min += 1
print(f"Liczba dodatnich jest {x_max}, Liczb ujemnych jest {x_min}")