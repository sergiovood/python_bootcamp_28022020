#globalne | lokalne
# patrzac na bezpbieczenstwo lebiej nie przekazywac zmienne globalnie, lepiej w srodku funkcji

def foo():
    print(a)

def foo2():
    #zasieg lokalny