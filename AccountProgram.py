class Account:
    def __init__(self,accountID,balance):
        self.accountID = accountID
        self.balance = balance
    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance = self.balance - amount
        else:
            print("Insufficent balance")
    def deposit(self,amount):
        self.balance = self.balance+amount
        print(self.balance)

    def getBalance(self):
        return self.balance

john = Account(1001,4500)# calling accountID,balance
veta = Account(1002,1)
john.deposit(2000)
veta.deposit(1)
print(john.getBalance())
print(veta.getBalance())
