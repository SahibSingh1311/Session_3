class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    """
    def __init__(self, data):
        points = data.split(",")
        self.x = int(points[0])
        self.y = int(points[1])
    """
    # If you want to have more different ways other then __init__, WE CAN CREATE METHODS OF OUR OWN
    @classmethod #decorator
    def createPoint(cls, data):
        points = data.split(",")
        refToObj = cls(pointsR)
    def showPoint(self):
        print(" point is: ",self.x,self.y)

p1 = Point()
p2 = Point(10,20)

p1.showPoint()
p2.showPoint()

file = open("point")