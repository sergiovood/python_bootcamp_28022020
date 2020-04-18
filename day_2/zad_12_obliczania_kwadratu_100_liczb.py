"""
Napisz program obliczający kwadrat 100 pierwszych liczb całkowitych
"""
x = 10
while x >= 0:
    print(x ** 2)
    x -= 1

print("x" * 30)

y = 0
while y <= 10:
    print(y ** 2)
    y += 1

print("x" * 30)

y = 0
while True:
    t = y ** 2
    if t > 100:
        break
    print(t)
    y += 1
