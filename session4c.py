data = [1, 2, 3, 4, 5, 6]
#length = len(data)
#print(length)
print(len(data))
print()
print(max(data)) #sequence of dictionary
#Iteration in List
print()
for i in range(len(data)):
    print(data[i])
    x = data[i]
    if x//2 == x/2:
        print([x**2 for x in data]) #list comprehension
        print(1)
    print("---------------------------------------------")
numbers = list(range(1, 101, 3))

print(numbers)
print("-----------------------")
print()

for elm in data: #Read All
    print(elm)
print("------------------------")
#max and in min dont work on hetrogenous