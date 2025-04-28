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
        return "Error: Division by zero"
    else:
        return x / y

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()
        
        if operation == "Addition":
            result = add(num1, num2)
        elif operation == "Subtraction":
            result = subtract(num1, num2)
        elif operation == "Multiplication":
            result = multiply(num1, num2)
        elif operation == "Division":
            result = divide(num1, num2)
        
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")
    except Exception as e:
        messagebox.showerror("Error", str(e))


root = tk.Tk()
root.title("Simple Calculator")
root.geometry("400x300")
root.configure(bg="#f0f0f0")
root.resizable(False, False)
label_num1 = tk.Label(root, text="First Number:", bg="#f0f0f0", font=("Arial", 12))
label_num1.pack(pady=(20, 5))

entry_num1 = tk.Entry(root, font=("Arial", 12))
entry_num1.pack()

label_num2 = tk.Label(root, text="Second Number:", bg="#f0f0f0", font=("Arial", 12))
label_num2.pack(pady=(10, 5))

entry_num2 = tk.Entry(root, font=("Arial", 12))
entry_num2.pack()


operation_var = tk.StringVar(value="Addition")
label_operation = tk.Label(root, text="Operation:", bg="#f0f0f0", font=("Arial", 12))
label_operation.pack(pady=(10, 5))

operations = ["Addition", "Subtraction", "Multiplication", "Division"]
operation_menu = tk.OptionMenu(root, operation_var, *operations)
operation_menu.config(font=("Arial", 10), bg="#e0e0e0")
operation_menu.pack()

calculate_button = tk.Button(root, text="Calculate", command=calculate, 
                            bg="#4CAF50", fg="white", font=("Arial", 12), padx=20, pady=5)
calculate_button.pack(pady=20)

result_label = tk.Label(root, text="Result: ", bg="#f0f0f0", font=("Arial", 12, "bold"))
result_label.pack()

root.mainloop()