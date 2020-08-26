class Book:
	def __init__(self, pages):
		self.pages=pages
	
	def __add__(self,other):
		total = self.pages+other.pages
		return Book(total)
	def __str__(self):
		return str(self.pages)

b4=Book(10)
b1=Book(20)
b2=Book(30)
b3=Book(40)
bx= b1+b2+b3+b4
print("b1+b2 :",(b1+b2).pages)
print("b1+b2+b3 :",(b1+b2+b3).pages)
print("b1+b2+b3+b4 :",(b1+b2+b3+b4).pages)
print("b1+b2+b3+b4 :",bx)