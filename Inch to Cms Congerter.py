import tkinter as tk

# Function to convert inches to centimeters
def convert_to_cm():
    try:
        inches = float(entry_inches.get())  # Get value from the entry box
        cm = inches * 2.54  # Convert inches to centimeters
        label_result.config(text=f"{inches} inches = {cm} cm")  # Update result label
    except ValueError:
        label_result.config(text="Please enter a valid number")

# Create the main window
root = tk.Tk()
root.title("Inch to Centimeter Converter")

# Create the input field and label
label_prompt = tk.Label(root, text="Enter value in inches:")
label_prompt.pack()

entry_inches = tk.Entry(root)
entry_inches.pack()

# Create a convert button
button_convert = tk.Button(root, text="Convert", command=convert_to_cm)
button_convert.pack()

# Create a label to display the result
label_result = tk.Label(root, text="Result will appear here")
label_result.pack()

# Run the Tkinter event loop
root.mainloop()
