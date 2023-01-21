
"1. Tìm hiểu mối quan hệ số cột và tên cột trong bảng tính Excel "
print("Chữ A là số",ord('A'))
print("Chữ B là số",ord('B'))
print("Chữ Z là số",ord('Z'))
# print("Chữ AA là số",ord('AA'))

"2. Tìm quy luật số cột --->tên cột"
"'A-->Z tương ứng 65-->90"
# Tổng số 
iCol = 27 # Nhập vào số Cột -->Cho ra tên cột A
colName = chr(iCol-1 +65)
print(colName)
"3. Hình thành dãy số"
# 0, 27, 54, 81, 108
""" Dựa vào cách tìm số hạng để tính vòng lặp
Tính số số hạng có trong dãy.

Số số hạng = (Số hạng lớn nhất của dãy – số hạng bé nhất của dãy): khoảng cách giữa hai số hạng liên tiếp trong dãy + 1

"""
iCol = 26
soHang = ((iCol-0)/27)+1
print(f'Số hạng: {soHang}')

iterate = int(soHang-1)
colname = ""
while iterate>=0:
    print(chr((iCol-1)%27) +65)
    iterate +=1

# for num in range(ord('A'),ord('Z')+1):   
#     print(f'Số {num}, tên cột là {chr(num)}')



"Bước 1:"
numCols = 16384
# Col_Name = chr(numCols-1+65)
"-----Sai khi ở cột AA"

"Bước 2:"
Col_Name =''
while numCols>0:   
    int_number = (numCols-1) // 26
    odd_number = (numCols-1) % 26
    Col_Name = chr(odd_number + 65) + Col_Name
    numCols = int_number
print(Col_Name)