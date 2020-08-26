s=str(input('Enter the string: '))
p=''
for i in s:
	if i in p:
		continue
	else:
		p+=i
print('Final String :',p)