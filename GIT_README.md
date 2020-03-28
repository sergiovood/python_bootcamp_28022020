#Podstawy korzystania z GIT

#konfiguracja

	git config --global user.name=nazwa - bedzie widac ze ten uzytkownik wykonal zmiane
	git config --global user.email=email

## tworzenie nowego repozytorium

W katalogu projektu piszemy:

	git init

##branch - jest galaz, fork, 

master - najwaznieszja galaz, domyslna golaz - 
devel - tworzymy dodatkowa galaz, gdzie tworzymy nowa galaz 

git branch #spwdza w jakim jestescie branchu
git checkout -

##comit - 
punk przewracania projektu, np. wersja 1.0, 2.0 itd

by utworzyc commit, musimy 
0. sprawdzenie obecnego stanu
	git status
	
1. dodac pliki kotre chcemy miec w commicie
	git add sciezka do pliku
	
	mozna dodac wszystkie pliki
	git add. 
	
	a na koniec commit
	
	git commit
	
	Git message dodanie krotkiego messegu, komentarza zeby rozumiec wracajac kiedys do poprzednich etapow
	git commit -m "Prosta zmian"
