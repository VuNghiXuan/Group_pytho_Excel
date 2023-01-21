"Input"
"Tìm hiểu dãy số tăng đều toán học, "
a  = [0, 1, 2, 3]
b  = [3, 5, 7, 9, 11, 13]

rng = [2, 3, 4, 1]
"""
1. Tìm tổng số hạng hoặc Số số hạng
    Tổng số hạng = {(số hạng cuối - số hạng đầu) / khoảng cách}+1
    Số số hạng = {(số hạng cuối tại trí trí cần tìm - số hạng đầu) / khoảng cách}+1
    ==> Như vậy tổng số hạng hoặc Số số hạng tương đương hàm len(a) trong Python
"""
tong_so_hang_a = ((3-0)/1)+1
tong_so_hang_b = ((13-3)/2)+1


print(f'tong_so_hang_a là: {tong_so_hang_a}')
print(f'tong_so_hang_b là: {tong_so_hang_b}')

"""
2. Tìm vị trí id, vị trí số hạng:
    id = giá trị của số hạng cuối tại trí trí cần tìm - tổng số hạng
    Ví dụ: vị trí cây   |---|---|---|
                        |---|---|        
                        Tính xuôi : i= Tổng số hạng - Số số hạng ==> 4-3 = 1
                        Tính ngược: i= Số số hạng - Tổng số hạng ==> 3-4 = -1
        
                Trong code:
                        Tính xuôi : id = len(a) - (len(a) - 1) ==> id = 1
                        Tính ngược: id = len(a) - 1 - len(a)   ==> id = -1

                Thay vào từng vị trí của a  = [0, 1, 2, 3]
                        id = 3 ==> 3-n = 3-4 = -1
                        id = 2 ==> 2-n = 2-4 = -2
                        id = 1 ==> 2-n = 1-4 = -3
                        id = 0 ==> 0-n = 0-4 = -4



"""
a  = [0, 1, 2, 3]
n = len(a)
print(n)
"""
Cách lấy vị trí n
    n(i) = Tổng số hạng(i) - Tổng số hạng trong dãy
    Ví dụ:
        a  = [0, 1, 2, 3] ; có n = 4 thì để xét đến vị trí cuối tức là n = n - (n-1)
        thì

"""
"""3. Các cách đếm ngược"""
print("----Cách 1:")
for i_a in range(len(a)-1,-1,-1):
    print(a[i_a])

print("----Cách 2:")
for i_a in reversed(range(len(a))):
    print(a[i_a])

print("----Cách 3:")
for i_a in range(len(a))[::-1]:
    print(a[i_a])



"""

3. Tìm tổng các số hạng trong dãy
    Tổng = (Số hạng lớn nhất của dãy + số hạng bé nhất của dãy) x số số hạng có trong dãy 
"""
print('----')
rng = range(5)
print('----xuôi')
for i in range(5):
    print(i)
print('----ngược')
for i in range(5-1,-1,-1):
    print(i)