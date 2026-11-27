class BankAccount:
    def __init__(self, account_number: str):
        # Strip spaces to store raw 26 digits cleanly
        digits = account_number.replace(" ", "")
        if len(digits) != 26 or not digits.isdigit():
            raise ValueError("Bank account number must consist of exactly 26 digits.")
        self.account_number = digits
        self.balance = 0.0

    def deposit(self, amount: float):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount: float):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds on the account")

    def _format_account_number(self):
        # Format as: 2 digits + six groups of 4 digits
        first_two = self.account_number[:2]
        groups = [self.account_number[i:i + 4] for i in range(2, 26, 4)]
        return f"{first_two} {' '.join(groups)}"

    def display(self):
        formatted_no = self._format_account_number()
        formatted_balance = f"{self.balance:.2f}".replace(".", ",")
        print(f"Bank Account No: {formatted_no}")
        print(f"Balance: PLN {formatted_balance}")


# 1. Create a bank account
account = BankAccount("12 3456 5555 9090 1111 0000 7722")

# 2. Display account balance
account.display()
print()

# 3. Deposit PLN 25,30
account.deposit(25.30)

# 4. Display account balance
account.display()
print()

# 5. Withdraw PLN 31,70
account.withdraw(31.70)

# 6. Display account balance
account.display()
print()

# 7. Withdraw PLN 14
account.withdraw(14.00)

# 8. Display account balance
account.display()