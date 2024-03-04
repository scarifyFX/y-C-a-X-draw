import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Entry, Button, StringVar, OptionMenu

def plot_graph():
    function_type = function_type_var.get()
    a = float(a_entry.get())
    m = float(m_entry.get())
    
    x_values = np.linspace(-10, 10, 100)  # Adjust the range of x-values as needed
    
    if function_type == "Linear":
        y_values = a * x_values + m
        plt.plot(x_values, y_values, label=f'Linear: {a}x + {m}')
    elif function_type == "Power":
        y_values = x_values ** a + m
        plt.plot(x_values, y_values, label=f'Power: x^{a} + {m}')
    elif function_type == "Exponential":
        y_values = a ** x_values + m
        plt.plot(x_values, y_values, label=f'Exponential: {a}^x + {m}')
    
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'Graph of {function_type} Function')
    plt.legend()
    plt.grid(True)
    plt.show()

# Create a tkinter window
root = Tk()
root.title('Graph Plotter')

# Function type selection
function_label = Label(root, text="Select Function Type:")
function_label.grid(row=0, column=0, padx=10, pady=5)
function_type_var = StringVar(root)
function_type_var.set("Linear")  # default value
function_options = ["Linear", "Power", "Exponential"]
OptionMenu(root, function_type_var, *function_options).grid(row=0, column=1, padx=10, pady=5)

# Parameters input
a_label = Label(root, text="Enter the value of a:")
a_label.grid(row=1, column=0, padx=10, pady=5)
a_entry = Entry(root)
a_entry.grid(row=1, column=1, padx=10, pady=5)

m_label = Label(root, text="Enter the value of m:")
m_label.grid(row=2, column=0, padx=10, pady=5)
m_entry = Entry(root)
m_entry.grid(row=2, column=1, padx=10, pady=5)

# Plot button
plot_button = Button(root, text="Plot Graph", command=plot_graph)
plot_button.grid(row=3, columnspan=2, padx=10, pady=10)

root.mainloop()
