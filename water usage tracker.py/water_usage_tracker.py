import tkinter as tk
from tkinter import messagebox

usage_log = []
def add_usage():
    try:
        value = float(entry.get())
        if value <= 0:
            raise ValueError
        usage_log.append(value)
        update_display()
        entry.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a positive number.")


def update_display():
    total = sum(usage_log)
    total_label.config(text=f"Total Water Used: {total:.2f} Liters")
    log_list.delete(0, tk.END)
    for i, val in enumerate(usage_log, start=1):
        log_list.insert(tk.END, f"{i}. {val:.2f} L")

def reset_data():
    if messagebox.askyesno("Reset", "Are you sure you want to clear all data?"):
        usage_log.clear()
        update_display()

app = tk.Tk()
app.title("EcoDrops – Water Usage Tracker")
app.geometry("400x400")
app.resizable(False, False)
app.configure(bg="#e0f7fa")

heading = tk.Label(app, text="EcoDrops 💧", font=("Helvetica", 20, "bold"), bg="#e0f7fa", fg="#00796b")
heading.pack(pady=10)

entry = tk.Entry(app, font=("Helvetica", 14), justify="center")
entry.pack(pady=10)

add_button = tk.Button(app, text="Add Usage", command=add_usage, font=("Helvetica", 12), bg="#4db6ac", fg="white")
add_button.pack(pady=5)

reset_button = tk.Button(app, text="Reset Data", command=reset_data, font=("Helvetica", 12), bg="#e57373", fg="white")
reset_button.pack(pady=5)

total_label = tk.Label(app, text="Total Water Used: 0.00 Liters", font=("Helvetica", 14), bg="#e0f7fa")
total_label.pack(pady=10)

log_label = tk.Label(app, text="Usage Log:", font=("Helvetica", 12, "bold"), bg="#e0f7fa")
log_label.pack()

log_list = tk.Listbox(app, height=8, font=("Helvetica", 12), width=30, justify="center")
log_list.pack(pady=5)

# Start the GUI loop
app.mainloop()
