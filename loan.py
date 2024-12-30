import tkinter as tk
from tkinter import messagebox, ttk
import json
import os

# File to store data
DATA_FILE = "loans.json"

# Load existing data or create a new one
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return []

def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

# Add a loan
def add_loan():
    name = name_entry.get().strip()
    amount = amount_entry.get().strip()

    if not name or not amount:
        messagebox.showerror("Error", "Both fields are required.")
        return

    try:
        amount = float(amount)
    except ValueError:
        messagebox.showerror("Error", "Amount must be a number.")
        return

    loans.append({"name": name, "amount": amount, "status": "Pending"})
    save_data(loans)
    update_table()
    name_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    messagebox.showinfo("Success", "Loan added successfully!")

# Update the table view
def update_table():
    for row in table.get_children():
        table.delete(row)
    for idx, loan in enumerate(loans, start=1):
        table.insert("", "end", values=(idx, loan["name"], loan["amount"], loan["status"]))

# Mark loan as repaid
def mark_repaid():
    selected_item = table.selection()
    if not selected_item:
        messagebox.showerror("Error", "Please select a loan to update.")
        return

    idx = int(table.item(selected_item)["values"][0]) - 1
    loans[idx]["status"] = "Repaid"
    save_data(loans)
    update_table()
    messagebox.showinfo("Success", "Loan marked as repaid.")

# Delete a loan
def delete_loan():
    selected_item = table.selection()
    if not selected_item:
        messagebox.showerror("Error", "Please select a loan to delete.")
        return

    idx = int(table.item(selected_item)["values"][0]) - 1
    loans.pop(idx)
    save_data(loans)
    update_table()
    messagebox.showinfo("Success", "Loan deleted.")

# Search loans
def search_loan():
    query = search_entry.get().strip().lower()
    for row in table.get_children():
        table.delete(row)
    results = [loan for loan in loans if query in loan["name"].lower()]
    for idx, loan in enumerate(results, start=1):
        table.insert("", "end", values=(idx, loan["name"], loan["amount"], loan["status"]))

# Main GUI
loans = load_data()

root = tk.Tk()
root.title("Loan Tracker")
root.geometry("600x400")

# Add Loan Section
tk.Label(root, text="Name:").grid(row=0, column=0, padx=5, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Amount:").grid(row=0, column=2, padx=5, pady=5)
amount_entry = tk.Entry(root)
amount_entry.grid(row=0, column=3, padx=5, pady=5)

add_button = tk.Button(root, text="Add Loan", command=add_loan,background="blue")
add_button.grid(row=0, column=4, padx=5, pady=5)

# Search Section
tk.Label(root, text="Search:").grid(row=1, column=0, padx=5, pady=5)
search_entry = tk.Entry(root)
search_entry.grid(row=1, column=1, padx=5, pady=5)
search_button = tk.Button(root, text="Search", command=search_loan)
search_button.grid(row=1, column=2, padx=5, pady=5)

# Loan Table
columns = ("#", "Name", "Amount", "Status")
table = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    table.heading(col, text=col)
    table.column(col, anchor=tk.CENTER)
table.grid(row=2, column=0, columnspan=5, padx=5, pady=10, sticky="nsew")

# Scrollbar for table
scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=table.yview)
table.configure(yscroll=scrollbar.set)
scrollbar.grid(row=2, column=5, sticky="ns")

# Actions Section
repaid_button = tk.Button(root, text="Mark as Repaid", command=mark_repaid)
repaid_button.grid(row=3, column=3, padx=5, pady=5)

delete_button = tk.Button(root, text="Delete Loan", command=delete_loan)
delete_button.grid(row=3, column=4, padx=5, pady=5)

# Initialize table view
update_table()

# Start the GUI
root.mainloop()
