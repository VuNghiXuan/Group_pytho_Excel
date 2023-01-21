import xlwings as xw

path_file = r'E:\py_Excel\File_Code\excel\obj_range.xlsx'
book  = xw.Book(path_file)

# book.save(r'E:\py_Excel\File_Code\excel\obj_range.xlsx')
shs = book.sheets
# shs.add("Bang_1")

# Obj Range
# rng = shs[0].range('A1:F11')
rng = shs('Bang_1').range('A1:F11')

adr_rng = rng.address


print(adr_rng)









