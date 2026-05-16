from bank_accounts import *

Tasha = BankAccount(1000,'Tasha')
Sarah = BankAccount(3000,'Sarah')

Tasha.getBalance()
Sarah.getBalance()

Sarah.deposit(2000)
Tasha.deposit(2000)

Tasha.withdraw(10000)
Tasha.withdraw(500)

Tasha.transfer(10000,Sarah)
Tasha.transfer(1000,Sarah)

Jim = InterestRewardsAcc(5000,'Jim')

Jim.getBalance()
Jim.deposit(200)
Jim.transfer(100,Tasha)

Blaze = SavingsAccount(1000,'Blaze')
Blaze.getBalance()

Blaze.deposit(100)
Blaze.transfer(100,Sarah)
