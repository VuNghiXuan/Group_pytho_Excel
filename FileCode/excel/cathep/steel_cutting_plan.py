class Loai_Thep():
    def __init__(self, cd_can_cat):
        
        self.cd_thep_can_cat = cd_can_cat
    def so_phuong_an(self):
        self.cd_chuan = 11.7
        self.so_thanh_nguyen = self.cd_chuan//self.cd_can_cat
        self.cd_con_lai = self.cd_chuan - self.so_thanh_nguyen
    def thongtin(self):
        print(f"Loại thép: {self.cd_thep_can_cat}")
        # print(f"Số thanh nguyên: {self.cd_c}")
        # print(f"Chiều dài còn lại sau khi cắt: {self.cd_con_lai}")

def main():    
    thep = Loai_Thep(1.04)
    thep.thongtin()
main()