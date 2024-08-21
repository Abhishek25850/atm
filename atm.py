class ATM:
    def __init__(self, pin, balance=0):
        self.pin = pin
        self.balance = balance
        self.transaction_history = []

    def verify_pin(self):
        entered_pin = input("Enter your PIN: ")
        return entered_pin == self.pin

    def account_balance(self):
        print(f"Your current balance is: ${self.balance:.2f}")
        self.transaction_history.append(f"Checked balance: ${self.balance:.2f}")

    def cash_withdrawal(self):
        amount = float(input("Enter the amount to withdraw: $"))
        if amount <= 0:
            print("Please enter a valid amount.")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"You have withdrawn: ${amount:.2f}")
            print(f"New balance: ${self.balance:.2f}")
            self.transaction_history.append(f"Withdrew: ${amount:.2f}, New balance: ${self.balance:.2f}")

    def cash_deposit(self):
        amount = float(input("Enter the amount to deposit: $"))
        if amount <= 0:
            print("Please enter a valid amount.")
        else:
            self.balance += amount
            print(f"You have deposited: ${amount:.2f}")
            print(f"New balance: ${self.balance:.2f}")
            self.transaction_history.append(f"Deposited: ${amount:.2f}, New balance: ${self.balance:.2f}")

    def change_pin(self):
        new_pin = input("Enter your new PIN: ")
        if new_pin == self.pin:
            print("The new PIN cannot be the same as the old PIN.")
        elif len(new_pin) != 4 or not new_pin.isdigit():
            print("PIN must be exactly 4 digits.")
        else:
            self.pin = new_pin
            print("PIN successfully changed.")
            self.transaction_history.append("PIN changed.")

    def print_transaction_history(self):
        if not self.transaction_history:
            print("No transactions found.")
        else:
            print("Transaction History:")
            for transaction in self.transaction_history:
                print(transaction)

def main():
    atm = ATM(pin="0101", balance=1000.00)  

    while True:
        if atm.verify_pin():
            while True:
                print("\nATM Menu")
                print("1. Account Balance Inquiry")
                print("2. Cash Withdrawal")
                print("3. Cash Deposit")
                print("4. Change PIN")
                print("5. Transaction History")
                print("6. Exit")
                
                choice = input("Enter your choice: ")

                if choice == '1':
                    atm.account_balance()

                elif choice == '2':
                    atm.cash_withdrawal()

                elif choice == '3':
                    atm.cash_deposit()

                elif choice == '4':
                    atm.change_pin()

                elif choice == '5':
                    atm.print_transaction_history()

                elif choice == '6':
                    print("Thank you for using the ATM. Goodbye!")
                    return

                else:
                    print("Invalid choice. Please try again.")
        else:
            print("Incorrect PIN. Please try again.")

if __name__ == "__main__":
    main()
