names = ["John",  "Fionna", "Kia"]
names[0] = "Johns Watson"
print(names)

# immutable
names1 = ("John",  "Fionna", "Kia")
# names1[0] = "John Mutable"
# names.append("Kim")
print (names1)

# convert tuple into list
newNames = list(names1)
print(newNames, type(newNames))
