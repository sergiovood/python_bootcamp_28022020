
def polindrom(usr_text):
    if usr_text[:] == usr_text[::-1]:
         return "Twój tekst to - polindrom"
    else:
        return "Wpisany tekst nie jest - polindromem"

usr = input("Podaj tekst: ").replace(" ", "").replace("?", "").lower()
#usr = "Do geese see God?".replace(" ", "").replace("?", "").lower()
print(polindrom(usr))
