file = open("Session11a.py","r")

# file = open("directory") other alternative method

print(type(file))

fileContents = file.read()
print(type(fileContents))
print()

print(fileContents)
print(len(fileContents))
print("Reread File")
fileContents = file.read()
print(fileContents) # Once a file is open it cant be read again. we need to re-open and re-read it
#HW; Read a fie and create a Dictionary  whuch will tell us how many classes and objects exist
# Key will be class name and value will be number of the objects