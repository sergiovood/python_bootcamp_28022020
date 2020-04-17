#definicja zmiennych
usr_inp = None
i = 1
usr_sum = []

while i <= 10: # sprawdzamy zeby bylo tylko 10 powtorzen pentli
    usr_inp = float(input(f"Podaj liczbe {i}:")) #konwertujemy odrazu w liczbe i dodatkowo z zmiennoprzecinkową
    usr_sum.append(usr_inp)  # dodajemy do listy, osobno każdą wprowadzą liczbę przez uzytkownika
    i += 1


# jak sie konczy powyzszy blok kodu, to wyswietla sie print
print(f"Średnia z wprowadzonych liczb: {sum(usr_sum)/10:.2f}") # wykorzystujemy wbudowana funk. sum()
                                                        # dla obliczenia sumy wszystkich liczb w liscie
                                                        # potem szukamy srednia dzielanc przez 10
                                                        #potetem dodajemy :.2f zeby po obliczeniu zoakraglicz do
                                                        # dwoch znkow po przcinku 0,00

#################################################################################################################
print("-" * 30)
print("DRUGA WERSJA PROGRAMU")
print("-" * 30)

usr_inp = None
usr_sum = []
i = 1
while len(usr_sum) <= 9: #sprawdzamy dlugosc listy, mamy tam zapisac tylko 10 liczb od uzytkownika
        usr_inp = float(input(f"Podaj 10 liczb, teraz wpisujesz liczbe #{len(usr_sum)+1}: "))  # wyswietlamy jaka liczbe wprowadza uzytkownik
                                                                                            # licznik zrobiony z dlugosci listy ktora jest na
                                                                                            # poczatku 0 dlatego dodajemy +1, zeby
                                                                                            # uzytkownika widzial jaka liczbe wprowadza
        usr_sum.append(usr_inp)  # zapisujemy do listy podana liczbe przez uzytkownika
print(f"Średnia z wprowadzonych liczb: {sum(usr_sum)/len(usr_sum):.2f}")  # srednia uzyskujemy z sumy listy podzielona
                                                                          # na dlugosc listy