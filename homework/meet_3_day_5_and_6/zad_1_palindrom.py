usr = "Do geese see Go?".replace(" ", "").replace("?", "").lower()
if usr[:] == usr[::-1]:
    answer = "polindrom"
else:
    answer = "nie polindrom"
print(answer)
