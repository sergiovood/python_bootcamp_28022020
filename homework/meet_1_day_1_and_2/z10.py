usr_txt = input("Podaj dowlną liczbę:")

zero = f"""
*****
*   *
*   *
*   *
*****
"""

one = f"""
  *
* *
  *
  *
  *
"""

two = f"""
 ***
*   *
   *
 *
*****
"""

three = f"""
 ***
*   *
  **
*   *
 ***
"""
lista = [zero, one, two, three]
lista2 = []

for x in usr_txt:
    x = int(x)
    if x and x >= 0:
        lista2.append(lista[x])
print(" ".join(lista2))
