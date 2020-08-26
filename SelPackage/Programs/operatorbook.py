class Book:
	def __init__(self, pages):
		self.pages=pages
	
	def __add__(self,other):
		total = self.pages+other.pages
		return Book(total)

b4=Book(10)
b1=Book(10)
b2=Book(10)
b3=Book(10)
print("b1+b2 :",b1+b2)
print("b1+b2+b3 :",b1+b2+b3)
print("b1+b2+b3+b4 :",b1+b2+b3+b4)