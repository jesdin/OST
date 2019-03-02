print("")
print("*Set Operations*")
print("---------------------------------")
print("")

setA = {1, 3, 5, 7}
setB = {2, 4, 6, 7}
print("setA: {}".format(setA))
print("setB: {}".format(setB))

print("")
print("*union*")
print(setA | setB)

print("")
print("*Intersection*")
print(setA & setB)

print("")
print("*Difference*")
print("A-B: +", end="")
print(setA - setB)

print("")
print("*Symmetric Difference*")
print(setA ^ setB)

print("")
print("*A subset of B*")
print(setA.issubset(setB))

print("")
print("*A superset of B*")
print(setA.issuperset(setB))
print("")
print("*Update*")
setA.update(setB)
print(setA)

print("")
print("*length*")
print(len(setA))

