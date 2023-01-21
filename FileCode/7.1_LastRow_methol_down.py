import xlwings as xw

in_path = r'E:\py_Excel\File_Code\excel\DanhSach.xlsx'

book = xw.Book(in_path)

shs = book.sheets
# print(shs)

sh1 = shs[0]
# print(sh1)
lr = sh1.range('B5').end('down').row

print(lr)
