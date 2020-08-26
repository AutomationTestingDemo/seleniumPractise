import csv
with open('empCSV.csv','w',newline='') as f:
	w=csv.writer(f)
	w.writerow(['ENO','ENAME','ESAL','EADDR'])
	n=int(input('enter the number of employees :'))
	for i in range(n):
		eno=int(input('enter the employe number :'))
		ename=input('enter the employe name :')
		esal=float(input('enter the employe sal :'))
		eaddr=input('enter the employe addr :')
		w.writerow([eno,ename,esal,eaddr])
print('All the employee data succesfully written to file')