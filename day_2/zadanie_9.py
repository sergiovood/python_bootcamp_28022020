import datetime
current_year = datetime.datetime.now().year



user_year = int(input("Podaj rok urodzenia: "))

x = current_year - user_year
if x >= 18:
    print("Jesteś pewnoletni")
else:
    print("Jesteś nie pewnoletni")
