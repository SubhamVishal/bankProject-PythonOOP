import sys
sys.path.append('.')

from Accounts.Checking import Checking
from Customers.Customer import Customer

x = Checking(54321, 654.3334)

print(x)

x.withdraw(1000)

x.withdraw(30)

print(x.balance)


bob = Customer('Bob', 1)

bob.open_checking(321, 555.55)

print(bob.get_total_deposits())

bob.open_savings(564,444.66)

print(bob.get_total_deposits())


nancy = Customer('Nancy',2)


nancy.open_business(2018,8900)

nancy.get_total_deposits()

nancy.make_dep('B',2018,67.45)

nancy.get_total_deposits()

nancy.make_wd('B',2018,1000000)

nancy.get_total_deposits()