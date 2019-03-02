string = input("Enter a String: ")
string = string.lower()
count = 0
for s in string:
	if(s == 'a' or s == 'e' or s == 'i' or s == 'o' or s == 'u'):
		count = count+1
print("No of vowels ", end='')
print(count)
