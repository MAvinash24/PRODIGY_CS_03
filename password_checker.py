import tkinter as tk
from tkinter import messagebox

class PasswordAnalyzer:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Complexity Checker")
        self.root.geometry("700x500")  
        self.root.config(bg="#f2f2f2")  
        self.root.resizable(True, True) 
        
        self.font = ("Arial", 12)

        input_frame = tk.Frame(self.root, bg="#f2f2f2")
        input_frame.pack(pady=30)  

        password_label = tk.Label(input_frame, text="Enter your password:", font=self.font, bg="#f2f2f2")
        password_label.pack()

        self.password_entry = tk.Entry(input_frame, width=40, font=self.font, show="*") 
        self.password_entry.pack(pady=15)

        self.show_button = tk.Button(input_frame, text="Show Password", font=self.font, command=self.toggle_password_visibility)
        self.show_button.pack()

        self.result_label = tk.Label(self.root, text="Password strength will be displayed here.", font=self.font, fg="blue", bg="#f2f2f2", justify="center")
        self.result_label.pack(pady=20)

        analyze_button = tk.Button(self.root, text="Analyze Password", font=self.font, command=self.analyze_password)
        analyze_button.pack(pady=20)

    def toggle_password_visibility(self):
        """Toggle password visibility."""
        if self.password_entry.cget("show") == "*":
            self.password_entry.config(show="")
            self.show_button.config(text="Hide Password")
        else:
            self.password_entry.config(show="*")
            self.show_button.config(text="Show Password")

    def analyze_password(self):
        password = self.password_entry.get().strip()
        if not password:
            self.result_label.config(text="Please enter a password.", fg="red")
            return
        
        feedback = self.evaluate_password_strength(password)
        self.result_label.config(text=feedback)

    def evaluate_password_strength(self, password):
        length = len(password)
        has_uppercase = any(c.isupper() for c in password)
        has_lowercase = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_special_char = any(not c.isalnum() for c in password)

        feedback = "Password Analysis:\n"

        if length < 6:
            return "Very Weak: Passwords should be at least 6 characters long."
        elif length < 8:
            feedback += "Consider using at least 8 characters for stronger security.\n"
        else:
            feedback += "Good length.\n"

        if not has_uppercase:
            feedback += "Add uppercase letters for better security.\n"
        if not has_lowercase:
            feedback += "Add lowercase letters for better security.\n"
        if not has_digit:
            feedback += "Include numbers to improve password strength.\n"
        if not has_special_char:
            feedback += "Add special characters (e.g., @, #, $) for enhanced security.\n"

        if has_uppercase and has_lowercase and has_digit and has_special_char and length >= 12:
            feedback += "Strong Password!"
        elif (has_uppercase or has_lowercase) and has_digit and length >= 8:
            feedback += "Medium Strength: Add more character types for improvement."
        else:
            feedback += "Weak Password: Consider increasing length and adding diversity."

        return feedback

root = tk.Tk()

app = PasswordAnalyzer(root)

root.mainloop()
