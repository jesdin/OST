mylist = []
strin = input(" Enter List of words:\n ")
for i in strin.split(" "):
    mylist.append(i)
n = int(input(" Enter n: "))
print(" Words having length greater than {}:".format(n))
for i in mylist:
    if(len(i)>n):
        print(" {}".format(i), end = " ")