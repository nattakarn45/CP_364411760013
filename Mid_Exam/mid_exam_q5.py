"""
Nane: Nattakarn Phaewkasin
ID: 364411760013
Grop: MIT421
"""

# Question 5
# เขียนโปรแกรมคำนวนผลการเรียนโดยรับค่าอินพุตคะแนน 1 ตัวที่เป็นจำนวนจริง จากนั้นตรวจสอบค่าคะแนนดังต่อไปนี้
# ถ้าคะแนนมอยู่ระหว่าง 80.00-100.0 ให้พิมพ์ A
# ถ้าคะแนนอยู่ระหว่าง 75.0 - 79.99 ให้พิมพ์ B+
# ถ้าคะแนนอยู่ระหว่าง 70.0 - 74.99 ให้พิมพ์ B
# ถ้าคะแนนอยู่ระหว่าง 65.0 - 69.99 ให้พิมพ์ C+
# ถ้าคะแนนอยู่ระหว่าง 60.0 - 64.99 ให้พิมพ์ C
# ถ้าคะแนนอยู่ระหว่าง 55.0 - 59.99 ให้พิมพ์ D+
# ถ้าคะแนนอยู่ระหว่าง 50.0 - 54.99 ให้พิมพ์ D
# ถ้าคะแนนน้อยกว่า 49.99 ให้พิมพ์ F

""
# > 80.00-100.0 = A
# > 75.0 - 79.99  = B+
# > 70.0 - 74.99 = B
# > 65.0 - 69.99 = C+
# > 60.0 - 64.99 = C
# > 55.0 - 59.99 = D+
# > 50.0 - 54.99 = D
# < 49.99 = F
""
g = float(input("ตรวจสอบค่าคะแนน? : "))
if g <49.99:
    print("F")
elif g >= 50.0 and g <= 54.99:
    print("D")
elif g >= 55.0 and g <= 59.99:
    print("D+")
elif g >= 60.0 and g <= 64.99:
    print("C")
elif g >= 65.0 and g <= 69.99:
    print("C+")
elif g >= 70.0 and g <= 74.99:
    print("B")
elif g >= 75.0 and g <= 79.99:
    print("B+")
else:
    print("A")