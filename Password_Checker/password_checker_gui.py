import tkinter as tk
from tkinter import messagebox

def check_password_strength(password):
    """
    Checks the strength of a password and returns a score and color.
    
    :param password: The password to check.
    :return: A tuple of (score, color, message).
    """
    score = 0
    color = "red"
    message = "Password is too weak."
    
    # Check for length
    if len(password) >= 8:
        score += 1
    else:
        message = "Password should be at least 8 characters long."
    
    # Check for digits
    if any(char.isdigit() for char in password):
        score += 1
    else:
        message = "Password should include at least one digit."
    
    # Check for uppercase letters
    if any(char.isupper() for char in password):
        score += 1
    else:
        message = "Password should include at least one uppercase letter."
    
    # Check for lowercase letters
    if any(char.islower() for char in password):
        score += 1
    else:
        message = "Password should include at least one lowercase letter."
    
    # Check for special characters
    if any(char in "!@#$%^&*()-_+=<>?/.,;:][{=}]" for char in password):
        score += 1
    else:
        message = "Password should include at least one special character."
    
    # Determine color based on score
    if score == 5:
        color = "green"
        message = "Password is strong."
    elif score == 4:
        color = "orange"
        message = "Password is decent but could be stronger."
    
    return score, color, message

def update_password_strength(*args):
    """
    Updates the GUI with the password strength.
    """
    password = password_var.get()
    score, color, message = check_password_strength(password)
    
    strength_label.config(text=message, fg=color)
    entry.config(bg=color)

def on_submit():
    """
    Checks the final password and displays a message.
    """
    password = password_var.get()
    score, color, message = check_password_strength(password)
    
    if score == 5:
        messagebox.showinfo("Success", "Your password is strong!")
    elif score == 3:
        messagebox.showinfo("Mild Warning", "You should try to make this stronger")
    else:
        messagebox.showwarning("Warning", "Common you can do better that this!")

# Set up the main application window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x200")

# Set up the StringVar for the password entry
password_var = tk.StringVar()
password_var.trace_add("write", update_password_strength)

# Add the entry for the password
entry = tk.Entry(root, textvariable=password_var, show="*", font=("Arial", 14), width=25)
entry.pack(pady=20)

# Add a label to show password strength
strength_label = tk.Label(root, text="Enter a password", font=("Arial", 12))
strength_label.pack(pady=10)

# Add a submit button
submit_button = tk.Button(root, text="Submit", command=on_submit, font=("Arial", 12))
submit_button.pack(pady=10)

# Start the GUI loop
root.mainloop()
