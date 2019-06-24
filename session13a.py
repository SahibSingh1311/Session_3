# tkinter to create GUI
from tkinter import *

#import session12a
#from session12a import customer
#from session12a import DBHelper

from session12a import *

def onClick():
    print("Button Clicked")
    cRef = customer(None, None, None)
    cRef.name = entryName.get()
    cRef.phone = entryPhone.get()
    cRef.email = entryEmail.get()
    cRef.showCustomerDetails()

    db = DBHelper()
    db.saveCustomerInDB(cRef)

window = Tk() #Crate a Frame where there is minimse close and maximize button is there
lblTitle = Label(window, text="Add Customer Details") #Yeh Bani bnayi clases hai so be carefull with the case
lblTitle.pack()


lblName = Label(window, text="Enter Customer Name")
lblName.pack()

entryName = Entry(window)
entryName.pack()

lblPhone = Label(window, text="Enter Customer Phone")
lblPhone.pack()

entryPhone = Entry(window)
entryPhone.pack()

lblEmail = Label(window, text="Enter Customer Email")
lblEmail.pack()

entryEmail = Entry(window)
entryEmail.pack()

btnAddCustomer = Button(window, text = "Add Customer", command = onClick)
btnAddCustomer.pack()
window.mainloop() #Keep on running the program/ process until we press the close button

"""
    Phase-I
    CRUD Operations with GUI
    
    Phase-II
    Loyalty Points: 100 --> 1Point => Re 1
    > Shopping amount should be entered
    > 2 : 3500 | 10 percent | 350 + 100 = 450
    > Check Loyalty Points
    > Redeem Loyalty Points
        Will apply if shopping amount greater then 500
        in 1 billing maximum redeemed point is 150
    
    Phase-III
"""