import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    user_input = length_entry.get()

    try:
        length = int(user_input)
        if length < 4:
            messagebox.showwarning("Invalid Input", "Password length must be at least 4.")
            return

        # Generate a new password of the given length
        characters = string.ascii_letters + string.digits + string.punctuation

        password = [
            random.choice(string.ascii_lowercase),
            random.choice(string.ascii_uppercase),
            random.choice(string.digits),
            random.choice(string.punctuation)
        ]

        # Fill the rest
        password += random.choices(characters, k=length - 4)
        random.shuffle(password)

        result_var.set(''.join(password))

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

# --- GUI Setup ---
app = tk.Tk()
app.title("Password Generator")
app.geometry("400x250")
app.configure(bg="#f0f0f0")

tk.Label(app, text="Password Generator", font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=10)

tk.Label(app, text="Enter desired password length:", bg="#f0f0f0").pack()
length_entry = tk.Entry(app, justify="center", width=20, font=("Arial", 12))
length_entry.pack(pady=5)

tk.Button(app, text="Generate Password", command=generate_password, font=("Arial", 12), bg="#4caf50", fg="white").pack(pady=10)

result_var = tk.StringVar()
tk.Entry(app, textvariable=result_var, font=("Arial", 12), width=30, justify="center", state="readonly").pack(pady=5)

app.mainloop()
