# Python function
# Definition function: Hàm định nghĩa

def ten_ham (doiso_1, doiso_2):
    # Sử dụng các đối số 
    ketqua = doiso_1 + doiso_2
    return ketqua

# 1.Phân biệt các tính năng của Hàm
# 1.1 Hàm thực hiện tác vụ hoặc chức năng nào đó không trả về kết quả
def huong_dan():
    print("""Hướng dẫn sử dụng:
    1. Bỏ gạo vào nồi
    2. Đổ nước vừa đủ""")

# huong_dan()

# 1.2 Hàm thực hiện tác vụ, có truyền đối số và trả về kết quả 
def noi_nau_com (gao, nuoc):
    huong_dan()  
    chk = ktra_nguyen_lieu(gao, nuoc) 
    if chk == True:
        return "cơm" 
    else:
        print("Nguyên liệu đưa vào nồi là sai")
        return
    

def ktra_nguyen_lieu(gao, nuoc):
    if gao =="gạo" and nuoc == "nước":
        return True
    else:
        return False

# print(ktra_nguyen_lieu("Thịt", "nước"))
nl_1 = "gạo"
nl_2 = "nước"
san_pham = noi_nau_com(nl_1, nl_2)

print("Đây là sản phẩm đầu ra:",san_pham)
