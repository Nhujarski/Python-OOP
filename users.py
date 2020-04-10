class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
    	self.account_balance += amount	
        return self
    def make_withdrawl(self,amount):
        self.account_balance -= amount
        return self 

    def display_user_balance(self):
        print(self.name,self.account_balance)
        return self

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self

nick = User("Nickolas Hujarski", "nick@python.com")
mike = User("Mike Mchalffey", "mike@python.com")
marshall = User("Marshall Mchalffey", "marsh@python.com")

mike.make_deposit(100).make_deposit(100).make_deposit(100).make_withdrawl(10).display_user_balance()

# print(mike.account_balance)

# print(mike.account_balance)

# ********************
nick.make_deposit(100).make_deposit(100).make_withdrawl(50).display_user_balance()
# ************************
marshall.make_deposit(100).make_withdrawl(20).make_withdrawl(20).make_withdrawl(20).display_user_balance()
# ****************
mike.transfer_money(marshall,50).display_user_balance()

marshall.display_user_balance()
