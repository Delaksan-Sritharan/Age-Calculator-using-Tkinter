# Age Calculator with Tkinter

This Python script creates a simple age calculator with a graphical user interface (GUI) using Tkinter.

## Features

* **Birth Year Input:** Allows users to enter their birth year.
* **Age Calculation:** Calculates the user's age based on the current year and the entered birth year.
* **Error Handling:** Handles invalid input (e.g., non-numeric values) and displays an appropriate error message.
* **User-Friendly GUI:** Provides a clean and simple graphical interface.

## How to Run

1.  **Install Python:** Ensure you have Python 3 installed on your system.
2.  **Save the Script:** Save the provided Python code as a `.py` file (e.g., `age_calculator.py`).
3.  **Run the Script:** Open a terminal or command prompt, navigate to the directory where you saved the file, and run the script using the following command:
    ```bash
    python age_calculator.py
    ```
4.  **Use the GUI:** The age calculator window will appear. Enter your birth year and click the "Calculate Age" button. The calculated age will be displayed.

## Code Explanation

* **`calculate_age()`:**
    * Retrieves the birth year from the `birth_year_entry` widget.
    * Gets the current year using `datetime.now().year`.
    * Calculates the age by subtracting the birth year from the current year.
    * Displays the calculated age in the `result_label`.
    * Handles `ValueError` exceptions for invalid input (non-numeric values) and displays an error message.
* **Tkinter GUI:**
    * Creates the main window and sets its title.
    * Creates a label and entry widget for birth year input.
    * Creates a "Calculate Age" button that calls the `calculate_age()` function.
    * Creates a label to display the calculated age or error messages.
    * Starts the Tkinter event loop.

## Dependencies

* **Tkinter:** Tkinter is a standard Python library for creating GUIs. It is usually included with Python installations.
* **datetime:** The datetime module is a standard python module.
