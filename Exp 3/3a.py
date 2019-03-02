#a
n = int(input("Enter num of studetns: "))
print("Enter Roll No Name and marks of 3 subj")
mylist = []
for i in range(n):
    string = input("Student {}: ".format(i+1))
    details = string.split(" ")
    student = ("{}".format(int(details[0])), "{}".format(details[1]), "{}".format(int(details[2])), "{}".format(int(details[3])), "{}".format(int(details[4])))
    mylist.append(student)
print(mylist)

#b
print("")
for i in mylist:
    if(i[1] == "Python"):
        print("{}\t{}".format(i[0], i[1]))

#c
print("")
studentlist = tuple(mylist)
print(studentlist)
studentlist = sorted(studentlist, key = lambda x: x[1])
print(studentlist)

#d
print("")
mylist = list(studentlist)
for i in range(n):
        t = input("makr of sub3 of {}: ".format(mylist[i][1]))
        mylist[i] = (mylist[i][0], mylist[i][1], mylist[i][2], mylist[i][3], t)
        # mylist[i] = ("{}".format(i[0]), "{}".format(i[1]), "{}".format(i[2]), "{}".format(i[3]), "{}".format(t))
del studentlist
studentdetails = tuple(mylist)
print(studentdetails)
