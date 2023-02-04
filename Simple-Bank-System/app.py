class BankAccount():
    # Class variables
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    
    # Class methods
    # Method to deposit money
    def deposit(self, amount):
        self.balance += amount
        print("You have deposited", amount, "in your account.")
    # Method to withdraw money
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("You have withdrawn", amount, "from your account.")
        else:
            print("Insufficient balance.")
    # Method to display account details
    def display(self):
        print("Name:", self.name)
        print("Balance:", self.balance)
    
# Create an object of the class
account = BankAccount("John", 1000)
# Display account details
account.display()
# Deposit money
account.deposit(500)
# Display account details
account.display()
# Withdraw money
account.withdraw(2000)
# Display account details
account.display()