from .Account import Account

class Business(Account):
	def __init__(self, acct_nbr, opening_deposit):
		super().__init__(acct_nbr, opening_deposit)


	 # Define a __str__ method that returns a string specific to Business accounts
	def __str__(self):
		return f'Business Account #{self.acct_nbr}\n  Balance: {Account.__str__(self)}'