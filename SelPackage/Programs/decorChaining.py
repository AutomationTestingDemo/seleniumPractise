def decor1(func):
	def inner(name):
		print("This is decor1")
		func(name)
	return inner

def decor2(func):
	def inner(name):
		print("This is decor2")
		func(name)
	return inner
@decor2
@decor1
def wish(name):
	print("Hello ",name)

wish("Kalyan")