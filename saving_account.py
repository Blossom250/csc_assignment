from account import Account

class SavingAccount(Account):
    def __init__(self, balance):
        super().__init__(balance)


    def withdraw(self, amount,limit):
         if amount>limit:
             print("You Have exceeed you limit of transaction")
         else:
            super().withdraw(amount)