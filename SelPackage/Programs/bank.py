import sys
class Bank:
	'''Bank Class with Bank Operations'''
	bName="ANZ Bank"

	def __init__(self,name,balance=0.0):
		self.name=name
		self.balance=balance
		
	def deposit(self,amount):
		self.balance=self.balance+amount
		print("Total Balance after Deposit is :", self.balance)

	def withdraw(self,wamount):
		if(wamount<=self.balance):
			self.balance=self.balance-wamount
			print("Total Balance after withdrawl is :", self.balance)

		else:
			print("Insufficient funds")
			sys.exit()

print("Welcome to ",Bank.bName)
cname=input("Enter your name :")
b=Bank(cname)
while True:
	print('d-Deposit \nw-Withdrawl \ne-Exit')
	option=input("Choose ur option:").lower()
	if option=='d':
		amount=float(input('Enter the amount to deposit :'))
		b.deposit(amount)
	
	elif option=='w':
		while True:
			wamount=float(input('Enter the amount to withdraw :'))
			if(wamount<100):
				print("Minimum withdrawl amount should be greater than 100 and Multiple of 100")
			else:
				break

		b.withdraw(wamount)

	elif option=='e':
		print("Thanks for banking with us")
		sys.exit()

	else:
		print("Invalid option...enter the valid option")

print("Please comeback soon :)")



		
