import tkinter as tk
from tkinter import messagebox
import string
import random

def generate_password():
    try:
        # Get the desired length of the password from the entry widget
        length = int(length_entry.get())
        
        if length < 4:
            messagebox.showerror("Error", "Password length should be at least 4 characters.")
            return

        # Define the characters to use in the password
        characters = string.ascii_letters + string.digits + string.punctuation
        
        # Generate a random password
        password = ''.join(random.choice(characters) for _ in range(length))
        
        # Display the generated password
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
    
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create and place the widgets
length_label = tk.Label(root, text="Enter password length:")
length_label.pack(pady=10)

length_entry = tk.Entry(root)
length_entry.pack(pady=5)

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

password_label = tk.Label(root, text="Generated password:")
password_label.pack(pady=10)

password_entry = tk.Entry(root, width=50)
password_entry.pack(pady=5)

# Run the main event loop
root.mainloop()
