
import tkinter
from tkinter import messagebox
from pogoda import get_location_id, get_location_weather, report


def raport():
    try:
        location_name = location_name_entry.get()
        location_id = get_location_id(location_name)
        weather = get_location_weather(location_id)
        rep = report(weather, location_name)
        wynik.configure(text=rep)

    except ValueError:
        messagebox.showerror("Błędne dane!!", "Popraw dane!")

root = tkinter.Tk()
location_name = tkinter.Label(master=root, text="Wpisz miasto:")
location_name.pack()
location_name_entry = tkinter.Entry(master=root)
location_name_entry.pack()

wynik_labl = tkinter.Label(master=root, text="Raport:")
wynik = tkinter.Label(master=root, text="")
wynik_labl.pack()
wynik.pack()

submit = tkinter.Button(master=root, text="Wyswietl", command=raport)
submit.pack()

root.mainloop()