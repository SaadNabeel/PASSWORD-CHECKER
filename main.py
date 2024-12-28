import tkinter as tk

def check_password_strength():
    password = password_entry.get()
    length = len(password)
    if length < 6:
        strength_label.config(text="Weak", fg="red")
    elif 6 <= length <= 10:
        strength_label.config(text="Medium", fg="orange")
    else:
        strength_label.config(text="Strong", fg="green")


root = tk.Tk()
root.title("Password Strength Checker")


tk.Label(root, text="Enter your password:").grid(row=0, column=0, padx=10, pady=10)

password_entry = tk.Entry(root, show="*")
password_entry.grid(row=0, column=1, padx=10, pady=10)

check_button = tk.Button(root, text="Check Strength", command=check_password_strength)
check_button.grid(row=1, column=0, columnspan=2, pady=10)

strength_label = tk.Label(root, text="")
strength_label.grid(row=2, column=0, columnspan=2, pady=10)


root.mainloop()
