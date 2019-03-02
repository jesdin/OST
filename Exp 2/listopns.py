#1. Operations of List
mylist = [1, 9, 5, 2, 7]
print(mylist)
ch = 1
while(ch != 11):
	print("1. Slicing")
	print("2. length")
	print("3. +, *")
	print("4. append")
	print("5. insert")
	print("6. count")
	print("7. sort")
	print("8. remove")
	print("9. pop")
	print("10.delete list")
	print("11.Exit")
	ch = int(input("Enter Choice: "))
	if(ch == 1):
		print(" mylist[1]: ", end="")
		print(mylist[1])
		print(" mylist[1:3]: ", end="")
		print(mylist[1:3])
		print(" mylist[::-1]: ", end="")
		print(mylist[::-1])
	elif(ch==2):
		print("length of list = " + str(len(mylist)))
	elif(ch == 3):
		print("mylist + [0]: ", end="")
		print(mylist + [0])
		print("mylist * 2: ", end="")
		print(mylist*2)
	elif(ch == 4):
		print("mylist.append(10): ", end="")
		mylist.append(10)
		print(mylist)
	elif(ch == 5):
		print("mylist.insert(3, 1): ", end="")	#list.insert(index, element)
		mylist.insert(3, 1)
		print(mylist)
	elif(ch == 6):
		print("count of 1: " + str(mylist.count(1)))
	elif(ch == 7):
		print("Sorted list: ", end="")
		mylist.sort()
		print(mylist)
	elif(ch == 8):
		print("remove 1st occurence of 5: ", end="")
		mylist.remove(5)
		print(mylist)
	elif(ch == 9):
		print("Pop index 2: ", end="")
		mylist.pop(2)
		print(mylist)
	elif(ch==10):
		print("deleting mylist: ", end="")
		del(mylist)
		print("List deleted Successfully")
	print()
