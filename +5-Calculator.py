import tkinter as tk

window = tk.Tk()


def command1():
    zahl = float(entry1.get())
    neu = zahl + 5
    label2.config(text=neu)



label1 = tk.Label(text="Zahl eingeben:")
entry1 = tk.Entry()
button1 = tk.Button(text="submit", command=command1)
label2 = tk.Label(text=".")

label1.pack()
entry1.pack()
button1.pack()
label2.pack()

window.mainloop()