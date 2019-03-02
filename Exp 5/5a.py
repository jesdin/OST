class accholder():
	count = 0
	def __init__(self):
		self.accnum = 0
		self.name = ""
		self.age = 0
		self.balance = 0.0
		accholder.count += 1
	def setdata(self, accnum, name, age, balance):
		self.accnum = accnum
		self.name = name
		self.age = age
		self.balance = balance
	def getdata(self):
		print("Name = %s\tBalance = %10.2f"%(self.name, self.balance))
	def update(self, newbal):
		self.balance = newbal
	def getNoOfAccounts():
		getNoOfAccounts = staticmethod(getNoOfAccounts)
		return accholder.count		

n = int(input("Enter number of employees: "))
emp = []
print("Enter details in the format 'accnum Name age balance'")
for i in range(n):
	t = input("Emp 1: ").split()
	e = accholder()
	e.setdata(int(t[0]), t[1], int(t[2]), float(t[3]))
	emp.append(e)
print("")
an = int(input("Enter accnum to change balance: "))
for i in range(n):
	if (emp[i].accnum == an):
		emp[i].update(float(input("New Balance: ")))
	else:
		print("accnum does not exist")
for e in emp:
	e.getdata()
print("No of account holders = %d"%(accholder.count))

class der1(accholder):
	def __init__(self):
		super(der1, self).__init__()
	def update(self, name):
		self.name = name
		
class der2(accholder):
	def __init__(self):
		super(der1, self).__init__()
	def update(self, name, bal):
		self.name = name
		self.balance = bal
		
d1 = der1()
print("Derived class 1:")
d1.getdata()
d1.update(input("Enter name to update: "))
d1.getdata()
d2 = der2()
print("Derived class 2:")
d2.getdata()
d2.update(input("Enter name to update: "), float(input("Enter balacne to update: ")))
d2.getdata()

print("No of account holders = %d"%(accholder.count))
