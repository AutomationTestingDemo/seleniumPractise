class Employee:
	def __init__(self,name,salary):
		self.name=name
		self.salary=salary
	def __mul__(self,other):
		return self.salary*other.days
class TimeSheet:
	def __init__(self,name,days):
		self.name=name
		self.days=days
e=Employee('Durga',500)
t=TimeSheet('kalyan',20)
print('This Month Salary:',e*t)