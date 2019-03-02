mylist = []
num = input("Enter Numbers: ")
for i in num.split(" "):
	mylist.append(int(i))
list1 = []
list2 = []

ch = 0
while(ch!=6):
	print("\n1. Put even and odd elements int 2 lists")
	print("2. Merge and sort 2 lists")
	print("3. Update 1st element with x value and delete middle element")
	print("4. find minimum and maximum of list")
	print("5. add 'N' names into existing list using extend function and check if word 'python' is present in the list")
	print("6. Exit")
	ch = int(input("Enter choice: "))
	if(ch == 1):
		for i in mylist:
			if(i%2 != 1):
				list1.append(i)
			else:
				list2.append(i)
		del(mylist)		
		print("Even list: ", end="")
		print(list1)
		print("Odd list: ", end="")
		print(list2)
	if(ch == 2):
		list1.extend(list2)
		list1.sort()
		print("After merging and sorting: ", end="")
		print(list1)
		del(list2) 
	if(ch == 3):
		list1[0] == 7
		list1.pop(len(list1)//2)
		print(list1)
	if(ch == 4):
		print("greatest: ", end="")
		print(max(list1))
		print("least: ", end="")
		print(min(list1)) 			
	if(ch == 5):
		mylist = []
		string = input("Enter n strings: ")
		for i in string.split(" "):
			mylist.append(i)
		list1.extend(mylist)
		print(list1)
		ch = 2
		for i in list1:
			if(i == "python"):
				print("word 'python' is present")
				ch = 1
				break
		if(ch == 2):
			print("word 'python' is not present") 
