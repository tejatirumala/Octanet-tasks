import tkinter as tk
from tkinter import messagebox, filedialog
from collections import namedtuple

class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)

    def total_cost(self):
        return self.price * self.quantity

class ReceiptCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Receipt Calculator")
        self.items = []

        # GUI Layout
        self.setup_gui()

    def setup_gui(self):
        # Labels and Entry Fields
        self.label_name = tk.Label(self.root, text="Item Name")
        self.label_name.grid(row=0, column=0, padx=10, pady=5)
        
        self.entry_name = tk.Entry(self.root)
        self.entry_name.grid(row=0, column=1, padx=10, pady=5)

        self.label_price = tk.Label(self.root, text="Price")
        self.label_price.grid(row=1, column=0, padx=10, pady=5)

        self.entry_price = tk.Entry(self.root)
        self.entry_price.grid(row=1, column=1, padx=10, pady=5)

        self.label_quantity = tk.Label(self.root, text="Quantity")
        self.label_quantity.grid(row=2, column=0, padx=10, pady=5)

        self.entry_quantity = tk.Entry(self.root)
        self.entry_quantity.grid(row=2, column=1, padx=10, pady=5)

        self.add_button = tk.Button(self.root, text="Add Item", command=self.add_item)
        self.add_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        # Text widget to display items
        self.text_receipt = tk.Text(self.root, width=40, height=10)
        self.text_receipt.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        # Tax, Discount, and Final Total Labels
        self.label_tax = tk.Label(self.root, text="Tax (%)")
        self.label_tax.grid(row=5, column=0, padx=10, pady=5)

        self.entry_tax = tk.Entry(self.root)
        self.entry_tax.grid(row=5, column=1, padx=10, pady=5)

        self.label_discount = tk.Label(self.root, text="Discount (%)")
        self.label_discount.grid(row=6, column=0, padx=10, pady=5)

        self.entry_discount = tk.Entry(self.root)
        self.entry_discount.grid(row=6, column=1, padx=10, pady=5)

        self.calculate_button = tk.Button(self.root, text="Calculate Total", command=self.calculate_total)
        self.calculate_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

        # Save Receipt Button
        self.save_button = tk.Button(self.root, text="Save Receipt", command=self.save_receipt)
        self.save_button.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

    def add_item(self):
        # Add item to the list and display
        name = self.entry_name.get()
        price = self.entry_price.get()
        quantity = self.entry_quantity.get()

        if name and price and quantity:
            item = Item(name, price, quantity)
            self.items.append(item)
            self.display_items()
            self.clear_inputs()
        else:
            messagebox.showwarning("Input Error", "Please fill all fields!")

    def display_items(self):
        # Clear text widget and display all items
        self.text_receipt.delete(1.0, tk.END)
        for item in self.items:
            self.text_receipt.insert(tk.END, f"{item.name}\tPrice: ${item.price:.2f}\tQty: {item.quantity}\tTotal: ${item.total_cost():.2f}\n")

    def clear_inputs(self):
        self.entry_name.delete(0, tk.END)
        self.entry_price.delete(0, tk.END)
        self.entry_quantity.delete(0, tk.END)

    def calculate_total(self):
        try:
            subtotal = sum(item.total_cost() for item in self.items)
            tax = float(self.entry_tax.get()) if self.entry_tax.get() else 0
            discount = float(self.entry_discount.get()) if self.entry_discount.get() else 0

            tax_amount = subtotal * (tax / 100)
            discount_amount = subtotal * (discount / 100)
            final_total = subtotal + tax_amount - discount_amount

            self.text_receipt.insert(tk.END, f"\nSubtotal: ${subtotal:.2f}\nTax: ${tax_amount:.2f}\nDiscount: ${discount_amount:.2f}\nFinal Total: ${final_total:.2f}\n")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers for tax and discount.")

    def save_receipt(self):
        # Save the receipt as a text file
        receipt_data = self.text_receipt.get(1.0, tk.END)
        if receipt_data.strip():
            file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
            if file_path:
                with open(file_path, 'w') as file:
                    file.write(receipt_data)
                messagebox.showinfo("Receipt Saved", f"Receipt saved at {file_path}")
        else:
            messagebox.showwarning("No Data", "No receipt data to save!")

if __name__ == "__main__":
    root = tk.Tk()
    app = ReceiptCalculator(root)
    root.mainloop()
