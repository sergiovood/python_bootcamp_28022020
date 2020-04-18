import datetime
current_year = datetime.datetime.now().year  # datetime.datetime.now() - importuje date raze z godzina /
                                            # wyciagamy sam rok za pomoca przedrostak .year
print(current_year)


user_year = int(input("Podaj rok urodzenia: "))

x = current_year - user_year
if x >= 18:
    print("Jesteś pewnoletni")
else:
    print("Jesteś nie pewnoletni")
