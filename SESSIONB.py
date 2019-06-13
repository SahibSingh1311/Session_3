"""
Relationship Mapping

    HAS-A MAPPING

        1 Engineer working on 1 Project
        1 Engineer working on many Project
        many Engineers working on many Projects

        1 Customer has 1 Address
        1 Customer has many Addresses
        many Customers have many Addresses

        1 Company has 1 Product
        1 company has many product
        many company has many product

        Company
            Name
            Location
            Worker
        Product
            modelNumber




        Customer
            Name
            phone
            email
        Address
            adrsLine
            city
            state

"""

class Customer:

    #constructor for Standardization
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address #HAS-A RELATIONSHIP
    def updateCustomerDetails(self, name, phone, emal):
        self.name = name
        self.phone = phone
        self.email = email
    def showCustomerDetails(self):
        print("~~~~~~~~~~~~~")
        print("Name: \t", self.name)
        print("Phone: \t", self.phone)
        print("email: \t", self.email)
class address:

    def __init__(self, adrsLine, city, state):
        self.AdrsLine = adrsLine
        self.City = city
        self.State = state
    def updateAddress (self, adrsLine, city, state):
        self.adrsLine = adrsLine
        self.city = city
        self.state = state
    def showAddressDetails(self):
        print("~~~~~~~~~~~~~~")
        print("Address Line: \t",self.AdrsLine)
        print("City: \t", self.City)
        print("State: \t", self.State)
        self.address.showAddressDetails()

a1 = address("Redwood Shores", "Bangalore", "Karnataka")
#a2 = address("KUMAR Residance","ludhiana", "Punjab")
#adrsList = [a1,a2]
c1 = Customer("john","9876542310","john@example.com", a1)

c1.showCustomerDetails()

"""
    1 Order can have many foodItems
    with user input Create a small program ;)
"""