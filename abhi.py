class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, initial_balance):
        if account_number not in self.accounts:
            self.accounts[account_number] = initial_balance
            print(f"Account {account_number} created with an initial balance of {initial_balance}.")
    def check_balance(self, account_number):
        if account_number in self.accounts:
            balance = self.accounts[account_number]
            print(f"Account {account_number} has a balance of {balance}.")
        else:
            print(f"Account {account_number} not found.")
def main():
    bank = Bank()

    while True:
        print("\nSTATE BANK OF INDIA")
        print("1. Create Account")
        print("2. Check Balance")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            account_number = input("Enter account number: ")
            initial_balance = float(input("Enter initial balance: "))
            bank.create_account(account_number, initial_balance) 
            
        elif choice == "2":
            account_number = input("Enter account number: ")
            bank.check_balance(account_number) 
            
        elif choice == "3":
            print("Exiting STATE BANK OF INDIA. THANK YOU , VISIT AGAIN!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")



main()


