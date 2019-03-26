import sqlite3
import sys

conn = None
try:
    conn = sqlite3.connect('data.db')
    print ("Opened database successfully")
except:
    print("Connection Unsucessfull")
    sys.exit()

# create table STUDENT
conn.execute('''CREATE TABLE STUDENT
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL,
         NUMBER         INT,
         DEPARTMENT     CHAR(15));''')
print("Created Table Student Successfully")