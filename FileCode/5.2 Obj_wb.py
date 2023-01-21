# Nhập vào thư viện xlwings
import xlwings as xw

# Cách tạo ra 1 workbook mới
wb = xw.Book()

filename = 'E:/py_Excel/File_Code/file_luu.xlsx'

# Phương thức workbook: wb
wb.save(filename)

print(wb)
