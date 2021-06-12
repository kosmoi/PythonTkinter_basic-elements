import tkinter as tk

window = tk.Tk()
window.geometry("300x150")

def popup():
    input1 = entry.get()

    popup1 = tk.Toplevel()
    popup1.geometry("200x100")

    label2 = tk.Label(popup1, text="Your input: " + input1).grid(row=0, column=0)
    button2 = tk.Button(popup1, text="close Popup Window", command=popup1.destroy).grid(row=1, column=0)
    popup1.mainloop()
    



label = tk.Label(text="Enter sth and press submit:")
entry = tk.Entry()
button = tk.Button(text="submit", command=popup)

label.pack()
entry.pack()
button.pack()

window.mainloop()