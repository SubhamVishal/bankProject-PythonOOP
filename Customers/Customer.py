from Accounts.Checking import Checking
from Accounts.Savings import Savings
from Accounts.Business import Business

class Customer:

	def __init__(self, name, PIN):
		self.name = name
		self.PIN = PIN
		self.accts = {'C':[],'S':[],'B':[]}

	def __str__(self):
		return self.name

	def open_checking(self, acct_nbr, opening_deposit):
		self.accts['C'].append(Checking(acct_nbr, opening_deposit))
	def open_savings(self, acct_nbr, opening_deposit):
		self.accts['S'].append(Savings(acct_nbr, opening_deposit))
	def open_business(self, acct_nbr, opening_deposit):
		self.accts['B'].append(Business(acct_nbr, opening_deposit))
	def get_total_deposits(self):
		total = 0
		for acct in self.accts['C']:
			print(acct)
			total += acct.balance
		for acct in self.accts['S']:
			print(acct)
			total += acct.balance
		for acct in self.accts['B']:
			print(acct)
			total += acct.balance
		print(f'Combined Deposits: ${total:2f}')
		
		
	def make_dep(cust,acct_type,acct_num,dep_amt):
		for acct in cust.accts[acct_type]:
			if acct.acct_nbr == acct_num:
				acct.deposit(dep_amt)
	
	def make_wd(cust,acct_type,acct_num,wd_amt):
		for acct in cust.accts[acct_type]:
			if acct.acct_nbr == acct_num:
				acct.withdraw(wd_amt)