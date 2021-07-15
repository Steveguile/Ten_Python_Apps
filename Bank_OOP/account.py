
class Account:

	def __init__(self, file_path):
		self.file_path = file_path
		with open(self.file_path, "r") as file:
			self.balance = int(file.read())

	def withdraw(self, amount):
		self.balance = self.balance - amount
		
	def deposit(self, amount):
		self.balance = self.balance + amount 

	def commit(self):
		with open(self.file_path, "w") as file:
			file.write(str(self.balance))

# Account parameter allows inheritence of Account
class Checking(Account):
	"""
	Some class documentation
	Can be called with object_instance.__doc__
	"""

	# A data member are both class and instance variables
	type="checking" # Class variable will persist accross all instance

	def __init__(self, file_path, fee):
		Account.__init__(self, file_path)
		# Instance variable
		self.fee = fee

	def transfer(self, amount):
		self.balance = self.balance - amount - self.fee
