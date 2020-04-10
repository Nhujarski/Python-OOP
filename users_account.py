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


class User:
    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.account = Bankaccount(int_rate =0.02, balance=0)

    def make_deposit(self,amount):	# takes an argument that is the amount of the deposit
    	self.account.deposit(amount)	
        return self
    def make_withdrawl(self,amount):
        self.account.withdraw(amount)
        return self 

    def display_user_balance(self):
        self.account.display_account_info()
        return self

    def transfer_money(self, other_user, amount):
        self.account.withdraw(amount)
        other_user.account.deposit(amount)
        return self

    
nick = User("Nick","nick@python")
nick.make_deposit(100).make_deposit(100).make_withdrawl(50).display_user_balance()
mike = User("Mike", "mike@python.com")

mike.make_deposit(50).display_user_balance()
nick.transfer_money(mike,50).display_user_balance()
# mike.yield_interest()
mike.display_user_balance()