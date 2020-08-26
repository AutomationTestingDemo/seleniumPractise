f= open('multiplelines.txt','w')
l=['sunny\n', 'bunny\n','cunny\n']
f.writelines(l)
f.close()
print('is file closed?', f.closed)