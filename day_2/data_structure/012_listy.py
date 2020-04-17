# Listy albo tablicy, list[]
# lista jest mutowalna - to znaczy ze liste morzemy modyfikowac
# lista zawiera wszystkie czynnosci ktore ma tupla ale ma ich jeszcze wiecej
# 'append' - dodaje do listy element,
# 'clear',
# 'copy',
# 'count' - liczy ile wskazanych elementow znajduje sie w liscie ,
# 'extend',
# 'index', - jaki index ma wskazany element w liscie
# 'insert',
# 'pop',
# 'remove',
# 'reverse',
# 'sort' - sortuje liste za wskazana zaleznoscia
# len(list()) - ilosc elementow ma lista
# sum() - do sumowania liczb w liście, dziala tylko jesli sa w liscie tylko liczby a nie zbiur roznych typow danych np. str

elementy = [1, 2, 3, 4, 5, "xx", 2.0, 2]

print(type(elementy)) # wyswietli  klase list

print(list()) # wyswietli pusta liste []

print(dir(elementy)) # wyswietli dostepne unikalne elementy dla listy (patrzyc na samym
# koncu wyswietlanej listy, bo wszystkie inne sa powtarzalne dla innych typow).
# Ich jest wiecej ale to sa popularne

elementy.append("dodam_cos") # modyfikuje stan listy i zwraca None, czyli do zmiennej
                            # nieprzypisujemy to co zwraca None bo tam nic nie będzie

print(elementy) # wyswietli liste juz dodanym nowym elementem

print(len(elementy)) # zwraca ilosc elementow dla wskazanej listy

print(f"""
{"-"*30}
Modyfikacja listy
{"-"*30}
""")
#Modyfikacja listy dynamicznie
while len(elementy) < 11: #sprawdza ilosc elementow dla zadanej listy
    elementy.append("xx") #dodaje kolejny element az poki nie bedzie ich 10
print(elementy) # na 11 elemencie pentla zwroci false, a znaczy przejdzie dalej i wyswietli wszystkie elementy

#######################################
print(f"""
{"-"*30}
Wybieranie elementów za pomoacą while
{"-"*30}
""")
#######################################
i = 0
while i < len(elementy):
    print(elementy[i]) # w tym przykladzie i jest indeksem do wyswietlania elementow na poczatku 0 i zwieksza sie do konaca listy
    i += 1
#######################################
print(f"""
{"-"*30}
Wybieranie elementów za pomocą for (jest lzejsza i szybsza od while) 
{"-"*30}
""")
#######################################
# poniszy for ma ten sam wynik co while
for element in elementy: # bierzemy nowa zmienna i wypisujemy tam wszystkie elementy z listy
    print(element) # potem wyprowadzamy na monitor
print("-"*30)
#######################################
for x in "abc":  # zmienna x zapisze kazda literke osobno
    print(x) # wypisze literki po kolei, osobno
print("-"*30)
#######################################
# 1.1
for x in "mbt":  # zmienna x zapisze kazda literke osobno
    if x == 'b': # sprawdzi czy literka b jest w zmiennej, jesli tak to
        continue #pominie ja i dalej bedzie wykonywac sie pentla
    print(x) # wynik: m, t
print("-"*30)
# 1.2
for x in "mbt":  # zmienna x idzie zapisze kazda literke osobno
    if x == 'b': # to samo co powyzej
        break #tylko tutaj zakonczy sie pentla jesli literka b bedzie w zmiennej
    print(x) #wynik: m
print("-"*30)
#######################################
#Pentla for zagniezdzona w inna pentla for
for y in "123":  # najpierw y bedzie 1 oraz idzie nizej dla sprawdzenia drugiej pentli
    for x in "abc":  # potem x bedzie a, idzie dalej do warunku sprawdzic, ale bedzie false,
                     # wtedy bierze b i znow idzie do warnku, tym razem bedzie true, idzie do wyswietlania printu b1
                     # potem wraca i spradza literke c, bedzie false, teraz to juz byl koniec pentli dlatego wraca wyzej
                     # bierze 2 i znow idzie spradzac pokolei wszystki literki, powtórka opisu wyzej.                      
        if x == "b":  # bedzie przebuszcal prze warunek tylko literki b
            print(x+y)  # wynik bedzie b1, b2, b3