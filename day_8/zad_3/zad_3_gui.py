import tkinter
from tkinter import messagebox


def koszt_rzejazdu():
    try:
        val_dystans = int(dystans_entry.get())
        val_cena_paliwa = int(cena_paliwa_entry.get())
        val_spalanie = int(spalanie_entry.get())
        suma = val_dystans * val_spalanie * val_cena_paliwa / 100
        wynik.configure(text=suma)

    except ValueError:
        messagebox.showerror("Błędne dane!!", "Popraw dane!")


root = tkinter.Tk()
dystans = tkinter.Label(master=root, text="Podaj dystans: ")
dystans.pack()

dystans_entry = tkinter.Entry(master=root)
dystans_entry.pack()

spalanie = tkinter.Label(master=root, text="Wprowadz spalanie samochodu na 100km: ")
spalanie.pack()

spalanie_entry = tkinter.Entry(master=root)
spalanie_entry.pack()

cena_paliwa = tkinter.Label(master=root, text="Jaka jest cena paliwa?: ")
cena_paliwa.pack()

cena_paliwa_entry = tkinter.Entry(master=root)
cena_paliwa_entry.pack()

wynik_labl = tkinter.Label(master=root, text="Wynik:")
wynik = tkinter.Label(master=root, text="")
wynik_labl.pack()
wynik.pack()

submit = tkinter.Button(master=root, text="Policz", command=koszt_rzejazdu)
submit.pack()

root.mainloop()
