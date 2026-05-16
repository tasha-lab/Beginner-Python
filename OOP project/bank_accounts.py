class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self,initial_amt, acc_name):
        self.balance = initial_amt
        self.name = acc_name
        print(f"\nAccount '{self.name}' created.\nBalance= ${self.balance:.2f}")

    def getBalance(self):
        print(f"\nAccount '{self.name}', balance= ${self.balance:.2f}")

    def deposit(self,amount):
        self.balance= self.balance+amount
        print(f"\nDeposit complete")
        self.getBalance()

    def viableTrans(self,amount):
        if self.balance>=amount:
            return
        else:
            raise BalanceException(
                f"\nSorry, account '{self.name}' only has a balance of ${self.balance}"
            )
        
    def withdraw(self,amount):
        try:
            self.viableTrans(amount)
            self.balance=self.balance-amount
            print(f"\nWithdraw complete")
            self.getBalance()
        except BalanceException as error :
            print(f"\nWithdraw interrupted:{error}")

    def transfer(self,amount,account):
        try:
            print(f"\n**********\n\nBeginning transfer...🚀")
            self.viableTrans(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print(f"\nTransfer complete!✅\n\n**********")
        except BalanceException as error:
            print(f"Transfer interrupted!❌{error}")

class InterestRewardsAcc(BankAccount):
    def deposit(self, amount):
        self.balance=self.balance+(amount*1.05)
        print(f"Deposit complete")
        self.getBalance()

class SavingsAccount(InterestRewardsAcc):
    def __init__(self, initial_amt, acc_name):
        super().__init__(initial_amt, acc_name)
        self.fee=5

    def withdraw(self, amount):
        try:
            self.viableTrans(amount+self.fee )
            self.balance=self.balance-(amount+self.fee)
            print(f"Withdraw complete!!")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted:{error}")