import xlwings as xw

path_file = r'E:\py_Excel\File_Code\excel\obj_range.xlsx'
book  = xw.Book(path_file)

# book.save(r'E:\py_Excel\File_Code\excel\obj_range.xlsx')
shs = book.sheets
# shs.add("Bang_1")

# Ghi dữ liệu list 1D vào bảng tính
list_1d = ["Nguyễn Văn Cường","Trần Như Hoàng", "Thiên Trúc"]

shs[0].range('A6').value = list_1d

# Ghi dữ liệu list 2D vào bảng tính
list_2d = [["Nguyễn Văn Cường","Trần Như Hoàng", "Thiên Trúc"],
            ['abc', "def", 4518],
            ['der', "hgk", 'oyuo']]
shs[0].range('A10').value = list_2d








