import emp,pickle
f=open("emp.txt","wb")
n= int(input("enter the number of emps :"))
for x in range(n):
	eno=int(input('enter the employe number :'))
	ename=input('enter the employe name :')
	esal=float(input('enter the employe sal :'))
	eaddr=input('enter the employe addr :')
	obj=emp.employee(eno,ename,esal,eaddr)
	pickle.dump(obj,f)
print("Emp Object Dumped Succesfully")