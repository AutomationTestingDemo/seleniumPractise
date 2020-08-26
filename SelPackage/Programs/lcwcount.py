import os,sys
fname=input('Enter the filename :')
if os.path.isfile(fname):
	print('File exists')
	f=open(fname,'r')
else:
	print('File not available')
lcount=wcount=ccount=0
for x in f:
	lcount=lcount+1
	ccount=ccount+len(x)
	words=x.split()
	wcount=wcount+len(words)
print('line count is :',lcount)
print('character count is :',ccount)
print('words count is :',wcount)