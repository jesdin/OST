num = int(input("Enter a Number: "))
temp = num
rev = 0
while(temp != 0):
	rev = 10*rev + temp%10
	temp = temp//10
if(rev == num):
	print(str(num) + " is palindrome")
else:
	print(str(num) + " is not palindrome")
