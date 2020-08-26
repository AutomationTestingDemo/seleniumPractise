class Engine:
	
	a=10
	
	def __init__(self):
		self.b=20
	
	def m1(self):
		print("Engine specific functionality")

class car:
	
	def __init__(self):
		self.engine=Engine()
	
	def m2(self):
		print(self.engine.a)
		print(self.engine.b)
		self.engine.m1()

c=car()
c.m2()