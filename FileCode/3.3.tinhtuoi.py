import datetime as dt

print("--------Thông tin học sinh------")

ten = input("Nhập tên học sinh: ")
dToan = float(input("Điểm toán: "))
dVan = float(input("Điểm văn: "))
dTB = round((dToan +dVan)/2,3)

nam_sinh = int(input("Nhập năm sinh: "))
nam_hientai = dt.date.today().year
tuoi = nam_hientai-nam_sinh

# print(type(dToan))
# print(type(dVan))

print("---------Xuất thông tin -----------")
print ('Tên học sinh:',ten)
print('Số tuổi:',tuoi)
print('Điểm trung bình là:',dTB)





# tuoi = nam_hientai - nam_sinh

