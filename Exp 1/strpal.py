string = input("Enter a String: ")
rev = ''.join(reversed(string))
if(string == rev):
	print("It is a Palindrome")
else:
	print("It is not Palindrome")

