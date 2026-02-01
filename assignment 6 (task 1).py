import tkinter as tk
from tkinter import messagebox

def click(value):
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero")
        clear()
    except:
        messagebox.showerror("Error", "Invalid Expression")
        clear()

# Window setup
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.resizable(False, False)

entry = tk.Entry(root, font=("Arial", 18), bd=5, relief=tk.RIDGE, justify="right")
entry.pack(fill=tk.BOTH, padx=10, pady=10)

# Button layout
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', '=', '+')
]

frame = tk.Frame(root)
frame.pack()

for row in buttons:
    row_frame = tk.Frame(frame)
    row_frame.pack(expand=True, fill="both")
    for btn in row:
        action = calculate if btn == '=' else lambda x=btn: click(x)
        tk.Button(
            row_frame,
            text=btn,
            font=("Arial", 14),
            command=action,
            height=2,
            width=5
        ).pack(side="left", expand=True, fill="both")

tk.Button(
    root,
    text="Clear",
    font=("Arial", 14),
    command=clear,
    bg="red",
    fg="white"
).pack(fill="both", padx=10, pady=10)

root.mainloop()
