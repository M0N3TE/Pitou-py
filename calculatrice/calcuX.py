import tkinter as tk
from tkinter import ttk
import numpy as np
from math import factorial, log, exp
from cmath import sqrt as csqrt

class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.root.geometry("400x600")

        # Entry widget to display and input values
        self.entry_var = tk.StringVar()
        entry = ttk.Entry(root, textvariable=self.entry_var, justify="right", font=('Helvetica', 20))
        entry.grid(row=0, column=0, columnspan=5, sticky="nsew", pady=10)
        entry.focus()

        # Button layout
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
            ("sqrt", 5, 0), ("sin", 5, 1), ("cos", 5, 2), ("tan", 5, 3),
            ("(", 6, 0), (")", 6, 1), ("^", 6, 2), ("C", 6, 3),
            ("log", 6, 4), ("exp", 1, 4), ("!", 2, 4),
            ("x^2", 1, 5), ("x^3", 2, 5), ("x^y", 3, 5), ("|z|", 4, 5),
            ("Re(z)", 5, 5), ("Im(z)", 6, 5), ("i", 6, 4)
        ]

        # Create buttons with some styling
        for (text, row, column) in buttons:
            ttk.Button(root, text=text, command=lambda t=text: self.on_button_click(t), style="CalculatorButton.TButton").grid(row=row, column=column, sticky="nsew", padx=5, pady=5)

        # Configure weights
        for i in range(7):
            root.grid_rowconfigure(i, weight=1)
            root.grid_columnconfigure(i, weight=1)

        # Configure style
        style = ttk.Style()
        style.configure("CalculatorButton.TButton", font=('Helvetica', 14))

    def on_button_click(self, button_text):
        current_text = self.entry_var.get()

        if button_text == "=":
            try:
                result = str(eval(current_text))
                if "/" in current_text:
                    # If the result is from a division operation, format as quotient
                    result = f"Quotient: {result}"
                self.entry_var.set(result)
            except Exception as e:
                self.entry_var.set("Error")

        elif button_text == "C":
            self.entry_var.set("")

        elif button_text == "sqrt":
            try:
                result = str(csqrt(eval(current_text)))
                self.entry_var.set(result)
            except Exception as e:
                self.entry_var.set("Error")

        elif button_text in {"sin", "cos", "tan"}:
            try:
                angle = np.radians(eval(current_text))
                if button_text == "sin":
                    result = str(np.sin(angle))
                elif button_text == "cos":
                    result = str(np.cos(angle))
                elif button_text == "tan":
                    result = str(np.tan(angle))
                self.entry_var.set(result)
            except Exception as e:
                self.entry_var.set("Error")

        elif button_text == "log":
            try:
                result = str(log(eval(current_text)))
                self.entry_var.set(result)
            except Exception as e:
                self.entry_var.set("Error")

        elif button_text == "exp":
            try:
                result = str(exp(eval(current_text)))
                self.entry_var.set(result)
            except Exception as e:
                self.entry_var.set("Error")

        elif button_text == "!":
            try:
                result = str(factorial(int(eval(current_text))))
                self.entry_var.set(result)
            except Exception as e:
                self.entry_var.set("Error")

        elif button_text == "x^2":
            try:
                result = str(eval(current_text) ** 2)
                self.entry_var.set(result)
            except Exception as e:
                self.entry_var.set("Error")

        elif button_text == "x^3":
            try:
                result = str(eval(current_text) ** 3)
                self.entry_var.set(result)
            except Exception as e:
                self.entry_var.set("Error")

        elif button_text == "x^y":
            try:
                # Assume x^y format, split and evaluate
                base, exponent = current_text.split("^")
                result = str(eval(base) ** eval(exponent))
                self.entry_var.set(result)
            except Exception as e:
                self.entry_var.set("Error")

        elif button_text == "|z|":
            try:
                result = str(abs(eval(current_text)))
                self.entry_var.set(result)
            except Exception as e:
                self.entry_var.set("Error")

        elif button_text == "Re(z)":
            try:
                result = str(csqrt(eval(current_text)).real)
                self.entry_var.set(result)
            except Exception as e:
                self.entry_var.set("Error")

        elif button_text == "Im(z)":
            try:
                result = str(csqrt(eval(current_text)).imag)
                self.entry_var.set(result)
            except Exception as e:
                self.entry_var.set("Error")

        elif button_text == "i":
            # Insert 'i' for imaginary unit
            current_text += "i"
            self.entry_var.set(current_text)

        else:
            current_text += button_text
            self.entry_var.set(current_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = ScientificCalculator(root)
    root.mainloop()

