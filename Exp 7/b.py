import sqlite3
import sys

conn = None
try:
    conn = sqlite3.connect('data.db')
    print ("Opened database successfully")
except:
    print("Connection Unsucessfull")
    sys.exit()


def insert(id, name, age, number, department):
    conn.execute("INSERT INTO STUDENT (ID,NAME,AGE,NUMBER,DEPARTMENT) \
      VALUES ({}, '{}', {}, {}, '{}')".format(id, name, age, number, department))
    conn.commit()
    print ("Data Entered Successfully")


def view_data():
    info = conn.execute("SELECT ID, NAME, AGE, NUMBER, DEPARTMENT from STUDENT")
    print("ID\tName\tAge\tNumber\tDepartment")
    for row in info:
        print("{}\t{}\t{}\t{}\t{}".format(row[0], row[1], row[2], row[3], row[4]))


def delete(id):
    conn.execute("DELETE from STUDENT where ID = {};".format(id))
    conn.commit()


def update(id_old, id_new, name, age, number, department):
    conn.execute('''UPDATE STUDENT SET ID = {}, NAME = '{}', AGE = {}, NUMBER = {}, DEPARTMENT = '{}' WHERE ID == {}'''.format(id_new, name, age, number, department, id_old))


while True:
    print("1. Insert\n2. View\n3. Update\n4. Delete\n5. Exit")
    ch = int(input("Enter Choice: "))
    if ch == 1:
        id = int(input("Enter ID: "))
        name = input("Enter Name: ")
        age = int(input("Enter age: "))
        number = int(input("Enter number: "))
        dept = input("Enter Department: ")
        insert(id, name, age, number, dept)
    if ch == 2:
        view_data()
    if ch == 3:
        id = int(input("Enter ID: "))
        id_n = int(input("Enter new ID: "))
        name = input("Enter new Name: ")
        age = int(input("Enter new age: "))
        number = int(input("Enter new number: "))
        dept = input("Enter new Department: ")
        update(id, id_n, name, age, number, dept)
    if ch == 4:
        id = int(input("Enter ID: "))
        delete(id)
    if ch == 5:
        break