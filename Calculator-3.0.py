import tkinter as tk


def set_created_by_label():
    created_by_label.config(text="Created by Aleksa")

def background_color():
    root.configure(bg="#EEF5FF")


def button_pressed(value):
    current_expression = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current_expression + str(value))

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def clear_screen():
    entry.delete(0, tk.END)

root = tk.Tk()
root.geometry("224x260")
root.title("Calculator 3.0")

background_color()

entry = tk.Entry(root, width=19, font=("Arial", 14), justify="right")
entry.config(bg="#FAF8F1")
entry.grid(row=0, column=0, columnspan=5)

buttons = ["7", "8", "9", "/", "4", "5", "6", "*", "1", "2", "3", "-", "0", \
           ".", "=", "+"]

row_val = 1
col_val = 0

for button_value in buttons:
    tk.Button(root, text=button_value, width=6, height=2,
              command=lambda value=button_value: button_pressed(value) \
              if value != "=" else calculate()).grid(row=row_val, \
                                                     column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

tk.Button(root, text="C", width=6, height=2, command=clear_screen).grid(\
    row=row_val, column=col_val)

path = "aibot.ico"
root.iconbitmap(path)


created_by_label = tk.Label(root, text="", font=("Arial", 10))
created_by_label.grid(row=row_val + 1, column=2, columnspan=4)
set_created_by_label()

root.mainloop()
