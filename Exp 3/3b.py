mydict = {}
n = int(input("Enter the no of key value pairs: "))
for i in range (n):
	string= input("{}: ".format(i+1))
	string= string.split(" ")
	mydict[string[0]] = string[1]

#b
print(mydict)
key = input("Enter key to update: ")

c = False
for k in mydict:
	if(k == key):
		c = True
		mydict[key] = input("Enter new value: ")

if(c == False):
	print("Key not in dict")

print("Updated dict: {}".format(mydict))

mydict2 = {}
n = int(input("Enter the no of key value pairs: "))
for i in range (n):
	string= input("{}: ".format(i+1))
	string= string.split(" ")
	mydict2[string[0]] = string[1]
mydict.update(mydict2)
print(mydict)

key = input("Enter key to delete: ")
c = False
for k in mydict:
	if(k == key):
		c = True
		del mydict[key]
		break
if(c == False):
	print("Key not in dict")
else:
	print("Key deleted successfully")
print(mydict)

#c
key = input("Enter key to find: ")

c = False
for k in mydict:
	if(k == key):
		c = True
		print("{}: {}".format(key,mydict[key]))
if(c==False):
	print("Key not found")

#d
newdict ={}
key= input("Enter list of keys: ").split(" ")
value= input("Enter list of values: ").split(" ")
newdict = dict(zip(key, value))
print(newdict)

#e
print(sorted(newdict))
for i in sorted(newdict):
	print("{}: {}".format(i, newdict[i]))