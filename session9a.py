class Product:
    resturantName = "ABC"
    #constructor
    def __init__(self, name, price):
        self.name = name
        self.price = price

    #Function
    def showProduct(self):
        print(self.name, self.price, Product.resturantName)

    #distructor
    def __del__(self):
        print("product deleted")
p1 = Product("Paneer", 200)
p2 = Product("DAL", 100)
print(hex(id(p1)))
print(hex(id(p2)))
print("THANKYOU")
#DELETION WILL HAPPEN AUTOMATICALLY AND WHEN MEMORY IS DELETED DISTRUCTOR IS CALLED AUTOMATICALLY
#DISTRUCTOR AND CONSTRUCTOR ARE DEPENDED UPON ONE'S REQUIREMENT
#CONSTRUCTOR IS FOR STANDARDIZATION
#DISTRUCTOR IS TO DO SOMETHING WITH THE DATA BEFORE DELETION