print("--------Thông tin học sinh------")

ten = input("Nhập tên học sinh: ")
dToan = float(input("Điểm toán: "))
dVan = float(input("Điểm văn: "))
dTB = round((dToan +dVan)/2,3)
# print(type(dToan))
# print(type(dVan))

print("---------Xuất thông tin -----------")
print ('Tên học sinh:',ten)
print('Điểm trung bình là:',dTB)

