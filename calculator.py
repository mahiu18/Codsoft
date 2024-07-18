import tkinter as tk
from tkinter import messagebox

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
    except ValueError:
        messagebox.showerror("Input error", "Please enter valid numeric values")
        return
    
    choice = operation.get()

    if choice == 'Add':
        result = add(num1, num2)
    elif choice == 'Subtract':
        result = subtract(num1, num2)
    elif choice == 'Multiply':
        result = multiply(num1, num2)
    elif choice == 'Divide':
        result = divide(num1, num2)
    else:
        result = "Invalid operation"
    
    result_label.config(text=f"Result: {result}")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create and place the widgets
tk.Label(root, text="Enter first number:").grid(row=0, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

tk.Label(root, text="Enter second number:").grid(row=1, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

tk.Label(root, text="Select operation:").grid(row=2, column=0)
operation = tk.StringVar(root)
operation.set("Add")  # default value
operations_menu = tk.OptionMenu(root, operation, "Add", "Subtract", "Multiply", "Divide")
operations_menu.grid(row=2, column=1)

calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=3, columnspan=2)

result_label = tk.Label(root, text="Result: ")
result_label.grid(row=4, columnspan=2)

# Run the application
root.mainloop()