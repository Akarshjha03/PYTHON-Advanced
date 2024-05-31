'''Create a BankAccount class:
Attributes: account_number, balance
Methods: deposit(amount), withdraw(amount)'''

class BankAccount:
    def __init__(self,account_number,balance):
        self.account_number=account_number
        self.balance=balance

    def deposite(self):
        amount = float(input("Enter the amount you want to deposite:"))
        self.balance +=  amount
        print ("Deposited Amount is :",amount)

    def withdraw(self,):
        new_amount=float(input('Enter the amount you want to withdraw:'))
        if (new_amount<=self.balance):
            print ("Amount withdrawn is :",new_amount)
            newbalance = self.balance - new_amount
            print(f"The current balance of your Account is {newbalance}")
        else:
            print("Insufficient Balance")
        

per1=BankAccount(23,500)
per1.deposite()
per1.withdraw()

per2=BankAccount(24,200)
per2.deposite()
per2.withdraw()
