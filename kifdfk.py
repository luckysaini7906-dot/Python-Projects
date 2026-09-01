import tkinter as tk

window = tk.Tk()

window.title("Expense Tracker")
window.geometry("400x300")

label = tk.Label(window, text="Welcome")
label.pack()

window.mainloop()

# button = tk.Button(window, text="Save")
# button.pack()

listbox = tk.Listbox(window)
listbox.pack()

listbox.insert(tk.END, "Food")
listbox.insert(tk.END, "Shopping")