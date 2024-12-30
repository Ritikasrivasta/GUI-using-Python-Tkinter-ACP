import tkinter as tk
import random
import string

# Function to generate a random password
def generate_password():
    length = int(entry_length.get())
    use_uppercase = checkbox_uppercase.var.get()
    use_numbers = checkbox_numbers.var.get()
    use_symbols = checkbox_symbols.var.get()

    # Define character sets
    char_sets = string.ascii_lowercase  # always include lowercase letters
    if use_uppercase:
        char_sets += string.ascii_uppercase
    if use_numbers:
        char_sets += string.digits
    if use_symbols:
        char_sets += string.punctuation

    # Generate a random password
    password = ''.join(random.choice(char_sets) for _ in range(length))
    entry_password.delete(0, tk.END)  # Clear the previous password
    entry_password.insert(0, password)  # Insert the generated password

# Create the main window
root = tk.Tk()
root.title("Random Password Generator")

# Create a label for password length
label_length = tk.Label(root, text="Password Length:")
label_length.grid(row=0, column=0, padx=10, pady=5, sticky="e")

# Create an entry field for the password length
entry_length = tk.Entry(root)
entry_length.grid(row=0, column=1, padx=10, pady=5)
entry_length.insert(0, "12")  # Default length of 12

# Checkbox options for including uppercase letters, numbers, and symbols
checkbox_uppercase = tk.Checkbutton(root, text="Include Uppercase", var=tk.BooleanVar())
checkbox_uppercase.grid(row=1, column=0, padx=10, pady=5, columnspan=2, sticky="w")

checkbox_numbers = tk.Checkbutton(root, text="Include Numbers", var=tk.BooleanVar())
checkbox_numbers.grid(row=2, column=0, padx=10, pady=5, columnspan=2, sticky="w")

checkbox_symbols = tk.Checkbutton(root, text="Include Symbols", var=tk.BooleanVar())
checkbox_symbols.grid(row=3, column=0, padx=10, pady=5, columnspan=2, sticky="w")

# Button to generate the password
button_generate = tk.Button(root, text="Generate Password", command=generate_password)
button_generate.grid(row=4, column=0, columnspan=2, pady=10)

# Create a label for displaying the generated password
label_password = tk.Label(root, text="Generated Password:")
label_password.grid(row=5, column=0, padx=10, pady=5, sticky="e")

# Entry to display the generated password
entry_password = tk.Entry(root, width=30)
entry_password.grid(row=5, column=1, padx=10, pady=5)

# Run the Tkinter event loop
root.mainloop()
