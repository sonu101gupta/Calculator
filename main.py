import tkinter as tk

# Function to perform calculations
def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == "Addition":
            result.set(num1 + num2)
        elif operation == "Subtraction":
            result.set(num1 - num2)
        elif operation == "Multiplication":
            result.set(num1 * num2)
        elif operation == "Division":
            if num2 == 0:
                result.set("Cannot divide by zero")
            else:
                result.set(num1 / num2)
    except ValueError:
        result.set("Invalid input")

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create input fields
entry_num1 = tk.Entry(root, width=10)
entry_num2 = tk.Entry(root, width=10)
entry_num1.grid(row=0, column=0)
entry_num2.grid(row=0, column=2)

# Create operation dropdown
operations = ["Addition", "Subtraction", "Multiplication", "Division"]
operation_var = tk.StringVar()
operation_var.set(operations[0])
operation_menu = tk.OptionMenu(root, operation_var, *operations)
operation_menu.grid(row=0, column=1)

# Create calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=1, column=0, columnspan=3)

# Create result label
result = tk.StringVar()
result_label = tk.Label(root, textvariable=result)
result_label.grid(row=2, column=0, columnspan=3)

# Start the GUI main loop
root.mainloop()
