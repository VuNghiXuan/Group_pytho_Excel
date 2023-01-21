"1. Tìm hiểu về hàm ord: Numerical order, ASCII"
# print(ord("AA"))
"Dãy số 1, 2, 3,..., 25, 26"
"Dãy số 1, 3, 5"
# tong_so_hang = ((5-1)/2)+1

tong_so_hang = int(((26-1)/1)+1)
# print(tong_so_hang)

iCol = 16384
# print(chr(iCol-1 +65))

col_name =''

while iCol >0:
    col_name = chr(((iCol-1)%tong_so_hang)+65) + col_name
    steps = (iCol-1)//tong_so_hang
    iCol = steps
print(col_name)

