from .Account import Account 

class Checking(Account):
	def __init__(self, acct_nbr, opening_deposit):
		#Run the base class __init__
		super().__init__(acct_nbr, opening_deposit)

	#Define a __str__ method that returns a string specific to checking accounts
	def __str__(self):
		return f'Checking Account #{self.acct_nbr}\n Balance: {Account.__str__(self)}' 