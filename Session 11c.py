class CA(object):
    pass


class CB(CA,):
    pass


class CC(object):
    pass


cRef = CA()
print("Object data      : ", cRef.__dict__)
print("Class Data       : ", CA.__dict__)
print("Child Class Data : ", CB.__dict__)
print("Child Class Data : ", CC.__dict__)
"""
    object #parent of all Classes, Object class is also known as GOD class
   int  str     Customer
                    PrimeCustomer
"""