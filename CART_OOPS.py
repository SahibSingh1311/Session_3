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

    def showOrderDetails(self):
        print("****************************")
        print(">>Resturant is: \t", self.restaurantName)

        for x in self.itemList:
            itm.showItemDetails()
class Item:

    def __init__(self, itemName, itemPrice):
        self.itemName = itemName
        self.itemPrice = itemPrice


    def showItemDetails(self):
        print("****************************")
        print(">>Item Name is: \t", self.itemName)
        print(">>Item Price is: \t", self.itemPrice)

Restaurant = Order(None)
Restaurant.restaurantName = input("Enter the Restaurant Name: \t")


itemList = []
choise = "yes"
while choise == "yes":
    itm = Item(None, None)
    itm.itemName = input("Enter the Item Name: \t")
    itm.itemPrice = int(input("Enter the Price: \t"))
    itemList.append(itm)

    choise = input("Would you like to add another item (yes/no): ")
Restaurant.showOrderDetails()
for x in range(len(itemList)):
    itemList[x].showItemDetails()