import copy

str1 = input("String 1: ")
str2 = input("String 2: ")

set1 = set(list(str1))
set1.discard(' ')
set2 = set(list(str2))
set2.discard(' ')
print("Set1: {}".format(set1))
print("Set2: {}".format(set2))
print("Common letters: {}".format(set1 & set2))
print("letters in str1 not in str2: {}".format(set1 - set2))
print("set of letters in both strings: {}".format(set1 | set2))
print("letters in str1 and str2 but not common in both: {}".format(set1 ^ set2))

copyshallow = copy.copy(set1)
copyasn = set1
print("Set1: {}".format(set1))
print("SetCopyShallow: {}".format(copyshallow))
print("SetAssgn: {}".format(copyasn))
print("adding Python to set1")
set1.add("Python")
print("Set1: {}".format(set1))
print("SetCopyShallow: {}".format(copyshallow))
print("SetAssgn: {}".format(copyasn))
print("")
print("ID of Set1: {}".format(id(set1)))
print("ID of SetCopyShallow: {}".format(id(copyshallow)))
print("ID of SetAssgn: {}".format(id(copyasn)))

