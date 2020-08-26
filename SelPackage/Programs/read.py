f = open('write.txt','r')
list=f.readlines()
for l in list:
	print(l)
f.close()