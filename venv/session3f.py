#identity and membership operators

n1 = 10
n2 = 10
#print( n1==n2)
print( n1 is n2)# identity
#print ( n1!=n2)
print(n1 is not n2)


rollNumbers = [1,2,3,4,5]

print( 14  not in rollNumbers) #membership
#explore membership in tuple and set and dictonary
rollNumbers2 = (1,2,3,4,5,3)

print( 14  in rollNumbers2)
print(rollNumbers2[2] is rollNumbers2[4])

rollNumbers1 = {1,2,3,4,5}

print( 14  in rollNumbers1)
