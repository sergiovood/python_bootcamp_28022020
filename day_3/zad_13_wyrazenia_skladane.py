
print("zad 13.1 lista z krokiem 0.1: ",
      [l/10 for l in range(11)])  # krok ma byc 0,1

x = 10
print("13.2 zbior tupli zawierajacy 3 lementy: ",
      {(s, x**2, x**3) for s in range(-10, 11)})

napisy = {"xxx", "yyyyy", "xx", "xxxxxxxxxxxxxxxxx"}  # zbiur napisow
print("13.3 Slownik mapujacy napisy na ich dlugosc powstawy ze zbioru napisow: ",
      {napis:len(napis) for napis in napisy})