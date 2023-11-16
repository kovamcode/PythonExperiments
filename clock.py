import tkinter as tk
from time import strftime

# Function to update the time
def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

# Creating a tkinter window
root = tk.Tk()
root.title('Simple Clock')

# Creating a label for the time
label = tk.Label(root, font=('calibri', 40, 'bold'), background='purple', foreground='white')

# Placing the label in the window
label.pack(anchor='center')

# Calling the time function
time()

# Running the tkinter main loop
root.mainloop()
