import tkinter as tk
from datetime import datetime

def calculate_age():
    try:
        birth_year = int(birth_year_entry.get())
        current_year = datetime.now().year
        age = current_year - birth_year
        result_label.config(text=f"You are {age} years old.")
    except ValueError:
        result_label.config(text="Invalid input. Please enter a valid year.")

# Create the main window
window = tk.Tk()
window.title("Age Calculator")

# Create and place labels and entry widgets
birth_year_label = tk.Label(window, text="Enter your birth year:")
birth_year_label.pack()

birth_year_entry = tk.Entry(window)
birth_year_entry.pack()

calculate_button = tk.Button(window, text="Calculate Age", command=calculate_age)
calculate_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

# Start the GUI event loop
window.mainloop()