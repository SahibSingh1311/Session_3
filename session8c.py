class Product:
    counter = 0
    def __init__(self):
        Product.counter = Product.counter +1
    def showObjects(self):
        print("Number of Objects:{} ".format(Product.counter))

p1 = Product()
p2 = Product()
p3 = Product()
p4 = p1
p5 = p3
p5. showObjects()