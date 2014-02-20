num = int(input('n'))


def doit(n):    
	print(n)
	if(n<num*3):
		doit(n+3)	


doit(3)
