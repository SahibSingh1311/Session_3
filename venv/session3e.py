#Bitwise operators
a = 8       #1000
b = 12      #1100
c = a & b   #1000
print(c)
c= a|b      #1100
print(c)
c= a^b      #0100
print(c)

x = 12
y = 3
#right shift (cause divide with 2^3)
#z = x >> y #1100 >>3 -> _ _ _ 1
#print(z)
#left shift( cause mmuktiply 2^3)

z= x<<y
print(z)

x=-13 #11011
y=2
z= x>>y
print("z is :",z)
#110..6.61 +11
#0100 1's compliment
#+  1 2's compliment
#0101
#0010
#+  1
#0011 -->3
