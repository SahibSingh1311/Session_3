cart= []
foodItem = input("ENTER A FOOD ITEM OF YOUR CHOICE")
cart.append(foodItem) #insert an element at last

print()
cart.extend(["Noodles", "MAnchuriam"]) #merge 2 strings this will merege at last and there will be change in the orignal list
cart.insert(0,"DAL") # inserting at desired index
print(cart)
#HW
#cart.pop()
#cart.push()