file = open("Session11a.py", "r")
line = file.readline()
print(line)
line = file.readline()
print(line)
line = file.readline()
print(line)
line = file.readline()
print(line)
line = file.readline()
print(line)
line = file.readline()
print(line)
line = file.readline()
print(line)
#read line will read one line
#and next time it will read next line
"""
for line in lines:
    print(lines)
"""
data = file.read(15)
print(data)
print("========")
data = file.read(30)
print(data)
file.close()