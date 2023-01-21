year = 2022 # int
print('-----------1.Nhập thông tin học sinh')
nhap_ten = input('Nhập tên: ')
nhap_nam_sinh = int(input('Nhập năm sinh: '))
dToan = float(input('Nhập điểm toán: '))
dVan = float(input('Nhập điểm văn: '))
# print("+++++++",type(nhap_nam_sinh))
dtb = round((dToan+dVan)/2,3)

print('-----------2.Xuất thông tin học sinh---------')
print('Họ và tên: ',nhap_ten)
print('Tuổi: ', year - nhap_nam_sinh)
print('Điểm trung bình là:' , dtb)
print('----------------Kết thúc--------------------')
