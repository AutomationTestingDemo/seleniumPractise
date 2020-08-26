l=['a','e','i','o','u']
s='motherfucker'
p=''
for x in s:
	if x in l:
		if x not in p:
			p+=x
		else:
			print('repeated vowel',x)
	else:
		print(x,'is not a vowel')
print('unique vowels in "s"',p)
