"""
    Database: mySQL
    prog Lang: SQL -> Structured Query Language
    1. Create Database
        Database is collection of Tables
        Tables can be related to each other : 1 to 1 relation or 1 to many relationship

    2. Create Table
        Table is collection of rows and columns eg: Excel Sheet

        ORM: Object relation mapping
        Your object's attribute should be your table column name
        but in tables we have 1 additional column and we call it as Primary Key

        1 2 3 4.......

        code: CREATE TABLE customer(
                            cid int PRIMARY KEY AUTO_INCREMENT,
                            name varchar (256),
                            phone varchar (20),
                            email varchar (256)
                         )
    3. Insert Data in Table
        cref = customer("John","9999988888","john@example.com")
        insert into customer(Null, "John","9999988888","john@example.com")
    4. Install Library mysql-connector
    5. Create a DBHelper
    6. Update data in table
"""

import mysql.connector

class DBHelper:

    def saveCustomerInDB(self, customer):
        #1. Create SQL Statement
        sqlInsert = "insert into customer values (Null, '{}', '{}','{}') ".format(customer.name,customer.phone, customer.email)

        #2 Create Connection
        con = mysql.connector.connect(user = "root", password = "", host ="localhost", database = "customer")

        #3 Obtain cursor or execute SQL statements {ACID}
        cursor = con.cursor()
        cursor.execute(sqlInsert)
        con.commit()

        print(customer.name, "SAVED!!")

    def updateCustomerInDB(self, customer):
        sql = "update customer set name = '{}', phone = '{}', email = '{}' where cid = '{}'".format(customer.name, customer.phone, customer.email, customer.cid )
        con = mysql.connector.connect(user = "root", password ="", host = "localhost", database = "customer")
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        print("Customer Updated")

    def deleteCustomerDetails(self,customer):
        sql = "delete from customer where cid = {}".format(customer.cid)
        con = mysql.connector.connect(user="root", password="", host="localhost", database="customer")
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()

    def fetchAllCustomer(self):
        sql = "select * from customer"
        con = mysql.connector.connect(user="root", password="", host="localhost", database="customer")
        cursor = con.cursor()
        cursor.execute(sql)
        # row = cursor.fetchone()
        # print(row)
        # row = cursor.fetchone()
        # print(row)
        rows = cursor.fetchall()
        #print(rows) #Rows is a List of Tuples, 1 Tuple Represent 1 Row
        for row in rows:
            print(row)

    def fetchCustomer(self, cid):
        sql = "select * from customer where cid = {}".format(cid)
        con = mysql.connector.connect(user="root", password="", host="localhost", database="customer")
        cursor = con.cursor()
        cursor.execute(sql)
        row = cursor.fetchone()
        print(row)


class customer:

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
    def showCustomerDetails(self):
        print(">>Name: {} Phone: {} Email: {}".format(self.name, self.phone, self.email ))

"""
print("Options: ")
print("1. Create New Customer")
print("2. Update Customer")
print("3. Delete Customer")
print("4. Show All Customers")
print("5. Show Particular Customers")

choice = int(input("Enter Choice: "))

if choice == 1:
    cRef = customer(None, None, None)
    cRef.name = input("Enter Customer Name      : ")
    cRef.phone = input("Enter Customer Phone    : ")
    cRef.email = input("Enter Customer Email    : ")

    cRef.showCustomerDetails()

    save = input("Do you want to Save Customer:(yes / no) ")
    if save == "yes":
        db = DBHelper()
        db.saveCustomerInDB(cRef)

elif choice == 2:
    cRef = customer(None, None, None)
    cRef.cid = int(input("Enter Customer ID     : ")) #You NEED TO KNOW THE CUSTOMER ID
    cRef.name = input("Enter Customer Name      : ")
    cRef.phone = input("Enter Customer Phone    : ")
    cRef.email = input("Enter Customer Email    : ")

    cRef.showCustomerDetails()

    save = input("Do you want to Save Customer:(yes / no) ")
    if save == "yes":
        db = DBHelper()
        db.updateCustomerInDB(cRef)
elif choice == 3:
    cRef = customer(None, None, None)
    cRef.cid = int(input("Enter Customer ID     : "))  # You NEED TO KNOW THE CUSTOMER ID
    save = input("Do you want to delete Customer:(yes / no) ")
    if save == "yes":
        db = DBHelper()
        db.deleteCustomerDetails(cRef)
        print("Customer Deleted")
elif choice == 4:
    db = DBHelper()
    db.fetchAllCustomer()
elif choice == 5:
    cRef = customer(None, None, None)
    cRef.cid = int(input("Enter Customer ID: "))

    db = DBHelper()
    db.fetchCustomer(cRef.cid)

"""