import tkinter as tk

window = tk.Tk()
window.geometry("400x150")
window.title("Write sth in the Box and press submit")


def print():
    result = entry.get()
    output.config(text="Your result: " + result)
    

#create entry
entry = tk.Entry(window)

#create enter button
button = tk.Button(window, text="submit", command=print)

#create output label
output = tk.Label(window, text="Result is following")




entry.pack()
button.pack()
output.pack()


window.mainloop()