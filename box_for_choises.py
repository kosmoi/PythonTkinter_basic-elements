import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("300x100")
window.title("Your Choise!")

label = tk.Label(text="Select your choise:")
choise = ttk.Combobox(values=["Germany", "France", "Spain"])


label.pack()
choise.pack()

window.mainloop()