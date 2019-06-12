#BHUT SARE DOUBT
#Seventh session in notebook
"""
        Student
            name
            phone
            email
            password
            isCollegeTraining #is wale terms have only 2 values : true or false
            collegeName
            rollNum

"""
class Student:
    pass
s1 = Student()
s1.name = "John"
s1.phone = "+91 99999 88888"
s1.email = "john@example.com"
s1.password = "pass123"
s1.isCollegeTraining = "True"
s1.collegeName = "ABC international college"
s1.rollNum = "1721078"
print(s1.__dict__)
s2 = Student()
s2.name = "John"
s2.ph = "+91 99999 88888"
s2.email = "john@example.com"
s2.passPhrase = "pass123"
s2.isCollegeTraining = "True"
s2.collegeNme = "ABC international college"
s2.roll = "1721078"
print(s2.__dict__)

# items will have different name when use on large scale
#challenge : No Standardization
# the solution to this is constructor

class Student:
    # self is a reference variable which will hold hashcode of current object
    #__init__ is known as constructor
    # constructor is aproperty of class
    def __init__(self, name, phone, email, password, isCollegeTraining, collegeName, rollNum):
        print(">> self is: ",self)
        self.fullName = name   #left side are property of object and right side are of constructor
        self.email = email # left side me hum object ke attribute bna rahe hai
        self.password = password
        self.phone = phone
        self.isCollegeTraining = isCollegeTraining
        self.collegeName = collegeName
        self.rollNum = rollNum
        # Qver writing-> a new constructor will be created and old will be removed
        """
        def __init__(self, name, phone):
        print(">> self is: ",self)
        self.fullName = name
        self.phone = phone
        """

s1 = Student("John","john@example.com","pass1234","+91 77777 88888","True","ABC Clg","1234567") #Student.__init__(s1,)
def showStudentDetails(self):
    print("Details of:", self.fullName)
    print("phone number:", self.phone)
    print("email:", self.email)

print("s1 is:  ",s1)
s2 = Student("Fionna","fionna@example.com","pass1234","+91 77999 88888","True","ABC Clg","1234765")
print("s1 is: ",s2)
print(s1.__dict__)
print(s2.__dict__)
s1.age = 22
s1.vehicleNum = "PB10AB1234"
s1.fullName = "John watson"
s2.fullName = "Fionna Flynn"
print(s1.__dict__)
print(s2.__dict__)
del s1.age
del s2.phone
print(s1.__dict__)
print(s2.__dict__)


print(s1.__dict__)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(Student.__dict__)