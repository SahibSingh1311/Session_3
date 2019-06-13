"""
    1 Order has 1 foodItem
    1 Order has many foodItems

    Order
        restaurantName
        orderNumber

    Item
        itemName
        itemPrice
        promoCode
        discount

    Address
        phone
        adrsLine
        city
        state
"""
class Order:

    def __init__(self, restaurantName):
        self.restaurantName = restaurantName
        self.orderNumber = 1
    def showOrderDetails(self):
        print("****************************")
        print(">>Resturant is: \t", self.restaurantName )
        print(">>Order Number is: \t", self.orderNumber)

class Item:

    def __init__(self, itemName, itemPrice):
        self.itemName = itemName
        self.itemPrice = itemPrice

    def showItemDetails(self):
        print("****************************")
        print(">>Item Name is: \t", self.itemName)
        print(">>Item Price is: \t", self.itemPrice)


itemList = []
choise = "yes"
while choise == "yes":
    itm = Item(None, None)
    itm.itemName = input("Enter the Item Name: \t")
    itm.itemPrice = input("Enter the Price: \t")
    itemList.append(itm)
    choise = input("Would you like to add another item (yes/no): ")

for itm in self.Item :
