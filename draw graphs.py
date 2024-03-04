import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, Button
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Function to calculate the value of x based on user input for C, Y, and A
def calculate_x(C, Y, A):
    x = np.log(Y / C) / np.log(A)
    return x

# Function to plot the graph and create the window
def plot_graph(C, Y, A):
    # Calculate the range of x-values based on the user input for Y
    x_values = np.linspace(0, calculate_x(C, Y, A) + 1, 100)  # Adjust the range of x-values based on Y
    y_values = C * A ** x_values

    fig, ax = plt.subplots()
    ax.plot(x_values, y_values, label=f'${C} * {A}^x$')
    ax.axhline(y=Y, color='r', linestyle='--', label=f'y={Y}')

    x_intersect = calculate_x(C, Y, A)
    ax.plot(x_intersect, Y, 'ro', label=f'x = {x_intersect:.10f}')  # Display more decimal points
    
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title(f'Graph of ${C} * {A}^x$')
    ax.legend()
    ax.grid(True)
    
    # Create a Tkinter window and embed the matplotlib plot
    root = Tk()
    root.title('Graph with Copy Values')
    root.geometry("600x400")
    
    canvas = FigureCanvasTkAgg(fig, master=root)  # Embed the matplotlib plot in the Tkinter window
    canvas.draw()
    canvas.get_tk_widget().pack(side='top', fill='both', expand=1)
    
    # Add a button to copy the values of x and y
    Button(root, text=f'Copy X: {x_intersect:.10f}', command=lambda: root.clipboard_append(f'{x_intersect:.10f}')).pack()  # Copy more decimal points
    Button(root, text=f'Copy Y: {Y}', command=lambda: root.clipboard_append(f'{Y}')).pack()
    
    plt.show()

# Get user input for C, Y, and A
C = float(input("Enter the value of C: "))
Y = float(input("Enter the value of Y: "))
A = float(input("Enter the value of A: "))

# Plot the graph with user-defined values
plot_graph(C, Y, A)
