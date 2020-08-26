class Section:
	def __init__(self,name,num,chick):
		self.name=name
		self.num=num
		self.chick=chick
	def display(self):
		print(self.name,'\t',self.num,'\t',self.chick)
list=[]
s=Section('kalyan','100','laura angel')
list.append(s)
s=Section('chakri','101','lana rhoades')
list.append(s)
s=Section('chintu','102','olivia del rio')
list.append(s)
print(list)
print(len(list))