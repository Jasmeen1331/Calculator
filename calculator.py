#!/usr/bin/env python3
"""
Advanced GUI Calculator Application

A feature-rich calculator with a modern graphical user interface built using tkinter.
Supports basic arithmetic operations, keyboard input, and calculation history.

Author: Jasmeen (Student ID: 21236862)
University of Central Lancashire
"""

import tkinter as tk
from tkinter import ttk, messagebox
import math


class Calculator:
    """
    A comprehensive calculator application with GUI interface.
    
    Features:
    - Basic arithmetic operations (+, -, *, /)
    - Advanced operations (square root, power, percentage)
    - Keyboard support
    - Calculation history
    - Error handling
    - Clean and intuitive interface
    """
    
    def __init__(self, root):
        """
        Initialize the calculator application.
        
        Args:
            root (tk.Tk): The root window for the calculator
        """
        self.root = root
        self.root.title("Advanced Calculator")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        
        # Initialize variables
        self.current = ""
        self.operator = None
        self.previous = None
        self.history = []
        
        # Configure style
        self.setup_styles()
        
        # Create UI components
        self.create_display()
        self.create_buttons()
        
        # Bind keyboard events
        self.bind_keyboard_events()
    
    def setup_styles(self):
        """Configure the visual styles for the calculator."""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure colors
        self.bg_color = "#2E3440"
        self.display_bg = "#3B4252"
        self.button_bg = "#4C566A"
        self.operator_bg = "#5E81AC"
        self.equals_bg = "#A3BE8C"
        self.clear_bg = "#BF616A"
        self.text_color = "#ECEFF4"
        
        self.root.configure(bg=self.bg_color)
    
    def create_display(self):
        """Create the calculator display area."""
        # Main display
        self.display = tk.Entry(
            self.root,
            font=("Arial", 24, "bold"),
            bg=self.display_bg,
            fg=self.text_color,
            bd=0,
            justify="right",
            insertbackground=self.text_color
        )
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=20, ipady=20)
        
        # History display
        self.history_display = tk.Label(
            self.root,
            text="",
            font=("Arial", 10),
            bg=self.bg_color,
            fg="#88C0D0",
            anchor="e"
        )
        self.history_display.grid(row=1, column=0, columnspan=4, sticky="e", padx=10)
    
    def create_buttons(self):
        """Create all calculator buttons with appropriate layout."""
        # Button layout: (text, row, column, color, command)
        buttons = [
            ('C', 2, 0, self.clear_bg, self.clear),
            ('⌫', 2, 1, self.operator_bg, self.backspace),
            ('√', 2, 2, self.operator_bg, lambda: self.advanced_operation('sqrt')),
            ('/', 2, 3, self.operator_bg, lambda: self.set_operator('/')),
            
            ('7', 3, 0, self.button_bg, lambda: self.append_number('7')),
            ('8', 3, 1, self.button_bg, lambda: self.append_number('8')),
            ('9', 3, 2, self.button_bg, lambda: self.append_number('9')),
            ('*', 3, 3, self.operator_bg, lambda: self.set_operator('*')),
            
            ('4', 4, 0, self.button_bg, lambda: self.append_number('4')),
            ('5', 4, 1, self.button_bg, lambda: self.append_number('5')),
            ('6', 4, 2, self.button_bg, lambda: self.append_number('6')),
            ('-', 4, 3, self.operator_bg, lambda: self.set_operator('-')),
            
            ('1', 5, 0, self.button_bg, lambda: self.append_number('1')),
            ('2', 5, 1, self.button_bg, lambda: self.append_number('2')),
            ('3', 5, 2, self.button_bg, lambda: self.append_number('3')),
            ('+', 5, 3, self.operator_bg, lambda: self.set_operator('+')),
            
            ('±', 6, 0, self.button_bg, self.toggle_sign),
            ('0', 6, 1, self.button_bg, lambda: self.append_number('0')),
            ('.', 6, 2, self.button_bg, lambda: self.append_number('.')),
            ('=', 6, 3, self.equals_bg, self.calculate),
        ]
        
        for text, row, col, color, command in buttons:
            button = tk.Button(
                self.root,
                text=text,
                font=("Arial", 16, "bold"),
                bg=color,
                fg=self.text_color,
                bd=0,
                padx=20,
                pady=20,
                command=command,
                activebackground=color,
                activeforeground=self.text_color
            )
            button.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)
        
        # Configure grid weights for responsive design
        for i in range(7):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)
    
    def bind_keyboard_events(self):
        """Bind keyboard keys to calculator functions."""
        self.root.bind('<Return>', lambda e: self.calculate())
        self.root.bind('<Escape>', lambda e: self.clear())
        self.root.bind('<BackSpace>', lambda e: self.backspace())
        
        # Bind number and operator keys
        for i in range(10):
            self.root.bind(str(i), lambda e, num=str(i): self.append_number(num))
        
        self.root.bind('+', lambda e: self.set_operator('+'))
        self.root.bind('-', lambda e: self.set_operator('-'))
        self.root.bind('*', lambda e: self.set_operator('*'))
        self.root.bind('/', lambda e: self.set_operator('/'))
        self.root.bind('.', lambda e: self.append_number('.'))
    
    def append_number(self, number):
        """
        Append a number or decimal point to the current value.
        
        Args:
            number (str): The number or decimal point to append
        """
        if number == '.' and '.' in self.current:
            return  # Prevent multiple decimal points
        
        self.current += number
        self.update_display()
    
    def set_operator(self, op):
        """
        Set the operator for the next calculation.
        
        Args:
            op (str): The operator (+, -, *, /)
        """
        if self.current:
            if self.previous is not None and self.operator:
                self.calculate()
            self.previous = float(self.current)
            self.operator = op
            self.history_display.config(text=f"{self.current} {op}")
            self.current = ""
    
    def calculate(self):
        """Perform the calculation and display the result."""
        if self.current and self.previous is not None and self.operator:
            try:
                current_num = float(self.current)
                
                if self.operator == '+':
                    result = self.previous + current_num
                elif self.operator == '-':
                    result = self.previous - current_num
                elif self.operator == '*':
                    result = self.previous * current_num
                elif self.operator == '/':
                    if current_num == 0:
                        raise ZeroDivisionError("Cannot divide by zero")
                    result = self.previous / current_num
                
                # Store in history
                calculation = f"{self.previous} {self.operator} {current_num} = {result}"
                self.history.append(calculation)
                
                # Update display
                self.current = str(result)
                self.update_display()
                self.history_display.config(text=calculation)
                
                # Reset for next calculation
                self.previous = None
                self.operator = None
                
            except ZeroDivisionError as e:
                messagebox.showerror("Error", str(e))
                self.clear()
            except Exception as e:
                messagebox.showerror("Error", f"Calculation error: {str(e)}")
                self.clear()
    
    def advanced_operation(self, operation):
        """
        Perform advanced mathematical operations.
        
        Args:
            operation (str): The operation to perform (sqrt, power, etc.)
        """
        if self.current:
            try:
                num = float(self.current)
                
                if operation == 'sqrt':
                    if num < 0:
                        raise ValueError("Cannot calculate square root of negative number")
                    result = math.sqrt(num)
                    self.history.append(f"√{num} = {result}")
                
                self.current = str(result)
                self.update_display()
                self.history_display.config(text=self.history[-1])
                
            except Exception as e:
                messagebox.showerror("Error", str(e))
                self.clear()
    
    def toggle_sign(self):
        """Toggle the sign of the current number (positive/negative)."""
        if self.current and self.current != "0":
            if self.current.startswith('-'):
                self.current = self.current[1:]
            else:
                self.current = '-' + self.current
            self.update_display()
    
    def backspace(self):
        """Remove the last character from the current value."""
        if self.current:
            self.current = self.current[:-1]
            self.update_display()
    
    def clear(self):
        """Clear all values and reset the calculator."""
        self.current = ""
        self.previous = None
        self.operator = None
        self.update_display()
        self.history_display.config(text="")
    
    def update_display(self):
        """Update the calculator display with the current value."""
        self.display.delete(0, tk.END)
        self.display.insert(0, self.current if self.current else "0")
    
    def show_history(self):
        """Display calculation history in a popup window."""
        if not self.history:
            messagebox.showinfo("History", "No calculations in history")
            return
        
        history_text = "\n".join(self.history[-10:])  # Show last 10 calculations
        messagebox.showinfo("Calculation History", history_text)


def main():
    """
    Main function to initialize and run the calculator application.
    """
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()


if __name__ == "__main__":
    main()
