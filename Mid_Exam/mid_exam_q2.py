"""
Nane: Nattakarn Phaewkasin
ID: 364411760013
Grop: MIT421
"""

# Question 2
# เขียนโปรแกรมรับอินพุต 1 ตัว ที่เป็นจำนวนจริง และตรวจสอบว่าจำนวนที่รับมามีค่ามากกว่า 0, น้อยกว่า 0 หรือเท่ากับ 0
#- ถ้ามีค่ามากกว่า 0 ให้ตรวจสอบต่อว่าเป็นเลขคู่หรือเลขคี่
  #- ถ้าเป็นเลขคู่ให้พิมพ์ "positive even."
  #- ถ้าเป็นเลขคี่ให้พิมพ์ "positive odd."
#- ถ้ามีค่าน้อยกว่า 0 ให้ตรวจสอบต่อว่าเป็นเลขคู่หรือเลขคี่
  #- ถ้าเป็นเลขคู่ให้พิมพ์ "negative even."
  #- ถ้าเป็นเลขคี่ให้พิมพ์ "negative odd."
#- ถ้ามีค่าเท่ากับ 0 ให้พิมพ์ "zero."

i = 0
while i < 10:
    num = int(input("Enter an integer: "))
    print("your number is : ",num)
    if num ==1:
        print("positive odd.")
    if num == 2:
        print("positive even.")
    if num == 3:
        print("positive odd.")
    if num == 4:
        print("positive even.")
    if num ==5:
        print("positive odd.")
    if num == 6:
        print("positive even.")
    if num ==7:
        print("positive odd.")
    if num == 8:
        print("positive even.")
    if num ==9:
        print("positive odd.")
    if num ==0:
        print("zero.")
        continue
    i += 1




