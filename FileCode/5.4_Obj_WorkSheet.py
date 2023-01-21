# Nhập vào thư viện xlwings
from ast import Delete
import xlwings as xw
import os # operating system

path_file = os.getcwd()

file_name = r'excel\file_luu.xlsx'   # raw string

full_name = os.path.join(path_file,file_name)

# Cách đọc workbook có sẵn trên máy
wb = xw.Book(full_name)

wb_name = wb.name
wb_full_path = wb.fullname
print("Đây là tên wb: ", wb_name, "và đây là đường dẫn: ", wb_full_path)


# 5.4 obj WorkSheet
shs = wb.sheets

sum_shs = len(shs)
# sh_element = shs[0].name
# print("------", sh_element)

# for loop: Cách lấy giá trị, đối tượng trong danh sách
# for sh in shs:
#     print(sh.name)

# for loop: Cách lấy index: vị trí và giá trị hoặc đối tượng trong danh sách
for id_sh in range(sum_shs): 
    print(shs[id_sh].name)

#  Cách tạo ra 1 hoặc nhiều sheet mới
# shs.add("tôi", 1)
for id_sh in range(5): 
    shs[id_sh]

#  Cách xóa 1 sheets
# shs("4").delete()

shs[2].delete()

# Đổi màu cho tab sheet
shs[1].api.Tab.ColorIndex = 4
shs('9').api.Tab.ColorIndex = 9

"api:  application propramming interface"
# Lấy tên sheet từ vị trí danh sách sheets


# Phương thức workbook: wb
# wb.save(filename)

# print(wb)

# wb.close()
# wb.app.quit()

