#string formating
name = "fionna"
age = 30
print("Welcome to the club %s"%(name))
print("your age is %d"%(age))
print("HEy, %s You are %d old"%(name, age))
print("Hey,",name,"You are", age, "old")
print("hey, {} you are {} old". format(name,age)) # pyhton syntax
#table of a number
number= int(input("Enter the number whoes table you want"))
for i in range(1,11):
    print("{} * {} = {}". format(number,i,number*i))