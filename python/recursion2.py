def sumofint(n):
	if(n==0):
		return n
	else:
		return n + sumofint(n-1)

print(sumofint(int(input('n:'))))
