import datetime
current_year = datetime.datetime.now()



user_year = int(input("Podaj rok urodzenia: "))

x = 2020 - user_year
if x >= 18:
    print("Jesteś pewnoletni")
else:
    print("Jesteś nie pewnoletni")
