# Nhập vào thư viện xlwings
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

# Phương thức workbook: wb
# wb.save(filename)

# print(wb)

# wb.close()
wb.app.quit()

