"""
Nane: Nattakarn Phaewkasin
ID: 364411760013
Grop: MIT421
"""

# Function
#  1. build- in funtion
print("Hello, MIT421")
s = "RUST"
print(len(s))

# 2. create by owner -- using "def" keyword

def myfunction1():
    print("Hello, from function 1.")

def myfunction2(msg):
    print("Hello, from function 2.",msg)

def myfunction3(num1,num2):
    print("Hello, from function 3.")
    #return statemnt
    return num1+num2

# calling funtion
myfunction1()

# calling funtion with parameter
myfunction2("RUTS")

#calling funtion with parameter and return statement
rs = myfunction3(10,10)
print(rs)

print(myfunction3(20,20))