class Bank_Account:
    def __init__(self):
        self.balance=0

    def deposit(self):
        amount=float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited:",amount)
 
    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance>=amount:
            self.balance-=amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")
    def display(self):
        print("\n your Balance=",self.balance)
print("Hello...!")
input("Account holder name:")
input("Acc.no:") 
s = Bank_Account()
s.deposit()
s.withdraw()
s.display()
