"""
Nane: Nattakarn Phaewkasin
ID: 364411760013
Grop: MIT421
"""

# exception
print("Start")

x = "MIT421"

try:
    print(x)
except NameError:
    print("variable name not define.")
except:
    print("Somthing went wrong")
else:
    print("No error.")
finally:
    print("Error has been excepted.")


print("End")