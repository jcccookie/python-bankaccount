###############################################################
#Classes
class Account:
   def __init__(self,acct_num,opening_bal):
      self.acct_num = acct_num
      self.bal = opening_bal

   def __str__(self):
      return f'${self.bal:.2f}'
   
   # Define a universal methods to accept deposits
   def deposit(self,dep_amt):
      self.bal += dep_amt

   # Define a universal methods to accept withdrawals
   def withdraw(self,with_amt):
      if self.bal >= with_amt:
         self.bal -= with_amt
      else:
         print('Funds Unavailable')


class Checking(Account):
   def __init__(self,acct_num,opening_bal):
      Account.__init__(self,acct_num,opening_bal)

   def __str__(self):
      return f"Checking Account: #{self.acct_num}\nBalance: {Account.__str__(self)}"

class Saving(Account):
   def __init__(self,acct_num,opening_bal):
      Account.__init__(self,acct_num,opening_bal)

   def __str__(self):
      return f"Saving Account: #{self.acct_num}\nBalance: {Account.__str__(self)}"

class Business(Account):
   def __init__(self,acct_num,opening_bal):
      Account.__init__(self,acct_num,opening_bal)

   def __str__(self):
      return f"Business Account: #{self.acct_num}\nBalance: {Account.__str__(self)}"      

class Customer:
   def __init__(self,name,pin):
      self.name = name
      self.pin = pin
      self.accts = {'C':[],'S':[],'B':[]}

   def __str__(self):
      return self.name

   def openChecking(self,acct_num,opening_deposit):
      self.accts['C'].append(Checking(acct_num,opening_deposit))
   
   def openSaving(self,acct_num,opening_deposit):
      self.accts['S'].append(Checking(acct_num,opening_deposit))

   def openBusiness(self,acct_num,opening_deposit):
      self.accts['B'].append(Checking(acct_num,opening_deposit))

   def getTotalDeposits(self):
      total = 0
      for acct in self.accts['C']:
         print(acct)
         total += acct.bal
      for acct in self.accts['S']:
         print(acct)
         total += acct.bal
      for acct in self.accts['B']:
         print(acct)
         total += acct.bal
      print(f'Combined Deposits: ${total:.2f}')

###############################################################
#Methods
def makeDeposit(customer,acct_type,acct_num,dep_amt):
   for acct in customer.accts[acct_type]:
      if acct.acct_num == acct_num:
         acct.deposit(dep_amt)


def makeWithdraw(customer,acct_type,acct_num,dep_amt):
   for acct in customer.accts[acct_type]:
      if acct.acct_num == acct_num:
         acct.withdraw(dep_amt)

###############################################################
#Main Program

nancy = Customer('Nancy',2)
nancy.openBusiness(2019,200)
nancy.getTotalDeposits()

makeWithdraw(nancy,'B',2019,110)
nancy.getTotalDeposits()