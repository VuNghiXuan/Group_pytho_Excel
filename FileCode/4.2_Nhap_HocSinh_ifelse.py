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

'''2, Xếp loại học lực	
0 <= dtb <5	Yếu
5 <= dtb <6,5	TB
6,5 <= dtb <8	Khá
8 <= dtb <10	Giỏi
dtb=10	Xuất sắc'''

if 0 <= dtb and dtb <5:
    print ("Xếp loại học lực: Yếu")
elif 5 <= dtb and dtb <6.5:
    print ("Xếp loại học lực: Trung bình")
elif 6.5 <= dtb and dtb <8:
    print ("Xếp loại học lực: Khá")
elif 8 <= dtb and dtb <10:
    print ("Xếp loại học lực: Giỏi")
elif dtb == 10:    
    print ("Xếp loại học lực: Xuất sắc")
# else:   
#     print ("Xếp loại học lực: Xuất sắc")

print('----------------Kết thúc--------------------')

# Xử lý nhập điểm
'''
1, Khống chế điểm nhập vào	
0 <= dToan <=10	Nhập sai
0 <= dVan <=10	Nhập sai
'''
if dToan<0 or dToan> 10:
    print("Nhập sai điểm toán:", dToan)
if dVan<0 or dVan> 10:
    print("Nhập sai điểm văn:", dVan)

