ages1 = (10, 20, 30, 40, 50, 60, 30)
ages2 = [10, 20, 30, 40, 50, 60, 30]
ages3 = {10, 20, 30, 40, 50, 60, 30}

print(ages1, hex(id(ages1)), type(ages1))
print(ages2, hex(id(ages2)), type(ages2))
print(ages3, hex(id(ages3)), type(ages3))
print()
print(hex(id(ages2)))
# PS: Tuple is IMMUTABLE -> Read Only
#     List is MUTABLE
#     Set is MUTABLE and UnOrdered due to Uniqueness
print()
for x in ages3:
    print(x, hex(id(x)))
print( ages2[3], hex(id(ages2[3])))
#print()
#print(30 in ages3)
# HW:
# How we will read in Set ?
# Answer: By using 'in' keyword in 'for' loop
# syntax : for x[any variable] in set_name:
#               print(x)
# or by checking if the value is there in the set by using following syntax
# print( x[x can be anything you want to search in the list] in [in keyword is must] set_name[name of set])
# Draw Memory Representations of sets and list!!