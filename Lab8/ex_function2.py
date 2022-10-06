"""
Nane: Nattakarn Phaewkasin
ID: 364411760013
Grop: MIT421
"""

# function with multiple parameter

def myfunc(*msg): # *msg --> tuple (...)
    print(msg)
    print(type(msg))

def myfunc2(*value):
    total = 0
    for x in  value:
        total += x
    #print(total)
    return total


myfunc(10)
myfunc(10,20,30)

x = myfunc2(10)
x = myfunc2(2,4,6,8,10,12,14)
print(x)




