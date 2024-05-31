'''A program that models a bank account, with classes for the account, the customer, 
and the bank.'''

class Customer:
    def __init__(self, name, address):
        self.name = name
        self.address = address

class Account:
    def __init__(self, customer, balance=0):
        self.customer = customer
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
            return
        self.balance -= amount
        return self.balance

class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def get_total_balance(self):
        return sum(account.balance for account in self.accounts)

# Usage
customer1 = Customer("Akarsh Jha", "Waghodia")
account1 = Account(customer1, 23000)
bank = Bank()
bank.add_account(account1)

print(bank.get_total_balance()) 