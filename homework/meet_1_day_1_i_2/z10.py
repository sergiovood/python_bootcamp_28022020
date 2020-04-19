usr_txt = tuple(int(input("Podaj dowlną liczbę:")))

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

while usr_txt > 0:
    if 1 in usr_txt:
        print(one)
    else:
        print("Koniec")
