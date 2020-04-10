class Bankaccount:

    def __init__(self, balance , int_rate=0.01 ):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self,amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print("Balance is: "+ "$" + str(self.balance))
        return self

    def yield_interest(self):
        self.balance = self.balance + self.balance * self.int_rate
        return self

user1 = Bankaccount(100,0.02)
user2 = Bankaccount(200)
user1.deposit(50).deposit(50).deposit(50).withdraw(50).yield_interest().display_account_info()
