class Student:
	
	def setName(self,name):
		self.name=name
	
	def getName(self):
		return self.name
	
	def setMarks(self,marks):
		self.marks=marks
	
	def getMarks(self):
		return self.marks
l=[]
n=int(input("Enter the number of students :"))
for i in range(n):
	s=Student()
	name=(input("Enter the student name :"))
	marks=float(input("Enter the Marks :"))
	s.setName(name)
	s.setMarks(marks)
	l.append(s)
for a in l:
	print("Name :",a.getName())
	print("Marks :",a.getMarks())
	print()