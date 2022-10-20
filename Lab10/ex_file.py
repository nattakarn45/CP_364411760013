"""
Nane: Nattakarn Phaewkasin
ID: 364411760013
Grop: MIT421
"""

# File I/10

# open file

f = open("test.txt")
print(f.read())  #read all text in a file
f.close()

f = open("test.txt")
print(f.read(10)) # read 10 charecters from file
f.close()

f = open("test.txt")
print(f.readline())
print(f.readline())
f.close()


f = open("test.txt")
line = f.readlines() # raed  line to list
for x in line:
    print(x)
f.close()

print(line)


count = 1
for x in range(len(line)):
    print(count,line[x])
    count += 1
    if count ==3:
        break
    count += 1