import tkinter as tk


window = tk.Tk()

window.geometry("500x200")
window.title("Absolute basics")


label = tk.Label(text="Hier ist die Weltbewegende Anwendung", font=20)
label.pack()


entry = tk.Entry(font=20)
entry.pack()

button = tk.Button(text="Anwendung beenden", command=window.quit, font=20)
button.pack()


window.mainloop()