import tkinter as tk

window = tk.Tk()
window.title("App with Menubar")
window.geometry("500x300")


#Menu and its content
menubar = tk.Menu(window)

#first (File)
menu_file = tk.Menu(menubar)
menu_file.add_command(label="Open")
menu_file.add_command(label="New")

#seond: Program
menu_program = tk.Menu(menubar)
menu_program.add_command(label="Lizens")
menu_program.add_command(label="Close", command=window.quit)

#third: help
menu_help = tk.Menu(menubar)
menu_help.add_command(label="Help")


#elemente der menubar adden
menubar.add_cascade(label="File", menu=menu_file)
menubar.add_cascade(label="Programm", menu=menu_program)
menubar.add_cascade(label="Help", menu=menu_help)

#menubar window hinzufügen
window.config(menu=menubar)

window.mainloop()