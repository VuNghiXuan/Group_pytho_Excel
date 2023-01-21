def select_in_range(prompt, min, max):
	choice = input(prompt)
	while not choice.isdigit() or int(choice) < min or int(choice) > max:
		choice = input(prompt)

	choice = int(choice)
	return choice
def nhap():
    ten = input('Tên: ')
    tuoi = input('Năm sinh: ')
    return ten, tuoi

def chon_chuc_nang():
    while True:
        show_chuc_nang()
        n= select_in_range("Chọn số từ 0-6: ", 0, 6)
        if n==0:
            break
        elif n==1:
            nhap()


def show_chuc_nang():    
    print("""******Chọn chức năng*****
    1. Nhập danh sách học sinh
    2. In danh sách học sinh
    3. Tìm danh sách học sinh có điểm cao nhất
    4. Sắp xếp học sinh tăng dần theo điểm
    5. Sắp xếp học sinh giảm dần theo điểm
    6. Liệt kê học sinh có điểm > 9
    0. Thoát
*************************""")
        
class Truong():
    def __init__(self, name, danhsach_lop):
        self.name = name
        self.danhsach_lop = danhsach_lop
class Lop ():
    def __init__(self, name, danhsach_hocsinh):
        self.name = name
        self.danhsach_hocsinh = danhsach_hocsinh

class Hocsinh:
    def __init__(self, name, diem):
        self.name = name
        self.diem = diem
    def show(self):
        print('Tên: ', self.name)
        print('Điểm: ', self.diem)
def main():    
    chon_chuc_nang()
main()

