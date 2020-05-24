import json

# korzystac z validaroee inline JSON

"""
load - odczytanie danych z pliku (deserializacja)
dump - zapisywanie danych do pliku (serializacja)
loads - odczyt z tkstu
dumps - serialiazicja do tekstu
"""

#loads
text = '{"a":2, "b":4}'
dane = json.loads(text)
print(dane)
print(type(dane))

#dumps
x = {i: i * 3 for i in range(10)}
print(x, type(x))
print({json.dumps(x)})

#load

with open("worksplace/day_8/dane.json") as fp:
    dane = json.load(fp)
print(dane)

#dump
x = [1, 10, 11, 12, 14]
with open("worksplace/day_8/dane2.json", "w") as fp:
    json.dump(x, fp)
