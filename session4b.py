tech = ["AR", "Android", "hadoop", "ios"]
tech[0] = "mobile apps" # update/ set operations
print(tech)
print()
del tech[3]
print(tech)
print(tech[-4:-1])

data = [1, 2, 3, 4, 5, "zuu", "sahib"]
data.pop(3) # removes on the bases of index
print(data)
#retrieve data from end using pop(-1)
data.remove(3) # delete on the bases of data
print(data)
