import tkinter as tk
from tkinter import messagebox

# Function to calculate Simple Interest
def calculate_si():
    try:
        # Get values from user input
        p = float(principal_entry.get())
        r = float(rate_entry.get())
        t = float(time_entry.get())

        # Formula for Simple Interest
        si = (p * r * t) / 100

        # Display the result
        result_label.config(text=f"Simple Interest: ₹{si:.2f}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric values!")

# Create main window
root = tk.Tk()
root.title("Simple Interest Calculator")
root.geometry("350x300")
root.config(bg="#e6e6ff")

# Heading
tk.Label(root, text="Simple Interest Calculator", font=("Arial", 16, "bold"), bg="#e6f5ff").pack(pady=10)

# Principal
tk.Label(root, text="Principal (₹):", font=("Arial", 12), bg="#e9e6ff").pack()
principal_entry = tk.Entry(root, width=25)
principal_entry.pack(pady=5)

# Rate
tk.Label(root, text="Rate (%):", font=("Arial", 12), bg="#e6e7ff").pack()
rate_entry = tk.Entry(root, width=25)
rate_entry.pack(pady=5)

# Time
tk.Label(root, text="Time (Years):", font=("Arial", 12), bg="#e9e6ff").pack()
time_entry = tk.Entry(root, width=25)
time_entry.pack(pady=5)

# Calculate Button
tk.Button(root, text="Calculate", font=("Arial", 12), bg="#0078ff", fg="white", command=calculate_si).pack(pady=10)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 13, "bold"), bg="#e6e6ff", fg="green")
result_label.pack(pady=10)

# Run the GUI loop
root.mainloop()