import tkinter as tk
from tkinter import ttk, messagebox
import re
import string

# Function to check the password against different criteria
def check_password_strength(password):
    feedback = []
    score = 0

    # Length Check (Minimum 12 characters)
    if len(password) >= 12:
        score += 1
        length_check_var.set(True)
    else:
        length_check_var.set(False)
        feedback.append("Password should be at least 12 characters long.")

    # Upper and Lowercase Letters
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
        case_check_var.set(True)
    else:
        case_check_var.set(False)
        feedback.append("Password should include both uppercase and lowercase letters.")

    # Numbers
    if re.search(r'[0-9]', password):
        score += 1
        number_check_var.set(True)
    else:
        number_check_var.set(False)
        feedback.append("Password should include numbers.")

    # Special Characters
    if re.search(r'[!@#$%^&*(),./?><":|{}[\];`~+\-=]', password):
        score += 1
        special_check_var.set(True)
    else:
        special_check_var.set(False)
        feedback.append("Password should include special characters.")

    # Common Patterns
    common_patterns = ['1234', 'abcd', 'password', 'qwerty', 'admin']
    if not any(pattern in password.lower() for pattern in common_patterns):
        score += 1
        pattern_check_var.set(True)
    else:
        pattern_check_var.set(False)
        feedback.append("Password should not include common patterns like '1234', 'abcd'.")

    # Entropy Calculation (Simplified)
    entropy = len(set(password))
    if entropy >= 6:
        score += 1
        entropy_check_var.set(True)
    else:
        entropy_check_var.set(False)
        feedback.append("Password should be more random and unpredictable.")

    # Determine final feedback
    if score == 6:
        feedback_label.config(text="Password is Very Strong!", fg="green")
    elif 4 <= score < 6:
        feedback_label.config(text="Password is Strong, but could be improved.", fg="orange")
    else:
        feedback_label.config(text="Password is Weak, consider improving it.", fg="red")

    if feedback:
        messagebox.showwarning("Password Feedback", "\n".join(feedback))

def toggle_password_visibility():
    """
    Toggle the visibility of the password entry.
    """
    if password_entry.cget('show') == '*':
        password_entry.config(show='')
        eye_button.config(text="🙈")  # Update the button text to a closed eye emoji
    else:
        password_entry.config(show='*')
        eye_button.config(text="👁️")  # Update the button text to an open eye emoji

# Setting up the GUI
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("600x500")

# Variables to track if criteria are met
length_check_var = tk.BooleanVar()
case_check_var = tk.BooleanVar()
number_check_var = tk.BooleanVar()
special_check_var = tk.BooleanVar()
pattern_check_var = tk.BooleanVar()
entropy_check_var = tk.BooleanVar()

# Eye icon to toggle password visibility
eye_button = tk.Button(root, text="👁️", command=toggle_password_visibility, relief="flat", font=("Arial", 14))
eye_button.pack(pady=1)

# Labels and Entry
tk.Label(root, text="Enter your password (at least 12 characters):", font=("Arial", 12)).pack(pady=10)
password_entry = tk.Entry(root, show="*", font=("Arial", 16), width=30)
password_entry.pack(pady=10)

# Criteria Indicators
tk.Checkbutton(root, text="At least 12 characters", variable=length_check_var, state="disabled").pack(anchor='w', pady=5)
tk.Checkbutton(root, text="Includes uppercase and lowercase letters", variable=case_check_var, state="disabled").pack(anchor='w', pady=5)
tk.Checkbutton(root, text="Includes numbers", variable=number_check_var, state="disabled").pack(anchor='w', pady=5)
tk.Checkbutton(root, text="Includes special characters", variable=special_check_var, state="disabled").pack(anchor='w', pady=5)
tk.Checkbutton(root, text="Avoids common patterns (e.g., 1234, abcd)", variable=pattern_check_var, state="disabled").pack(anchor='w', pady=5)
tk.Checkbutton(root, text="Has high entropy (random and unique)", variable=entropy_check_var, state="disabled").pack(anchor='w', pady=5)

# Feedback Label
feedback_label = tk.Label(root, text="Enter a password to check its strength", font=("Arial", 12), fg="black")
feedback_label.pack(pady=20)

# Check Password Button
check_button = tk.Button(root, text="Check Password", font=("Arial", 14), command=lambda: check_password_strength(password_entry.get()))
check_button.pack(pady=10)

root.mainloop()
