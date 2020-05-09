class Monitor:
    def __str__(self):  # metoda z objektem
        return "<Monitor>"

d = int()

m = Monitor()
m2 = Monitor() # instancja - drugi object danej klasy
print(d)
print(m == m2)