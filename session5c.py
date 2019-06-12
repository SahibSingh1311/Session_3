#build Ins on string

name = "Fionna Flynn"
new = name.upper()
print(new)
# Strings are immutable i.e whenever we perform any manipulation( modification) on string there is always a new string created on the location
anotherName = "john watson"
new = anotherName.capitalize()
print(new)
names = "John, Jennie, Jim, Jack, Joe"
idx = names.index("i")
print(idx)
new = names.replace('J','K')
print( names, new)
#num = names.count("J", 0, len(names))
num = names.count("John", 0, len(names))
print(num)

data = names.split(",")
print(data, type(data))
for n in data:
    print (data)
#strip can be used when user gives u input and accidently given space.

Quote = "Search the candle rather than cursing the darkness"
data = Quote.split(" ") #split demands a pattern here space is the repeating pattern
print(data, len(data))

salutation = "Mr."
fName = "George"
name = salutation + fName
print(name)

number = "100"
print(type(number))

if number.isdigit():
    print("n is : ", n,type(n))

song = "hello.mp3"
if song.endswith(".mp3"):
    print("play")
