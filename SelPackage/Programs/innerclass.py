class person:
	def __init__(self,name,dd,mm,yyyy):
		self.name=name
		self.dob=self.dob(dd,mm,yyyy)

	def display(self):
		print("Name is :",self.name)
		self.dob.displayage()


	class dob:
		def __init__(self,dd,mm,yyyy):
			self.dd=dd
			self.mm=mm
			self.yyyy=yyyy
		
		def displayage(self):
			print("Age is {}/{}/{}".format(self.dd,self.mm,self.yyyy))
p=person('Kalyan','04','06','1994')
p.display()