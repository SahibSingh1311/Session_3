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
"""

import mysql.connector

class DBHelper:


    def saveCustomerInDB(self, customer):
        #1. Create SQL Statement
        sql = "insert into customer values (Null, '{}', '{}','{}') ".format(customer.name,customer.phone, customer.email)

        #2 Create Connection
        con = mysql.connector.connect(user = "root", password = "", host ="localhost", database = "customer")

        #3 Obtain cursor or execute SQL statements {ACID}
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()

        print(customer.name, "SAVED!!")

class customer:

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
    def showCustomerDetails(self):
        print(">>Name: {} Phone: {} Email: {}".format(self.name, self.phone, self.email ))


print("Options: ")
print("1. Create New Customer")

choice = int(input("Enter Choice: "))

if choice ==1:
    cRef = customer(None, None, None)
    cRef.name = input("Enter Customer Name      : ")
    cRef.phone = input("Enter Customer Phone    : ")
    cRef.email = input("Enter Customer Email    : ")

    cRef.showCustomerDetails()

    save = input("Do you want to Save Customer:(yes / no) ")
    if save == "yes":
        db = DBHelper()
        db.saveCustomerInDB(cRef)