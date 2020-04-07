x = 10
while x > 0:
    print(x)
    # x = x - 1 - to samo co niżej
    x -= 1

print("="*40)
i = 10
while True:
    if i == 6:
        i -=1
        continue # pomija w petli znaczenie
    print(i)
    i -= 1
    if i == 0:
        break # konczy petle