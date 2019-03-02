#Fibonacci Series

def fibo(i, j, n):
	if(n!=0):
		print(i)
		fibo(i + j, i, n-1)
	return

fibo(0, 1, int(input("Enter n: ")))
