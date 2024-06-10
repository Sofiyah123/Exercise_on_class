class Account:
    def __init__(self, account_number: str, account_holder: str, balance: float = 0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def __str__(self):
        return f"Account({self.account_number}, {self.account_holder}, Balance: {self.balance:.2f})"

    def deposit(self, amount: float):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount:.2f}. New balance: {self.balance:.2f}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount: float):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount:.2f}. New balance: {self.balance:.2f}")
        else:
            print("Insufficient funds or invalid amount.")

    def transfer(self, amount: float, other_account):
        if not isinstance(other_account, Account):
#The main essence of this aspect is to essure other 
#acct conform with the pertain use by the main acct
            print("Transfer failed. The recipient must be an instance of Account.")
            return

        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            other_account.balance += amount
            print(f"Transferred {amount:.2f} to account {other_account.account_number}. New balance: {self.balance:.2f}")
            print(f"Recipient's new balance: {other_account.balance:.2f}")
        else:
            print("Insufficient funds or invalid amount.")


class Bank:
    def __init__(self):
        self.accounts = []
    
    def find_account(self, account_number: str):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
            return None

    def create_account(self, account_number: str, account_holder: str, balance: float = 0.0):
        if self.find_account(account_number):
            print("Account with this number already exists.")
            return
        new_account = Account(account_number, account_holder, balance)
        self.accounts.append(new_account)
        print(f"Created new account: {new_account}")

    

    def deposit_to_account(self, account_number: str, amount: float):
        account = self.find_account(account_number)
        if account:
            account.deposit(amount)
        else:
            print("Account not found.")

    def withdraw_from_account(self, account_number: str, amount: float):
        account = self.find_account(account_number)
        if account:
            account.withdraw(amount)
        else:
            print("Account not found.")

    def transfer_between_accounts(self, from_account_number: str, to_account_number: str, amount: float):
        from_account = self.find_account(from_account_number)
        to_account = self.find_account(to_account_number)
        if from_account and to_account:
            from_account.transfer(amount, to_account)
        else:
            print("One or both accounts not found.")

    def view_all_accounts(self):
        if not self.accounts:
            print("No accounts in the bank.")
        for account in self.accounts:
            print(account)


def user_interface():
    bank = Bank()

    while True:
        print("\nBank Menu:")
        print("1. Create a new account")
        print("2. Deposit to an account")
        print("3. Withdraw from an account")
        print("4. Transfer between accounts")
        print("5. View all accounts")
        print("6. Find an account by account number")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            account_number = input("Enter account number: ")
            account_holder = input("Enter account holder name: ")
            balance = float(input("Enter initial balance: "))
            bank.create_account(account_number, account_holder, balance)
        elif choice == "2":
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount to deposit: "))
            bank.deposit_to_account(account_number, amount)
        elif choice == "3":
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount to withdraw: "))
            bank.withdraw_from_account(account_number, amount)
        elif choice == "4":
            from_account_number = input("Enter from account number: ")
            to_account_number = input("Enter to account number: ")
            amount = float(input("Enter amount to transfer: "))
            bank.transfer_between_accounts(from_account_number, to_account_number, amount)
        elif choice == "5":
            bank.view_all_accounts()
        elif choice == "6":
            account_number = input("Enter account number: ")
            account = bank.find_account(account_number)
            if account:
                print(account)
            else:
                print("Account not found.")
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")


user_interface()
