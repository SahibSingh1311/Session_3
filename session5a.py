# strings
# set
# dictionary

#johnsShop = 'Johns Coffee Shop' # strings can be stored using single quotes
#johnsShop = "John's Coffee Shop"
#johnsShop = 'John\'s Coffee Shop'
johnsShop = R'John\'s Coffee Shop' # raw string i.e symbols dont be considered (used in path)
print(johnsShop)

#message ="This is an awesome day." \
 #       "We will Enjoy alot." \
 #       "have fun." # break the string into multiple sentense
#print(message)
quotes = """Be Exceptional
Search for candle rather than running away from darkness"""
print(quotes)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

name = "John Watson"
print(name, type(name), hex(id(name)))
print(max(name), min(name)) #output of J is low bcs oof ascii codes

print(name[1])
print(name[len(name)-1])
print(name[1:3])
print("t" in name) # membership testing

email = "john@example.com"
if "@" in email and "." in email:
    print("valid email")
else:
    print("invalid.")

# HW: create a program to test member in sequence
# your program should work on tuple, list and set
