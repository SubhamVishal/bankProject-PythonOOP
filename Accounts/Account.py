class Account:
	#Define an inti constructor method with attributes shared by all the accounts
	def __init__(self, acct_nbr, opening_deposit):
		self.acct_nbr = acct_nbr
		self.balance = opening_deposit

	#Define a __str__ method to return a recognizable string to any print() command
	def __str__(self):
		return f'${self.balance:.2f}'

	#Define a universal method to accept deposits
	def deposit(self, dep_amt):
		self.balance += dep_amt

	def withdraw(self, wd_amt):
		if self.balance >= wd_amt:
			self.balance -= wd_amt
		else:
			print('Funds Unavailable')