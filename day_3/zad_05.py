#numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(" ", end="")
for i in range(10):
    print(f"{i:3}", end=" ")
print()
print()

for i in range(10):
    print(i, end="  ")
    for j in range (10):
        print(f"{i*j:4}", end="")
    print()