"""
Nane: Nattakarn Phaewkasin
ID: 364411760013
Grop: MIT421
"""
print("start")

def divition(a,b):
    try:
        return a/b
    except:
        raise ZeroDivisionError("devide by zero")

try:
    rs = divition(10,0)
    print("the result: ",rs)
except Exception as e:
    print("Error log: ",e.args)


print("End")