import tkinter as tk
from tkinter import messagebox
import getpass

class ATM:
    def __init__(self, pin, balance=0):
        self.pin = pin
        self.balance = balance
        self.transaction_history = []

    # Validate PIN
    def validate_pin(self, input_pin):
        return input_pin == self.pin

    # Check Balance
    def check_balance(self):
        self.transaction_history.append(f"Balance inquiry: ${self.balance}")
        return f"Your current balance is: ${self.balance}"

    # Deposit Cash
    def deposit_cash(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Cash deposit: ${amount}")
            return f"${amount} deposited successfully!"
        return "Invalid deposit amount."

    # Withdraw Cash
    def withdraw_cash(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Cash withdrawal: ${amount}")
            return f"${amount} withdrawn successfully!"
        elif amount > self.balance:
            return "Insufficient balance."
        else:
            return "Invalid withdrawal amount."

    # Change PIN
    def change_pin(self, old_pin, new_pin):
        if self.validate_pin(old_pin):
            self.pin = new_pin
            self.transaction_history.append("PIN changed")
            return "PIN changed successfully!"
        return "Incorrect current PIN."

    # View Transaction History
    def view_transaction_history(self):
        if not self.transaction_history:
            return "No transactions yet."
        return "\n".join(self.transaction_history)


class ATM_GUI:
    def __init__(self, master):
        self.master = master
        self.master.title("ATM Machine")
        self.master.geometry("400x400")
        
        self.pin = "1234"  # Default PIN for simplicity
        self.atm = ATM(pin=self.pin, balance=1000)
        
        self.label = tk.Label(master, text="Enter your PIN", font=("Arial", 12))
        self.label.pack(pady=20)
        
        self.pin_entry = tk.Entry(master, show="*", font=("Arial", 12), width=10)
        self.pin_entry.pack(pady=10)
        
        self.enter_button = tk.Button(master, text="Enter", command=self.check_pin)
        self.enter_button.pack(pady=10)

    def check_pin(self):
        input_pin = self.pin_entry.get()
        if self.atm.validate_pin(input_pin):
            self.show_menu()
        else:
            messagebox.showerror("Error", "Incorrect PIN. Try again.")
    
    def show_menu(self):
        # Clear the window
        self.clear_window()

        # Show ATM menu options
        self.label = tk.Label(self.master, text="ATM Menu", font=("Arial", 16))
        self.label.pack(pady=20)
        
        buttons = [
            ("Check Balance", self.check_balance),
            ("Deposit Cash", self.deposit_cash),
            ("Withdraw Cash", self.withdraw_cash),
            ("Change PIN", self.change_pin),
            ("Transaction History", self.view_transaction_history),
            ("Exit", self.master.quit)
        ]
        
        for btn_text, command in buttons:
            button = tk.Button(self.master, text=btn_text, command=command, width=20, height=2)
            button.pack(pady=5)

    def check_balance(self):
        result = self.atm.check_balance()
        messagebox.showinfo("Balance Inquiry", result)

    def deposit_cash(self):
        self.clear_window()
        self.label = tk.Label(self.master, text="Enter amount to deposit:", font=("Arial", 12))
        self.label.pack(pady=20)
        
        self.amount_entry = tk.Entry(self.master, font=("Arial", 12))
        self.amount_entry.pack(pady=10)
        
        deposit_button = tk.Button(self.master, text="Deposit", command=self.handle_deposit)
        deposit_button.pack(pady=10)

    def handle_deposit(self):
        amount = float(self.amount_entry.get())
        result = self.atm.deposit_cash(amount)
        messagebox.showinfo("Deposit", result)
        self.show_menu()

    def withdraw_cash(self):
        self.clear_window()
        self.label = tk.Label(self.master, text="Enter amount to withdraw:", font=("Arial", 12))
        self.label.pack(pady=20)
        
        self.amount_entry = tk.Entry(self.master, font=("Arial", 12))
        self.amount_entry.pack(pady=10)
        
        withdraw_button = tk.Button(self.master, text="Withdraw", command=self.handle_withdrawal)
        withdraw_button.pack(pady=10)

    def handle_withdrawal(self):
        amount = float(self.amount_entry.get())
        result = self.atm.withdraw_cash(amount)
        messagebox.showinfo("Withdrawal", result)
        self.show_menu()

    def change_pin(self):
        self.clear_window()
        self.label = tk.Label(self.master, text="Enter current PIN and new PIN:", font=("Arial", 12))
        self.label.pack(pady=20)
        
        self.old_pin_entry = tk.Entry(self.master, show="*", font=("Arial", 12))
        self.old_pin_entry.pack(pady=5)
        self.old_pin_entry.insert(0, "Current PIN")

        self.new_pin_entry = tk.Entry(self.master, show="*", font=("Arial", 12))
        self.new_pin_entry.pack(pady=5)
        self.new_pin_entry.insert(0, "New PIN")
        
        change_pin_button = tk.Button(self.master, text="Change PIN", command=self.handle_change_pin)
        change_pin_button.pack(pady=10)

    def handle_change_pin(self):
        old_pin = self.old_pin_entry.get()
        new_pin = self.new_pin_entry.get()
        result = self.atm.change_pin(old_pin, new_pin)
        messagebox.showinfo("PIN Change", result)
        self.show_menu()

    def view_transaction_history(self):
        result = self.atm.view_transaction_history()
        messagebox.showinfo("Transaction History", result)

    def clear_window(self):
        for widget in self.master.winfo_children():
            widget.destroy()


# Run the ATM GUI
if __name__ == "__main__":
    root = tk.Tk()
    atm_gui = ATM_GUI(root)
    root.mainloop()
