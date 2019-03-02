# Demonstrate tupple and dictionary

#tuple
print("*Tuple Operations*")
print("------------------------------------------------")
print("")
print("*Create a Tuple*")
myTuple = tuple(input("Enter elements seperated by a space:\n").split(" "))
print(myTuple)
print("")
print("*Add*")
temp = list(myTuple)
ele = input("Enter an element: ")
temp.append(ele)
myTuple = tuple(temp)
print(myTuple)
print("")
print("*Sort*")
temp = list(myTuple)
temp.sort()
myTuple = tuple(temp)
print(myTuple)
print("")
print("*Find an element*")
val = input("Enter the element: ")
if val in myTuple:
    print("Element found.")
else:
    print("Element not found.")
print("")
print("*Delete*")
temp = list(myTuple)
val = input("Enter the element: ")
if val in myTuple:
    temp.remove(val)
    print("Element deleted.")
    myTuple = tuple(temp)
    print(myTuple)
else:
    print("Element not found.")
    myTuple = tuple(temp)

print("")
print("*Dictionary Operations*")
print("------------------------------------------------")

print("")
print("*Create a Dict*")
myDict = {}
keys = (input("Enter the keys seperated by a space:\n")).split(" ")
values = (input("Enter the values seperated by a space:\n")).split(" ")
# for i in range(len(keys)):
#     myDict[keys[i]] = int(values[i])
myDict = dict(zip(keys, values))
print(myDict)    

print("")
print("*Add*")
nkey = input("Enter the new key: ")
nvalue = int(input("Enter the new value: "))
myDict[nkey] = nvalue
print("Updated Dictionary:\n", myDict)

print("")
print("*Sort*")
print("Sorted Dictionary:\n", dict(sorted(myDict.items())))

print("")
print("*Find*")
temp = input("Enter the key you want to find: ")
if temp in myDict:
    print("Key found with value: ", myDict[temp])
else:
    print("Key not found")

print("")
print("*Delete*")
temp = input("Enter the key you want to delete: ")
if temp in myDict:
    myDict.pop(temp)
    print("Updated Dictionary:\n", myDict)
else:
    print("Key not found.")
