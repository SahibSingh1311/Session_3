employee = {"name":"John","eid":10,"email":"Johnsnow@example.com", "salary":30000}
print(len(employee))
print(max(employee), min(employee)) # it works on keys in dictionary key plays an important role
employee["name"] = "John Snow"
print(employee["name"])
keys = list(employee)
print(keys, type(keys))
# In dict we have keys as unique but values can be duplicated
#for key in keys:
 #   print(key,employee(key))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
dishes = {"dish1": 100, "dish2": 200, "dish3": 300}
keys = list(dishes)
print(keys)
value = list(dishes.values())
print(value)
index = max(value)
if index == value:
    print("working")
    print(index,keys[index])