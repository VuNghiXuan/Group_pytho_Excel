def nhap():
    for i in range(n):
        a[i] = Hocsinh(0,0,0,0)
        print('Nhập học sinh thứ:', i+1)
        a[i].ten = input('Nhập tên: ')
        a[i].lop = input('Nhập lớp: ')
        a[i].diem = float(input('Nhập điểm: '))
        a[i].truong = input('Nhập trường: ')
def xuat():
    for i in range(n):
        a[i].print_infor()
def find_max():
    dmax= a[0].diem
    imax= 0
    for i in range(n):
        if a[i].diem>dmax:
            dmax=a[i].diem
            imax = i
    a[imax].print_infor()

def sxtang():
    for i in range(n):
        for j in range(i):
            if a[i].diem<a[j].diem:
                a[i].diem, a[j].diem = a[j].diem, a[i].diem
                a[i].ten, a[j].ten = a[j].ten, a[i].ten
                a[i].lop, a[j].lop = a[j].lop, a[i].lop
                a[i].truong, a[j].truong = a[j].truong, a[i].truong
    xuat()
def sxgiam():
    for i in range(n):
        for j in range(i):
            if a[i].diem>a[j].diem:
                a[i].diem, a[j].diem = a[j].diem, a[i].diem
                a[i].ten, a[j].ten = a[j].ten, a[i].ten
                a[i].lop, a[j].lop = a[j].lop, a[i].lop
                a[i].truong, a[j].truong = a[j].truong, a[i].truong
    xuat()
def over_9():
    for i in range(n):
        if a[i].diem>=9:
            a[i].print_infor()
class Hocsinh:
    def __init__(self, ten, lop, diem, truong):
        self.ten = ten
        self.lop = lop
        self.diem = diem
        self.truong = truong
    def print_infor(self):
        print('-----------Thông tin học sinh-----------')
        print('Tên:', self.ten)
        print('Lớp:', self.lop)
        print('Điểm:', self.diem)
        print('Trường:', self.truong)
        print('----------------------------------------')

while True:
    print("""****************
    1. Nhập danh sách học sinh
    2. In danh sách học sinh
    3. Tìm danh sách học sinh có điểm cao nhất
    4. Sắp xếp học sinh tăng dần theo điểm
    5. Sắp xếp học sinh giảm dần theo điểm
    6. Liệt kê học sinh có điểm > 9
    0. Thoát
    *************************""")
    choice = int(input('Chọn chức năng từ 0->6: '))
    if choice==1:
        n=int(input('Số học sinh cần nhập: '))
        a = [0]*n
        nhap()
    if choice==2:
        xuat()
    if choice==3:
        find_max()
    if choice==4:
        sxtang()
    if choice==5:
        sxgiam()
    if choice==6:
        over_9()
    if choice==0:
        break
