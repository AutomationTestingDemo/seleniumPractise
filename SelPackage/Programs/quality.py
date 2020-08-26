n = int(input('Enter the number of people :'))
d={}
for x in range(n):
	Name=str(input('Enter the name :'))
	quality=str(input('Enter the quality :'))
	d[Name]=quality
print(d)
while True:
	name=str(input('Enter the name to know the quality :'))
	quality=d.get(name,-1)
	if quality==-1:
		print(name,' Person not available')
	else:
		print('Quality of the person ',name,' is ',quality)
	s=str(input('Do u want to continue to know the quality of the person [Y|N]:'))
	if s=='N':
		break
print('Thankyou for using our Application')

