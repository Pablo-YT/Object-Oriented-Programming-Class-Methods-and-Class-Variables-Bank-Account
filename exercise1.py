class Bank_Account:
    """docstring for Bank_Account"""

    interest_rate = float()
    accounts = []

    # Create account
    @classmethod
    def create(cls):
        ac = Bank_Account()
        cls.accounts.append(ac)
        return ac

        # total funds

    @classmethod
    def total_funds(cls):
        total = 0
        for acc in range(0, len(cls.accounts)):
            total += cls.accounts[acc].balance
            return total

            # interest in time

    @classmethod
    def interest_time(cls):
        for acc in range(0, len(cls.accounts)):
            acc_id = cls.accounts[acc]
            acc_id.balance = acc_id.balance * (1 + acc_id.interest_rate / 100)

    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount


my_account = Bank_Account.create()
your_account = Bank_Account.create()
print(my_account.balance)  # 0
print(Bank_Account.total_funds())  # 0
my_account.deposit(2000)  # 2000
your_account.deposit(3000)  # 3000
print(my_account.balance)
print(your_account.balance)  # 2000
print(Bank_Account.total_funds())  # 2000
Bank_Account.interest_time()
print(my_account.balance)  # 3000
print(your_account.balance)  # 2000
print(Bank_Account.total_funds())  # 1500
my_account.withdraw(500)
print(my_account.balance)  # 1500
print(Bank_Account.total_funds())
