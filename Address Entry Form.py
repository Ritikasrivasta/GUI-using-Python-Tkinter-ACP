import tkinter as tk

# Function to handle form submission
def submit_form():
    name = entry_name.get()
    street = entry_street.get()
    city = entry_city.get()
    state = entry_state.get()
    zip_code = entry_zip.get()

    # Display the entered data in the result label
    label_result.config(text=f"Name: {name}\nStreet: {street}\nCity: {city}\nState: {state}\nZIP Code: {zip_code}")

# Create the main window
root = tk.Tk()
root.title("Address Entry Form")

# Create labels and entry fields for the form
label_name = tk.Label(root, text="Name:")
label_name.grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=5)

label_street = tk.Label(root, text="Street Address:")
label_street.grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_street = tk.Entry(root)
entry_street.grid(row=1, column=1, padx=10, pady=5)

label_city = tk.Label(root, text="City:")
label_city.grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry_city = tk.Entry(root)
entry_city.grid(row=2, column=1, padx=10, pady=5)

label_state = tk.Label(root, text="State:")
label_state.grid(row=3, column=0, padx=10, pady=5, sticky="e")
entry_state = tk.Entry(root)
entry_state.grid(row=3, column=1, padx=10, pady=5)

label_zip = tk.Label(root, text="ZIP Code:")
label_zip.grid(row=4, column=0, padx=10, pady=5, sticky="e")
entry_zip = tk.Entry(root)
entry_zip.grid(row=4, column=1, padx=10, pady=5)

# Create the submit button
button_submit = tk.Button(root, text="Submit", command=submit_form)
button_submit.grid(row=5, column=0, columnspan=2, pady=10)

# Create a label to display the submitted data
label_result = tk.Label(root, text="Your address will appear here", justify="left")
label_result.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Run the Tkinter event loop
root.mainloop()
