n=[10,50,600,80,90]
for i in n:
     if i==600:
         print('cant process',i)
         continue
     print(i,'Processed Successfull')
else:
     print('Successfull')