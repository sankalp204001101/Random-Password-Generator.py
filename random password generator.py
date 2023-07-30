import tkinter as tk
import random
import string

def generate_password():
    password_strength = strength_var.get()
    password_length = length_var.get()
    
    if password_strength == "Weak":
        chars = string.ascii_lowercase
    elif password_strength == "Medium":
        chars = string.ascii_letters + string.digits
    else:
        chars = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(chars) for _ in range(password_length))
    result_label.config(text="Generated Password: " + password)

# Create the main window
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("600x300")

# Password Strength selection
strength_var = tk.StringVar()
strength_var.set("Weak")
strength_label = tk.Label(root, text="Select Password Strength:")
strength_label.pack()

strength_choices = ["Weak", "Medium", "Strong"]
for choice in strength_choices:
    tk.Radiobutton(root, text=choice, variable=strength_var, value=choice).pack()

# Password Length selection
length_var = tk.IntVar()
length_var.set(8)  # Default password length is 8 characters
length_label = tk.Label(root, text="Enter Password Length:")
length_label.pack()

length_entry = tk.Entry(root, textvariable=length_var)
length_entry.pack()

# Generate Password Button
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

# Label to display the generated password
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()




