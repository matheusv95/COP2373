class BankAcct:
    #Start the BankAcct class with default values for balance and interest rate.
    def __init__(self, name, account_number, amount=0.0, interest_rate=0.0):
        # Stores the name, account number, initial balance, and interest rate.
        self.name = name
        self.account_number = account_number
        self.amount = amount
        self.interest_rate = interest_rate

    # Change the interest rate.
    def adjust_interest_rate(self, new_rate):
        """Adjusts the interest rate to the new specified rate."""
        self.interest_rate = new_rate

    # Deposit money into the account, check if the amount is positive and add to the current balance.
    def deposit(self, amount):
        """Deposits a specified amount to the account."""
        if amount > 0:
            self.amount += amount
            print(f"Deposited ${amount:.2f}")
        else:
            print("Deposit amount must be positive.")

    # Withdraw money from the account, check if the amount is available, and deduct from the current balance.
    def withdraw(self, amount):
        """Withdraws a specified amount from the account, if funds are sufficient."""
        if 0 < amount <= self.amount:
            self.amount -= amount
            print(f"Withdrew ${amount:.2f}")
        elif amount > self.amount:
            print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    # Check the current balance.
    def get_balance(self):
        return self.amount

    # Calculate interest for a given number of days.
    def calculate_interest(self, days):
        daily_rate = self.interest_rate / 365
        interest = self.amount * daily_rate * days
        return interest

    # Display account details as a string.
    def __str__(self):
        """Returns a string representation of the account balance and interest rate."""
        return (f"Account Holder: {self.name}\n"
                f"Account Number: {self.account_number}\n"
                f"Balance: ${self.amount:.2f}\n"
                f"Interest Rate: {self.interest_rate:.2%}")

# Test function for the BankAcct class
def test_bank_acct():
    # Create a BankAcct object with initial values
    account = BankAcct("Matheus H Hipolito", "123456789", 1000.0, 0.05)

    # Test depositing money into the account
    print("\nTesting deposit:")
    account.deposit(500.0)
    print(account)

    # Test withdrawing money from the account
    print("\nTesting withdrawal:")
    account.withdraw(200.0)
    print(account)

    # Test withdrawing more money than available in the account
    print("\nTesting insufficient funds withdrawal:")
    account.withdraw(2000.0)
    print(account)

    # Check the balance
    print("\nTesting balance retrieval:")
    print(f"Balance: ${account.get_balance():.2f}")

    # Test adjusting the interest rate
    print("\nTesting interest rate adjustment:")
    account.adjust_interest_rate(0.03)
    print(account)

    # Test calculating interest for a specific period (e.g., 30 days)
    print("\nTesting interest calculation for 30 days:")
    interest = account.calculate_interest(30)
    print(f"Interest for 30 days: ${interest:.2f}")

# Run the test function
if __name__ == "__main__":
    test_bank_acct()
