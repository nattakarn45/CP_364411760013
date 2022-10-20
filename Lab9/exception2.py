"""
Nane: Nattakarn Phaewkasin
ID: 364411760013
Grop: MIT421
"""

# Exception
print("Start")
while True:
    try:
        num = int(input("Enter an integer: "))
        print(f' You number is  {num}')
        break
    except ValueErrorError as e:
        print("Error log : ",e.args)
        print("please, enter only integer.")


print("End")
