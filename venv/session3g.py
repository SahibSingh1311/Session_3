#Conditionalvconstrains

total = 500
"""
if total >= 500:
    print("flat 40% off") #pep: pyhton enhance procedure
else:
    print("Sorry No Discount")
"""

if total>=100 and total<200:
    print("flat 10%")
elif total>=200 and total<500:
    print("flat 30%")
elif total >500:
    print ("flat 50%")
else:
    print("ADD valuables upto for disconnect")
#nested if/else
isInternetConnected = True
isGPSConnected = True
if isInternetConnected and isGPSConnected:
    print("You can browse net")
    if isGPSConnected:
        print("Access MAPS")
    else:
        print("SORRY!!")
else :
    print("Fail to browse and connect to map")

#Execute same code snippets by taking amazon or whatsapp or zomato as use case