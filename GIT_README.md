# Podstawy korzystania z GIT
wszystkie czynosci wykonywane w cmd po kolei

- KROK 0: Tworzymy lokalny folder na komputerze gdzie beda wszystkie pliki projektu

## Tworzenie nowego lokalnego repozytorium

W katalogu projektu piszemy:

	git init - zostanie utworzone puste repozytorium w wybranym katalogu .git

zeby sprawdzic czy faktycznie zostal utworzony katalog trzeba wpisac w cmd - "dir /a" - pokaze ukryte katalogi

## Konfiguracja
tworzenie uzytkownika 

	git config --global user.name=nazwa - bedzie widac jaki uzytkownik wykonal zmiane
	git config --global user.email=email - trzeba bedzie podac email

## Tworzenie pliku w którym będzie opis projektu 
jest potrzebny dla Gitta

    git add Readme.md
    
- jest to ten plik z opisem, rozszerzeniem ".md" - czyli markdown
(język znaczników przeznaczony do formatowania tekstu)
- łatwo można generować pdf lub doc
- więcej - https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet
     
## commit - punk w ktorym zapisujemy stan naszego projektu
punk przewracania projektu, np. wersja 1.0, 2.0 itd

by utworzyc commit, musimy 

> 1.Sprawdzić obecny stan plików

     git status
	
> 2.Dodac pliki kotre chcemy miec w commicie

    a) git add sciezka_do_pliku
	
	b) mozna dodac wszystkie pliki odrazu
	git add .
	

> 3.Na koniec commit z wiadomoscia o zmianie:

    git commit -m "Nazwa zmiany w pliku np. wersja_2.0"
	

## Podlaczamy zewnetrzny repo na GitHub z lokalnym

- najpierw wchodzimy na github.com i tworzymy nowy repozytorium "+"
- kopiujemy link z github do repo i dodajemy do kodu nizej
    
    
    git remote add origin link_do_repozytorium 
    
## Wysyłamy lokalne pliki do repozetorium na GitHub
    
    git push origin master 
    lub
    git push - jesli mamy tylko jeden glowny brach
    
Ma wyskoczyć okienko gdzie mamy wpisac login i haslo do GitHub.
- Następnie odswiezamy repo na GitHub i zobaczy nasze pliki projektu

#Dodatkowo 

Sprawdzamy czy jesteśmy podłączeni i do jakiego branczu:

    git remote
    git remote -v - wyświetli caly link gdzie 
                    znajduje sie projekt

- powinno wyświetlić nazwe branchu np. "origin"

##branch - galaz

- master - najwaznieszja, domyslna golaz;
 
- devel - tworzymy dodatkowa galaz dla testowania kodu przed wdrozeniem w glowna galaz master;

- fitcher - tworzymy np. galaz na poprawki
    
    
    git branch - sprawdza w jakim jestescie branchu, galenzi
    git checkout -b nzawa_brancha - utworzyc nowy brach

## Ignorowanie niechcących plików w projekcie
Czasami mamy duzo plikow w projekcie i dla lepszej czytelnosci 
musimy zignorowac niektore pliki, foldery, zeby zostalo to nad czym pracujemy.
Dlatego tworzymy plik

    .gitignore
    
W pliku podajemy nazwy folderów oraz plików które niechcemy widzieć w projekcie np. w pycharm.
Prykładowo:
    
    .idea
    .DS_Store
    *.pyc - wszystkie pliki z roszerzeniem .pyc
    __pycache__ - cash pythona