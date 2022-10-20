"""
Nane: Nattakarn Phaewkasin
ID: 364411760013
Grop: MIT421
"""

# create file
import os
# create empty file
try:
    f = open("test2.txt","x")
    f.close()
except:
    print("file alraedy exits.")

# create test3.txt
#C:\Users\LabCom_MT-4\Desktop\Nattakarn
try:
    f = open("C:\\Users\LabCom_MT-4\Desktop\\test3.txt","x")
    f.close()
except Exception as e:
    print(e)


# Write file
#mode "a"
try:
    f = open("test2.txt","w")
    f.write("Nattakarn Phaewkasin")
except:
    print("Cloud not found a fine name 'test2.txt")
finally:
    f.close()

# delete file #ลบไฟล์

if os.path.exists("test3.txt")
    os.remove("test3.txt")
else:
    print("File not found")